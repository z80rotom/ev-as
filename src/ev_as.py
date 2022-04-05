import os
import struct
import json
import glob
from argparse import ArgumentParser

import UnityPy
import marshmallow

from antlr4 import *
from evAssembler import EvCmd, evAssembler
from evLexer import evLexer
from evParser import evParser

from ev_argtype import EvArgType
from ev_cmd import EvCmdType
from function_definitions import FunctionDefinition
from msbt import MsbtFile

DATA_FILES =  ['dp_scenario1',
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
            scenario_msgs = {}

            try:
                for dateFile in DATA_FILES:
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
    return
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
    return
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
    return
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
    return
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

def updateLabelDatas(path, lang, labelDatas):
    print("Updating message files using Macro information.")
    msbt_files = {}
    for data_file in DATA_FILES:
        ifpath = os.path.join(path, "{}_{}.json".format(lang, data_file))
        with open(ifpath, "r", encoding='utf-8') as ifobj:
            try:
                msbt_file = MsbtFile.Schema().loads(ifobj.read())
            except marshmallow.exceptions.ValidationError as exc:
                print("Failed to load: {}. Unable to update message files".format(ifpath))
                print(exc)
                return
            msbt_files[data_file] = msbt_file
    for scriptMessage, labelData in labelDatas.items():
        splitMsg = scriptMessage.split('%')
        dataFile = splitMsg[0]
        unlocalized_key = splitMsg[1]
        msbt_file: MsbtFile = msbt_files[dataFile]
        found_entry = False
        for i, iLabelData in enumerate(msbt_file.labelDataArray):
            if iLabelData.labelName == labelData.labelName:
                labelData.labelIndex = iLabelData.labelIndex
                labelData.arrayIndex = iLabelData.arrayIndex
                msbt_file.labelDataArray[i] = labelData
                found_entry = True
                break
        if found_entry:
            continue
        arrayIndex = msbt_file.labelDataArray[-1].arrayIndex + 1
        labelData.labelIndex = arrayIndex
        labelData.arrayIndex = arrayIndex
        msbt_file.labelDataArray.append(labelData)
    
    for data_file in DATA_FILES:
        ifpath = os.path.join(path, "{}_{}.json".format(lang, data_file))
        with open(ifpath, "w", encoding='utf-8') as ofobj:
            msbt_file = msbt_files[data_file]
            json.dump(MsbtFile.Schema().dump(msbt_file), ofobj, indent=4)

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
    labelDatas = {}
    for ifpath in glob.glob("scripts/*.ev"):
        basename = os.path.basename(ifpath)
        basename = os.path.splitext(basename)[0]
        input_stream = FileStream(ifpath, encoding='utf-8')
        lexer = evLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = evParser(stream)
        tree = parser.prog()

        assembler = evAssembler(ifpath)
        walker = ParseTreeWalker()
        walker.walk(assembler, tree)
        unityTree = convertToUnity(ifpath, assembler.scripts, assembler.strTbl)
        scripts[basename] = unityTree
        labelDatas.update(assembler.macroAssembler.labelDatas)
    repackUnityAll("Dpr/ev_script", "bin/ev_script", scripts)
    updateLabelDatas("AssetFolder/english_Export", "english", labelDatas)

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