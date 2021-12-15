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
    line: int
    column: int

@dataclass
class EvCmd:
    cmdType: EvCmdType
    args: list
    line: int
    column: int

def encode_float(var):
    var = float(var)
    data = int(struct.unpack('<i', struct.pack('<f', var))[0])
    return data

class evAssembler(evListener):
    def __init__(self):
        self.currentLabel = None
        self.scripts = {}
        self.strTbl = []
        self.currCmdIdx = -1
        self.writer = EndianBinaryWriter()

    def enterLbl(self, ctx: evParser.LblContext):
        lbl = ctx.getChild(0)
        # If someone can get the grammar working a bit better
        # then this replace can go away, but I can't get the :
        # in the right rule not to do this without making labels
        # unable to start with _
        lblName = str(lbl).replace(':', '')
        self.currentLabel = lblName
        self.scripts[self.currentLabel] = []
        self.currCmdIdx = -1

    def enterEvCmd(self, ctx:evParser.EvCmdContext):
        name = str(ctx.getChild(0))
        if not hasattr(EvCmdType, name):
            # NOTE: should probably be an error
            print("Invalid EvCmd: {}".format(name))
            return
        evCmdType = getattr(EvCmdType, name)
        args = []
        evCmd = EvCmd(evCmdType, args, ctx.start.line, ctx.start.column)
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
            EvArg(EvArgType.Value, argVal, ctx.start.line, ctx.start.column)
        )
    
    def enterWork(self, ctx: evParser.WorkContext):
        # Note this probably won't always work this well
        argVal = int(str(ctx.getChild(0))[1:])

        # Defaulting to argType 1 since that is passing by value
        # but that just simply isn't true for most of these
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.Work, argVal, ctx.start.line, ctx.start.column)
        )

        if argVal > MAX_WORK:
            print("[Warning] line {}:{} Invalid work: @{}".format(ctx.start.line, ctx.start.column, argVal))

    def enterFlag(self, ctx: evParser.FlagContext):
        # Note this probably won't always work this well
        argVal = int(str(ctx.getChild(0))[1:])
        # Defaulting to argType 1 since that is passing by value
        # but that just simply isn't true for most of these
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.Flag, argVal, ctx.start.line, ctx.start.column)
        )
    
        if argVal > MAX_FLAG:
            print("[Warning] line {}:{} Invalid Flag: #{}".format(ctx.start.line, ctx.start.column, argVal))

    def enterSysFlag(self, ctx: evParser.SysFlagContext):
        # Note this probably won't always work this well
        argVal = int(str(ctx.getChild(0))[1:])
        # Defaulting to argType 1 since that is passing by value
        # but that just simply isn't true for most of these
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.SysFlag, argVal, ctx.start.line, ctx.start.column)
        )
    
    def enterString_(self, ctx: evParser.String_Context):
        strVal = str(ctx.getChild(0))[1:-1] # Trim off apostrophes
        if strVal not in self.strTbl:
            self.strTbl.append(strVal)
        argVal = self.strTbl.index(strVal)
        self.scripts[self.currentLabel][self.currCmdIdx].args.append(
            EvArg(EvArgType.String, argVal, ctx.start.line, ctx.start.column)
        )    

        if argVal > MAX_SYS_FLAG:
            print("[Warning] line {}:{} Invalid System Flag: ${}".format(ctx.start.line, ctx.start.column, argVal))
