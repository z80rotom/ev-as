from enum import IntEnum, auto

class EvArgType(IntEnum):
    CmdType = 0
    Value = 1
    Work = 2
    Flag = 3
    SysFlag = 4
    String = 5