from copy import copy
import os
import struct
import json
import glob
from argparse import ArgumentParser

import UnityPy
from gdatamanger import DATA_FILES
import marshmallow

from antlr4 import *
from evAssembler import EvCmd, evAssembler
from evLexer import evLexer
from evParser import evParser

from ev_argtype import EvArgType
from ev_cmd import EvCmdType
from function_definitions import FunctionDefinition
from msbt import MsbtFile
from validator import Validator

def jsonDumpUnity(tree, ofpath):
    with open(ofpath, "w") as ofobj:
        json.dump(tree, ofobj, indent=4)

def convertToUnity(ifpath, scripts, strList, linkerLabels):
    # FunctionDefinition.load("ev_scripts.json")
    tree = {}
    treeScripts = []

    validator = Validator()

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

            validator.validate_command(cmd, strList, linkerLabels)

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
            json.dump(MsbtFile.Schema().dump(msbt_file), ofobj, indent=4, ensure_ascii=False)

def assemble(ifpath, ofpath, script):
    input_stream = FileStream(ifpath)
    lexer = evLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = evParser(stream)
    tree = parser.prog()

    assembler = evAssembler()
    walker = ParseTreeWalker()
    walker.walk(assembler, tree)
    unityTree = convertToUnity(assembler.scripts, assembler.strTbl, assembler.scripts.keys())
    repackUnity(ofpath, script, unityTree)

def repackUnityAll(ifpath, ofpath, scripts):
    os.makedirs("bin", exist_ok=True)
    
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

def load_definitions():
    ifpath = "scripts/global_defines.ev"
    input_stream = FileStream(ifpath, encoding='utf-8')
    lexer = evLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = evParser(stream)
    tree = parser.prog()

    assembler = evAssembler(ifpath)
    walker = ParseTreeWalker()
    walker.walk(assembler, tree)

    return assembler

def loadCoreLabels(ifpath, ignoreNames):
    linkerLabels = []
    with open(ifpath, "rb") as ifobj:
        bundle = UnityPy.load(ifpath)

        for obj in bundle.objects:
            if obj.type.name != "MonoBehaviour":
                continue
            data = obj.read()
            if data.name in ignoreNames:
                continue
            if obj.serialized_type.nodes:
                tree = obj.read_typetree()
                if "Scripts" not in tree:
                    continue
                scripts = tree["Scripts"]
                for script in scripts:
                    label = script["Label"]
                    linkerLabels.append(label)

    return linkerLabels

def assemble_all():
    scripts = {}
    labelDatas = {}
    flags = {}
    works = {}
    sysflags = {}
    if os.path.exists("scripts/global_defines.ev"):
        assembler = load_definitions()
        flags = assembler.flags
        works = assembler.works
        sysflags = assembler.sysflags
    
    commands = {}
    if os.path.exists("commands.json"):
        print("Loading external commands reference from commands.json")
        with open("commands.json", "r") as ofobj:
            data = json.load(ofobj)
            for entry in data:
                try:
                    commands[entry["Name"]] = entry["Id"]
                except KeyError:
                    print("Unable to load commands.json, missing either Id or Name key. Defaulting to known commands")

    linkerLabels = []
    toConvertList = []
    ignoreList = []
    for ifpath in glob.glob("scripts/*.ev"):
        # Special file with special behaviour
        basename = os.path.basename(ifpath)
        basename = os.path.splitext(basename)[0]
        if basename == "global_defines.ev":
            continue
        input_stream = FileStream(ifpath, encoding='utf-8')
        lexer = evLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = evParser(stream)
        tree = parser.prog()

        assembler = evAssembler(ifpath, commands=copy(commands), flags=copy(flags), works=copy(works), sysflags=copy(sysflags))
        walker = ParseTreeWalker()
        walker.walk(assembler, tree)
        toConvertList.append((ifpath, assembler.scripts, assembler.strTbl, basename))
        linkerLabels.extend(assembler.scripts.keys())
        labelDatas.update(assembler.macroAssembler.labelDatas)
        ignoreList.append(basename)
    linkerLabels.extend(loadCoreLabels("Dpr/ev_script", ignoreList))
    for toConvert in toConvertList:
        unityTree = convertToUnity(toConvert[0], toConvert[1], toConvert[2], linkerLabels)
        scripts[toConvert[3]] = unityTree
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