import os
import struct
import json
import glob
from argparse import ArgumentParser

import UnityPy

from antlr4 import *
from evAssembler import EvCmd, evAssembler
from evLexer import evLexer
from evParser import evParser

from ev_argtype import EvArgType
from ev_cmd import EvCmdType
from function_definitions import FunctionDefinition


class GDataManager:
    SCENARIO_MSGS = None
    DISABLED_MSGS = False

    @classmethod
    def getMoveById(cls, moveId):
        move_list = cls.getMoveList()
        return move_list[moveId]

    @classmethod
    def getScenarioMsgList(cls):
        if cls.DISABLED_MSGS:
            return None
        if not cls.SCENARIO_MSGS:
            dataFiles = ['dp_scenario1' ,
                'dp_scenario2',
                'dp_scenario3',
                'dp_options',
                'ss_report' ,
                'dlp_underground' ,
                'dp_tvshow',
                'dlp_net_union_room',
                'dp_trainer_msg_sub',
                'dp_poffin_main',
                'ss_fld_shop',
                'dlp_gmstation',
                'dlp_rotom_message',
                'ss_fld_dressup',
                'dp_net_communication',
                'dp_contest',
                'ss_net_net_btl',
                'ss_btl_tower_main',
                'ss_btl_tower_menu_ui_text',
            ]
            scenario_msgs = {}

            try:
                for dateFile in dataFiles:
                    ifpath = "AssetFolder/english_Export/english_{}.json".format(dateFile)
                    array = []
                    with open(ifpath, "r", encoding='utf-8') as ifobj:
                        data = json.load(ifobj)
                        for entry in data["labelDataArray"]:
                            labelName = entry["labelName"]
                            array.append(labelName)
                    scenario_msgs[dateFile] = array
            except FileNotFoundError as exc:
                cls.DISABLED_MSGS = True
                print("Warning: english files not found. Message validation will not be enabled: {}".format(exc))
                return None
            cls.SCENARIO_MSGS = scenario_msgs
        return cls.SCENARIO_MSGS    

def jsonDumpUnity(tree, ofpath):
    with open(ofpath, "w") as ofobj:
        json.dump(tree, ofobj, indent=4)

def validate_talk_msg(cmd: EvCmd, strList):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

def validate_talk_keywait(cmd: EvCmd, strList: list):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

def validate_easy_obj_msg(cmd: EvCmd, strList: list):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

def validate_add_custum_win_label(cmd: EvCmd, strList: list):
    scenarioMsgList = GDataManager.getScenarioMsgList()
    if scenarioMsgList is None:
        return
    msgIdx = cmd.args[0].data
    msg = strList[msgIdx]
    splitMsg = msg.split('%')
    try:
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
    except IndexError:
        return
        # raise RuntimeError('Invalid msg: {} passed to {} at {}: {}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

    if dataFile not in scenarioMsgList:
        raise RuntimeError('Unknown datafile: {} passed to {} at {}:{}'.format(dataFile, cmd.cmdType.name, cmd.line, cmd.column))
    if unlocalized_key not in scenarioMsgList[dataFile]:
        raise RuntimeError('Unknown message: {} passed to {} at {}:{}'.format(msg, cmd.cmdType.name, cmd.line, cmd.column))

VALIDATE_TABLE = {
    EvCmdType._TALKMSG : validate_talk_msg,
    EvCmdType._TALK_KEYWAIT : validate_talk_keywait,
    EvCmdType._EASY_OBJ_MSG : validate_easy_obj_msg,
    EvCmdType._ADD_CUSTUM_WIN_LABEL : validate_add_custum_win_label
}

def convertToUnity(ifpath, scripts, strList):
    # FunctionDefinition.load("ev_scripts.json")
    tree = {}
    treeScripts = []

    for label, script in scripts.items():
        scriptCommands = []
        for cmd in script:
            evCmdType = cmd.cmdType
            # funcDef = FunctionDefinition.getFunctionDefinition(evCmdType)
            scriptArgs = [
                {
                    "argType" : EvArgType.CmdType,
                    "data" : evCmdType.value
                }
            ]

            if evCmdType in VALIDATE_TABLE:
                valid_func = VALIDATE_TABLE[evCmdType]
                try:
                    valid_func(cmd, strList)
                except RuntimeError as exc:
                    print(exc)

            # reqArgs = funcDef.noReqArgs()
            # if len(cmd.args) < reqArgs:
            #     print("[Warning] {}:{} Too few arguments passed in. At least {} required. {} provided.".format(cmd.line, cmd.column, reqArgs, len(cmd.args)))
            # noMaxArgs = funcDef.maxArgs()
            # if len(cmd.args) > noMaxArgs:
            #     print("[Warning] {}:{}  Too many arguments passed in. At most {} allowed. {} provided.".format(cmd.line, cmd.column, noMaxArgs, len(cmd.args)))
            
            for i, arg in enumerate(cmd.args):
                # argDef = funcDef.validArgs[i]
                #if arg.argType not in argDef.validArgTypes:
                #    print("[Warning] {} {}:{} invalid argument".format(ifpath, arg.line, arg.column))
                

                scriptArgs.append({
                    "argType" : arg.argType,
                    "data" : arg.data
                })
            
            scriptCommands.append({
                "Arg" : scriptArgs
            })

        treeScripts.append({
            "Label" : label,
            "Commands" : scriptCommands
        })
    tree["Scripts"] = treeScripts
    tree["StrList"] = strList
    return tree

def repackUnity(ofpath, script, unityTree):
    with open(ofpath, "rb") as ifobj:
        bundle = UnityPy.load(ofpath)

        for obj in bundle.objects:
            if obj.type.name == "MonoBehaviour":
                data = obj.read()
                if obj.serialized_type.nodes:
                        tree = obj.read_typetree()
                        if data.name == script:
                            tree.update(unityTree)
                            obj.save_typetree(tree)
    
    
    with open(ofpath, "wb") as ofobj:
        # Thanks Aldo796
        ofobj.write(bundle.file.save(packer=(64,2)))

def assemble(ifpath, ofpath, script):
    input_stream = FileStream(ifpath)
    lexer = evLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = evParser(stream)
    tree = parser.prog()

    assembler = evAssembler()
    walker = ParseTreeWalker()
    walker.walk(assembler, tree)
    unityTree = convertToUnity(assembler.scripts, assembler.strTbl)
    repackUnity(ofpath, script, unityTree)

def repackUnityAll(ifpath, ofpath, scripts):
    with open(ifpath, "rb") as ifobj:
            bundle = UnityPy.load(ifpath)

            for obj in bundle.objects:
                if obj.type.name == "MonoBehaviour":
                    data = obj.read()
                    if obj.serialized_type.nodes:
                            tree = obj.read_typetree()
                            if data.name in scripts:
                                unityTree = scripts[data.name]
                                tree.update(unityTree)
                                obj.save_typetree(tree)
    
    with open(ofpath, "wb") as ofobj:
        # Thanks Aldo796
        ofobj.write(bundle.file.save(packer=(64,2)))

def assemble_all():
    scripts = {}
    for ifpath in glob.glob("scripts/*.ev"):
        basename = os.path.basename(ifpath)
        basename = os.path.splitext(basename)[0]
        input_stream = FileStream(ifpath)
        lexer = evLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = evParser(stream)
        tree = parser.prog()

        assembler = evAssembler(ifpath)
        walker = ParseTreeWalker()
        walker.walk(assembler, tree)
        unityTree = convertToUnity(ifpath, assembler.scripts, assembler.strTbl)
        scripts[basename] = unityTree
    repackUnityAll("Dpr/ev_script", "bin/ev_script", scripts)

def main():
    # parser = ArgumentParser()
    # parser.add_argument("-i", "--input", dest='ifpath', action='store', required=True)
    # parser.add_argument("-o", "--output", dest='ofpath', action='store', required=True)
    # parser.add_argument("-s", "--script", dest='script', action='store', required=True)

    # vargs = parser.parse_args()
    # assemble(vargs.ifpath, vargs.ofpath, vargs.script)
    assemble_all()
    print("Assembly finished")

if __name__ == "__main__":
    main()