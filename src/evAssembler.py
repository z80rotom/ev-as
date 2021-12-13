import struct
from dataclasses import dataclass

from antlr4 import *
from UnityPy.streams import EndianBinaryReader, EndianBinaryWriter

from ev_argtype import EvArgType
if __name__ is not None and "." in __name__:
    from .evParser import evParser
else:
    from evParser import evParser

from evListener import evListener
from ev_cmd import EvCmdType

MAX_WORK = 500
MAX_FLAG = 4000
MAX_SYS_FLAG = 1000

@dataclass
class EvArg:
    argType: int
    data: int

@dataclass
class EvCmd:
    cmdType: EvCmdType
    args: list

def encode_float(var):
    var = float(var)
    data = int(struct.unpack('<i', struct.pack('<f', var))[0])
    return data

class evAssembler(evListener):
    currentLabel = None
    scripts = {}
    strTbl = []
    currCmdIdx = -1
    writer = EndianBinaryWriter()

    def enterLabel(self, ctx:evParser.LabelContext):
        lbl = ctx.getChild(0)
        lblName = str(lbl.getChild(0))
        self.currentLabel = lblName
        self.scripts[self.currentLabel] = []
        self.currCmdIdx = -1

    def enterEvCmd(self, ctx:evParser.EvCmdContext):
        name = str(ctx.getChild(0))
        if not hasattr(EvCmdType, name):
            # NOTE: should probably be an error
            print("Invalid EvCmd")
            return
        evCmdType = getattr(EvCmdType, name)
        args = []
        evCmd = EvCmd(evCmdType, args)
        self.scripts[self.currentLabel].append(evCmd)
        self.currCmdIdx += 1

    def enterNumber(self, ctx: evParser.NumberContext):
        # Note this probably won't always work this well
        argVal = encode_float(float(str(ctx.getChild(0))))
        try:
            self.writer.write_int(argVal)
        except Exception as exc:
            print("Invalid float: {}".format(argVal))
        # Defaulting to argType 1 since that is passing by value
        # but that just simply isn't true for most of these
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.Value, argVal)
        )
    
    def enterWork(self, ctx: evParser.WorkContext):
        # Note this probably won't always work this well
        argVal = int(str(ctx.getChild(0))[1:])

        # Defaulting to argType 1 since that is passing by value
        # but that just simply isn't true for most of these
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.Work, argVal)
        )

        if argVal > MAX_WORK:
            print("[Warning] line {}:{} Invalid work: @{}".format(ctx.start.line, ctx.start.column, argVal))

    def enterFlag(self, ctx: evParser.FlagContext):
        # Note this probably won't always work this well
        argVal = int(str(ctx.getChild(0))[1:])
        # Defaulting to argType 1 since that is passing by value
        # but that just simply isn't true for most of these
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.Flag, argVal)
        )
    
        if argVal > MAX_FLAG:
            print("[Warning] line {}:{} Invalid Flag: #{}".format(ctx.start.line, ctx.start.column, argVal))

    def enterSysFlag(self, ctx: evParser.SysFlagContext):
        # Note this probably won't always work this well
        argVal = int(str(ctx.getChild(0))[1:])
        # Defaulting to argType 1 since that is passing by value
        # but that just simply isn't true for most of these
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.SysFlag, argVal)
        )
    
    def enterString_(self, ctx: evParser.String_Context):
        strVal = str(ctx.getChild(0))[1:-1] # Trim off apostrophes
        if strVal not in self.strTbl:
            self.strTbl.append(strVal)
        argVal = self.strTbl.index(strVal)
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.String, argVal)
        )    

        if argVal > MAX_SYS_FLAG:
            print("[Warning] line {}:{} Invalid System Flag: ${}".format(ctx.start.line, ctx.start.column, argVal))
