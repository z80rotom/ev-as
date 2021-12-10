import os
import struct
import json
from argparse import ArgumentParser

import UnityPy

from antlr4 import *
from evAssembler import evAssembler
from evLexer import evLexer
from evParser import evParser

from ev_argtype import EvArgType

def jsonDumpUnity(tree, ofpath):
    with open(ofpath, "w") as ofobj:
        json.dump(tree, ofobj, indent=4)

def convertToUnity(scripts, strList):
    tree = {}
    treeScripts = []

    for label, script in scripts.items():
        scriptCommands = []
        for cmd in script:
            scriptArgs = [
                {
                    "argType" : EvArgType.CmdType,
                    "data" : cmd.cmdType.value
                }
            ]

            for arg in cmd.args:
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

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest='ifpath', action='store', required=True)
    parser.add_argument("-o", "--output", dest='ofpath', action='store', required=True)
    parser.add_argument("-s", "--script", dest='script', action='store', required=True)

    vargs = parser.parse_args()
    assemble(vargs.ifpath, vargs.ofpath, vargs.script)

if __name__ == "__main__":
    main()