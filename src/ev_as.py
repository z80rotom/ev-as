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
    def getScenarioMsgList(cls, messagepath):
        if cls.DISABLED_MSGS:
            return None
        if not cls.SCENARIO_MSGS:
            scenario1 = []
            scenario2 = []
            scenario3 = []
            try:
                with open(os.path.join(messagepath, "english_dp_scenario1.json"), "r", encoding='utf-8') as ifobj:
                    data = json.load(ifobj)
                    for entry in data["labelDataArray"]:
                        labelName = entry["labelName"]
                        scenario1.append(labelName)
                with open(os.path.join(messagepath, "english_dp_scenario2.json"), "r", encoding='utf-8') as ifobj:
                    data = json.load(ifobj)
                    for entry in data["labelDataArray"]:
                        labelName = entry["labelName"]
                        scenario2.append(labelName)
                with open(os.path.join(messagepath, "english_dp_scenario3.json"), "r", encoding='utf-8') as ifobj:
                    data = json.load(ifobj)
                    for entry in data["labelDataArray"]:
                        labelName = entry["labelName"]
                        scenario3.append(labelName)
            except FileNotFoundError as exc:
                cls.DISABLED_MSGS = True
                print("Warning: english files not found. Message validation will not be enabled: {}".format(exc))
                return None
            cls.SCENARIO_MSGS = {
                'dp_scenario1' : scenario1,
                'dp_scenario2' : scenario2,
                'dp_scenario3' : scenario3
            }
        return cls.SCENARIO_MSGS    

def jsonDumpUnity(tree, ofpath):
    with open(ofpath, "w") as ofobj:
        json.dump(tree, ofobj, indent=4)

def validate_talk_msg(cmd: EvCmd, strList, messagepath):
    scenarioMsgList = GDataManager.getScenarioMsgList(messagepath=messagepath)
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

def validate_talk_keywait(cmd: EvCmd, strList: list, messagepath):
    scenarioMsgList = GDataManager.getScenarioMsgList(messagepath=messagepath)
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

def validate_easy_obj_msg(cmd: EvCmd, strList: list, messagepath):
    scenarioMsgList = GDataManager.getScenarioMsgList(messagepath=messagepath)
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
}

def convertToUnity(ifpath, scripts, strList, messagepath):
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

            if messagepath and evCmdType in VALIDATE_TABLE:
                valid_func = VALIDATE_TABLE[evCmdType]
                try:
                    valid_func(cmd, strList, messagepath)
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

def assemble(ifpath, ofpath, script, messagepath):
    input_stream = FileStream(ifpath)
    lexer = evLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = evParser(stream)
    tree = parser.prog()

    assembler = evAssembler()
    walker = ParseTreeWalker()
    walker.walk(assembler, tree)
    unityTree = convertToUnity(ifpath, assembler.scripts, assembler.strTbl, messagepath)
    repackUnity(ofpath, script, unityTree)

def repackUnityAll(ofpath, scripts):
    with open(ofpath, "rb") as ifobj:
            bundle = UnityPy.load(ofpath)

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

def assemble_all(idfpath, ofpath, messagepath):
    scripts = {}
    for ifpath in glob.glob(os.path.join(idfpath, "*.ev")):
        basename = os.path.basename(ifpath)
        basename = os.path.splitext(basename)[0]
        input_stream = FileStream(ifpath)
        lexer = evLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = evParser(stream)
        tree = parser.prog()

        assembler = evAssembler()
        walker = ParseTreeWalker()
        walker.walk(assembler, tree)
        unityTree = convertToUnity(ifpath, assembler.scripts, assembler.strTbl, messagepath)
        scripts[basename] = unityTree
    repackUnityAll(ofpath, scripts)

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest='ifpath', action='store', default='scripts')
    parser.add_argument("-o", "--output", dest='ofpath', action='store', default='bin/ev_script')
    parser.add_argument("-s", "--script", dest='script', action='store')
    parser.add_argument("-v", "--validate", dest='validate', action='store_true')
    parser.add_argument("-nv", "--no-validate", dest='validate', action='store_false')
    parser.set_defaults(validate=True)
    parser.add_argument("-m", "--message", dest='message', action='store', default='AssetFolder/english_Export')

    vargs = parser.parse_args()
    messagePath = vargs.message if vargs.validate else None
    
    if os.path.isfile(vargs.ifpath):
        script = vargs.script if vargs.script else os.path.basename(os.path.basename(vargs.ifpath))
        assemble(vargs.ifpath, vargs.ofpath, script, messagePath)
    else:
        assemble_all(vargs.ifpath, vargs.ofpath, messagePath)

if __name__ == "__main__":
    main()