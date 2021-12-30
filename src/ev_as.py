import os
import struct
import json
import glob
from argparse import ArgumentParser

import UnityPy

from antlr4 import *
from evAssembler import evAssembler
from evLexer import evLexer
from evParser import evParser

from ev_argtype import EvArgType
from function_definitions import FunctionDefinition

def jsonDumpUnity(tree, ofpath):
    with open(ofpath, "w") as ofobj:
        json.dump(tree, ofobj, indent=4)

def convertToUnity(ifpath, scripts, strList):
    FunctionDefinition.load("ev_scripts.json")
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

        assembler = evAssembler()
        walker = ParseTreeWalker()
        walker.walk(assembler, tree)
        unityTree = convertToUnity(ifpath, assembler.scripts, assembler.strTbl)
        scripts[basename] = unityTree
    repackUnityAll("Dpr/ev_script", "bin/ev_script", scripts)

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest='ifpath', action='store', required=True)
    parser.add_argument("-o", "--output", dest='ofpath', action='store', required=True)
    parser.add_argument("-s", "--script", dest='script', action='store', required=True)

    vargs = parser.parse_args()
    assemble(vargs.ifpath, vargs.ofpath, vargs.script)
    # assemble_all()

if __name__ == "__main__":
    main()