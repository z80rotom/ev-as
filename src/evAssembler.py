from enum import IntEnum, auto
import struct
from dataclasses import dataclass
import sys

from antlr4 import *
from UnityPy.streams import EndianBinaryReader, EndianBinaryWriter

from ev_argtype import EvArgType
from ev_macro import EvMacroType
import msbt
if __name__ is not None and "." in __name__:
    from .evParser import evParser
else:
    from evParser import evParser

from evListener import evListener
from ev_cmd import EvCmdType
from ev_work import EvWork
from ev_flag import EvFlag
from ev_sys_flag import EvSysFlag

MAX_WORK = 500
MAX_FLAG = 4000
MAX_SYS_FLAG = 1000

MACRO_NAME_CMD_TABLE = {
    EvCmdType._POKE_TYPE_NAME : msbt.TagID.PokeType,
    EvCmdType._NUMBER_NAME : msbt.TagID.Number
}

@dataclass
class EvCmdTypeWrapper:
    name: str
    value: int

    def __hash__(self):
        return self.value

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
    filename: str

@dataclass
class EvMacro:
    cmdType: EvMacroType
    args: list
    line: int
    column: int

    def isValid(self):
        return self.cmdType.isValid()

class Indicator(IntEnum):
    ScrollPage = auto()
    ScrollLine = auto()
    NewLine = auto()
    TagStart = auto()
    TagEnd = auto()
    End = auto()

def encode_float(var):
    var = float(var)
    data = int(struct.unpack('<i', struct.pack('<f', var))[0])
    return data

def calculateStrWidth(inputString):
    charDict = {
        "A" :20.125,
        "B" :17.3125,
        "C" :20.25,
        "D" :22.109375,
        "E" :15.84375,
        "F" :16.15625,
        "G" :23.328125,
        "H" :22.015625,
        "I" :8.390625,
        "J" :12.640625,
        "K" :19.046875,
        "L" :14.96875,
        "M" :25.984375,
        "N" :21.625,
        "O" :24.390625,
        "P" :16.28125,
        "Q" :24.390625,
        "R" :17.625,
        "S" :15.453125,
        "T" :17.125,
        "U" :21.34375,
        "V" :20.0,
        "W" :28.640625,
        "X" :20.28125,
        "Y" :19.328125,
        "Z" :18.171875,
        "a" :15.296875,
        "b" :17.25,
        "c" :13.953125,
        "d" :17.28125,
        "e" :15.96875,
        "é" :15.96875,
        "f" :9.765625,
        "g" :16.1875,
        "h" :15.578125,
        "i" :7.609375,
        "j" :7.328125,
        "k" :14.8125,
        "l" :7.78125,
        "m" :22.71875,
        "n" :15.578125,
        "o" :17.15625,
        "p" :17.25,
        "q" :17.28125,
        "r" :9.65625,
        "s" :11.515625,
        "t" :10.046875,
        "u" :15.578125,
        "v" :14.078125,
        "w" :19.8125,
        "x" :14.46875,
        "y" :14.375,
        "z" :13.03125,
        "1" :0,
        "2" :0,
        "3" :0,
        "4" :0,
        "5" :0,
        "6" :0,
        "7" :0,
        "8" :0,
        "9" :0,
        "0" :0,
        "-" : 11.203125,
        "!" : 7.265625,
        "?" : 14.46875,
        '"' : 13.03125,
        " " : 8.671875,
        "," : 8.828125,
        "." : 7.90625,
        "'" : 8.828125
    }
    total = 0.0
    for char in inputString:
        if char == "'":
            char = "’"
        try:
            total += charDict[char]
        except:
            total += charDict[" "]
    return total

class MacroAssembler:
    def __init__(self, fileName):
        self.fileName = fileName
        self.labelDatas = {}
    
    def parseText(self, origText):
        origText = origText.replace('\r\n', '\\n')
        origText = origText.replace('\n', '\\n') # Just in case
        # Don't want things ending with these seperators, nasty business
        if origText.endswith('\\r'):
            origText = origText[:-2]
        text = origText
        splitters = ['\\n', '\\r', '\\f', '{', '}']
        items = {}
        indicators = {}
        lastIndex = 0
        while True:
            indices = {}
            for splitter in splitters:
                if splitter in text:
                    indices[text.index(splitter)] = splitter
            if not indices:
                break
            i = min(indices.keys())
            splitter = indices[i]
            indicator = None
            if splitter == '\\r':
                indicator = Indicator.ScrollPage
            if splitter == '\\n':
                indicator = Indicator.NewLine
            if splitter == '\\f':
                indicator = Indicator.ScrollLine
            if splitter == '}':
                indicator = Indicator.TagEnd
            if splitter == '{':
                indicator = Indicator.TagStart
            indicators[text.index(splitter)+lastIndex] = indicator
            items[text.index(splitter)+lastIndex] = text[:text.index(splitter)]
            lastIndex = text.index(splitter)+lastIndex
            text = text[text.index(splitter)+len(splitter):]
        try:
            max_idx = max(items.keys())
        except ValueError:
            max_idx = 0
        idx = max_idx
        if items:
            idx += len(items[idx])
        items[idx] = text
        indicators[idx] = Indicator.End
        return {
            "items" : items,
            "indicators" : indicators
        }

    def genLabelData(self, labelName, text, tags):
        TAG_COMMANDS = {
            "PLAYER",
            "RIVAL",
            "SUPPORT"
            "RIVAL_POKEMON_NAME",
            "SUPPORT_POKEMON_NAME",
            # TODO: Add support for the following
            # SPEAKERS_NAME
            # ITEM_NAME
            # ITEM_WAZA_NAME
            # NUMBER_NAME
            # SEAL_NAME
            # PARK_ITEM_NAME
            # POKETCH_NAME
            # GOODS_NAME
            # TRAP_NAME
            # TAMA_NAME
            # NUMBER_NAME
            # ACCE_NAME
            # IMC_BG_NAME
        }
        styleInfo = msbt.StyleInfo.default()
        attributeValueArray = msbt.LabelData.defaultAttributeValueArray()
        tagDataArray = []
        wordDataArray = []

        textTree = self.parseText(text.data)
        items = textTree["items"]
        indicators = textTree["indicators"]
        for pos in items:
            item: str = items[pos]
            indicator = indicators[pos]
            if indicator == Indicator.NewLine:
                wordDataArray.append(msbt.WordData(
                    msbt.WordDataPatternID.Event,
                    msbt.MsgEventID.NewLine,
                    -1,
                    0.0,
                    item,
                    calculateStrWidth(item)
                ))
            if indicator == Indicator.ScrollLine:
                wordDataArray.append(msbt.WordData(
                    msbt.WordDataPatternID.Event,
                    msbt.MsgEventID.ScrollLine,
                    -1,
                    0.0,
                    item,
                    calculateStrWidth(item)
                ))                
            if indicator == Indicator.ScrollPage:
                wordDataArray.append(msbt.WordData(
                    msbt.WordDataPatternID.Event,
                    msbt.MsgEventID.ScrollPage,
                    -1,
                    0.0,
                    item,
                    calculateStrWidth(item)
                ))
            if indicator == Indicator.TagStart:
                wordDataArray.append(msbt.WordData(
                    msbt.WordDataPatternID.Str,
                    msbt.MsgEventID.NONE,
                    -1,
                    0.0,
                    item,
                    calculateStrWidth(item)
                ))
            if indicator == Indicator.TagEnd:
                if not item.isdigit():
                    # TODO: Raise exception
                    pass
                # Just the tag index
                tagIndex = int(item)
                # This tag index seems to be the index into the
                # tagData array whereas the other tagIndex is the 
                # 
                wordDataArray.append(msbt.WordData(
                    msbt.WordDataPatternID.WordTag,
                    msbt.MsgEventID.NONE,
                    len(tagDataArray),
                    0.0,
                    "",
                    -1.0
                ))
                tagID = msbt.TagID.Default
                if tagIndex in tags:
                    tagID = tags[tagIndex]
                tagDataArray.append(msbt.TagData(
                    tagIndex,
                    msbt.GroupTagID.Name,
                    tagID,
                    msbt.TagPatternID.Word,
                    0,
                    0,
                    [],
                    msbt.ForceGrmID.NONE
                ))
            if indicator == Indicator.End:
                wordDataArray.append(msbt.WordData(
                    msbt.WordDataPatternID.Str,
                    msbt.MsgEventID.End,
                    -1,
                    0.0,
                    item,
                    calculateStrWidth(item)
                ))

        return msbt.LabelData(
            0,
            0,
            labelName.data,
            styleInfo,
            attributeValueArray,
            tagDataArray,
            wordDataArray
        )

    def processTextMacro(self, cmdType, macro, commands, strTbl, tags):
        # TODO: Add a list of valid msg files
        try:
            msgFile: EvArg = macro.args[0]
            if msgFile.argType != EvArgType.MacroString:
                raise RuntimeError("Invalid parameter {} passed to EvMacro: {} at {}:{}:{}", msgFile.data, macro, self.fileName, msgFile.line, msgFile.column)
        except IndexError:
            raise RuntimeError("EvMacro: {} is missing argument msgFile at {}:{}:{}", macro, self.fileName, msgFile.line, msgFile.column)
        
        # TODO: Add validate the actual contents of the label
        # to ensure it's proper utf-8 string.
        try:
            label: EvArg = macro.args[1]
            if label.argType != EvArgType.MacroString:
                raise RuntimeError("Invalid parameter {} passed to EvMacro: {} at {}:{}:{}", label.data, macro, self.fileName, label.line, msgFile.column)
        except IndexError:
            raise RuntimeError("EvMacro: {} is missing argument label at {}:{}:{}", macro, self.fileName, label.line, label.column)
        
        try:
            text: EvArg = macro.args[2]
            if text.argType != EvArgType.MacroString:
                raise RuntimeError("Invalid parameter {} passed to EvMacro: {} at {}:{}:{}", text.data, macro, self.fileName, text.line, msgFile.column)
        except IndexError:
            raise RuntimeError("EvMacro: {} is missing argument text at {}:{}:{}", macro, self.fileName, text.line, text.column)
        
        strVal = "{}%{}".format(msgFile.data, label.data)
        # if strVal in self.msg_keys:
        #    raise RuntimeError("EvMacro: {}. Label `{}` is already used at {}:{}:{}".format(macro.cmdType.name, strVal, self.fileName, text.line, text.column))
        macroCommands = []
        labelData = self.genLabelData(label, text, tags)

        if strVal not in strTbl:
            strTbl.append(strVal)
        # self.msg_keys.append(strVal)
        self.labelDatas[strVal] = labelData
        
        # Create the main command and add it to the commands list
        argVal = strTbl.index(strVal)
        evCmdArgs = [EvArg(EvArgType.String, argVal, msgFile.line, msgFile.column)]
        evCmdArgs.extend(macro.args[3:])
        macroCommands.append(EvCmd(cmdType, evCmdArgs, macro.line, macro.column, self.fileName))

        commands.extend(macroCommands)
        return len(macroCommands)

    def process(self, macro, commands, strTbl, tags):
        if macro.cmdType == EvMacroType.Invalid:
            raise RuntimeError("Invalid EvCmd or EvMacro: {} at {}:{}:{}".format(macro, self.fileName, macro.line, macro.column))
        textMacroMap = {
            EvMacroType._MACRO_TALKMSG : EvCmdType._TALKMSG,
            EvMacroType._MACRO_TALK_KEYWAIT : EvCmdType._TALK_KEYWAIT,
            EvMacroType._MACRO_EASY_OBJ_MSG : EvCmdType._EASY_OBJ_MSG,
            EvMacroType._MACRO_ADD_CUSTUM_WIN_LABEL : EvCmdType._ADD_CUSTUM_WIN_LABEL
        }

        if macro.cmdType in textMacroMap:
            evCmdType = textMacroMap[macro.cmdType]
            return self.processTextMacro(evCmdType, macro, commands, strTbl, tags)

        raise RuntimeError("Invalid EvMacro: {} at {}:{}:{}".format(macro, self.fileName, macro.line, macro.column))

class evAssembler(evListener):
    def __init__(self, fileName, commands=None, flags=None, works=None, sysflags=None):
        self.fileName = fileName
        self.macro = EvMacro(EvMacroType.Invalid, [], 0, 0)
        self.macroAssembler = MacroAssembler(fileName)
        self.currentLabel = None
        self.scripts = {}
        self.strTbl = []
        self.currCmdIdx = -1
        self.writer = EndianBinaryWriter()
        self.commands = {} if commands is None else commands
        self.flags = {} if flags is None else flags
        self.works = {} if works is None else works
        self.sysflags = {} if sysflags is None else sysflags

    def enterLbl(self, ctx: evParser.LblContext):
        lblName = ctx.name().getText()
        commands = []
        for instructionCtx in ctx.instruction():
            isMacro = False
            macroType = None
            tags = {}
            cmdName = instructionCtx.name()
            cmdName = cmdName.upper()
            evCmdType = None

            if hasattr(EvMacroType, cmdName):
                # Not a command, but a macro, set the current macro so I can get it on
                macroType = getattr(EvMacroType, cmdName)
                isMacro = True
            
            if not hasattr(EvCmdType, cmdName):
                if cmdName in self.commands:
                    evCmdType = EvCmdTypeWrapper(cmdName, self.commands[cmdName])
                else:
                    raise RuntimeError("Invalid EvCmd or EvMacro: {} at {}:{}:{}".format(cmdName, self.fileName, ctx.start.line, ctx.start.column))
            else:
                evCmdType = getattr(EvCmdType, cmdName)
            args = []

            for arg in instructionCtx.expressionlist().argument()
                if arg.number() is not None:
                    args.append(self.parseNumber(arg.number(), evCmdType, tags, isMacro))
                    continue
                if arg.work() is not None:
                    argVal = self.parseNameValue(arg.work(), EvWork, self.works)
                    if argVal is None:
                        raise RuntimeError("Unknown work: @{}. Cannot convert to number {}:{}:{}".format(argVal, self.fileName, arg.work().start.line, arg.work().start.column))
                    if argVal > MAX_WORK:
                        print("[Warning] line {}:{}:{} Invalid work: @{}".format(self.fileName, arg.work().start.line, arg.work().start.column, argVal))
                    args.append(EvArg(EvArgType.Work, argVal, arg.work().start.line, arg.work().start.column))
                    continue
                if arg.flag() is not None:
                    argVal = self.parseNameValue(arg.work(), EvWork, self.works)
                    if argVal is None:
                        raise RuntimeError("Unknown Flag: #{}. Cannot convert to number {}:{}:{}".format(argVal, self.fileName, arg.flag().start.line, arg.flag().start.column))
                    if argVal > MAX_FLAG:
                        print("[Warning] line {}:{}:{} Invalid Flag: #{}".format(self.fileName, arg.flag().start.line, arg.flag().start.column, argVal))
                    args.append(EvArg(EvArgType.Flag, argVal, arg.flag().start.line, arg.flag().start.column))
                    continue
                if arg.sysFlag() is not None:
                    argVal = self.parseNameValue(arg.work(), EvSysFlag, self.sys_flags)
                    if argVal is None:
                        raise RuntimeError("Unknown SysFlag: ${}. Cannot convert to number {}:{}:{}".format(argVal, self.fileName, arg.sysFlag().start.line, arg.sysFlag().start.column))
                    if argVal > MAX_SYS_FLAG:
                        print("[Warning] line {}:{}:{} Invalid SysFlag: ${}".format(self.fileName, arg.sysFlag().start.line, arg.sysFlag().start.column, argVal))
                    args.append(EvArg(EvArgType.SysFlag, argVal, arg.sysFlag().start.line, arg.sysFlag().start.column))
                    continue
            if isMacro:
                self.macro = EvMacro(macroType, args, ctx.start.line, ctx.start.column)
                self.currCmdIdx += self.macroAssembler.process(self.macro, self.scripts[self.currentLabel], self.strTbl, tags)
            else:
                evCmd = EvCmd(evCmdType, args, ctx.start.line, ctx.start.column, self.fileName)
                commands.append(evCmd)
        self.scripts[lblName] = commands

    def enterDefine(self, ctx: evParser.DefineContext):
        work = ctx.work()
        flag = ctx.flag()
        sysflag = ctx.sysFlag()
        number = ctx.number()
        value = int(str(number.NUMBER().getText()))

        if work is not None:
            key = str(work.NAME().getText()).upper()
            if value > MAX_WORK:
                raise RuntimeError("Invalid work definition: @{}. {} greater than max work value {} at {}:{}:{}".format(key, value, MAX_WORK, self.fileName, ctx.start.line, ctx.start.column))
            self.works[key] = value
        if flag is not None:
            key = str(flag.NAME().getText()).upper()
            if value > MAX_FLAG:
                raise RuntimeError("Invalid flag definition: #{}. {} greater than max flag value {} at {}:{}:{}".format(key, value, MAX_FLAG, self.fileName, ctx.start.line, ctx.start.column))
            self.flags[key] = value
        if sysflag is not None:
            key = str(sysflag.NAME().getText()).upper()
            if value > MAX_SYS_FLAG:
                raise RuntimeError("Invalid SysFlag definition: ${}. {} greater than max sysflag value {} at {}:{}:{}".format(key, value, MAX_SYS_FLAG, self.fileName, ctx.start.line, ctx.start.column))
            self.sysflags[key] = value

    def parseNumber(self, ctx: evParser.NumberContext, cmdType, tags, isMacro):
        argVal = encode_float(float(ctx.NUMBER.getText()))
        try:
            self.writer.write_int(argVal)
        except Exception as exc:
            print("Invalid float: {}".format(argVal))
        
        if not isMacro:
            if cmdType in MACRO_NAME_CMD_TABLE:
                tags[argVal] = MACRO_NAME_CMD_TABLE[cmdType]
        return EvArg(EvArgType.Value, argVal, ctx.start.line, ctx.start.column)
    
    def parseNameValue(self, ctx, enumCls, fallback):
        if ctx.NUMBER():
            argVal = int(ctx.NUMBER().getText())
        else:
            name = ctx.NAME().getText().upper()
            if hasattr(enumCls, name):
                argVal = getattr(enumCls, name)
            elif argVal in fallback:
                argVal = fallback[name]
        return argVal
    
    def parseString_(self, ctx: evParser.String_Context, isMacro):
        strVal = ctx.getText()[1:-1] # Trim off apostrophes
        if isMacro:
            return EvArg(EvArgType.MacroString, strVal, ctx.start.line, ctx.start.column)
        if strVal not in self.strTbl:
            self.strTbl.append(strVal)
        argVal = self.strTbl.index(strVal)
        return EvArg(EvArgType.String, argVal, ctx.start.line, ctx.start.column)