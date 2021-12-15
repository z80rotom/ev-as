import json
from dataclasses import dataclass

@dataclass
class ArgDef:
    validArgTypes: list
    optional: bool
    description: str
    name: str

@dataclass
class FuncDef:
    validArgs: list
    description: str
    name: str

    def noReqArgs(self):
        length = 0
        for arg in self.validArgs:
            if not arg.optional:
                length += 1
        return length
    
    def maxArgs(self):
        return len(self.validArgs)

class FunctionDefinition:
    _functionDefinitions = {}

    @classmethod
    def load(cls, ifpath):
        with open(ifpath, "r") as ifobj:
            ev_scripts = json.load(ifobj)
            for evCmdTypeNo, evCmd in ev_scripts.items():
                evCmdTypeNo = int(evCmdTypeNo)
                args = evCmd["validArgs"]
                argDefs = [ArgDef(**arg) for arg in args]
                funcDef = FuncDef(validArgs=argDefs, description=evCmd["description"], name=evCmd["name"])
                cls._functionDefinitions[evCmdTypeNo] = funcDef

    @classmethod
    def getFunctionDefinition(cls, evCmdType):
        return cls._functionDefinitions[evCmdType.value]