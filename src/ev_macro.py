from enum import IntEnum, auto

class EvMacroType(IntEnum):
    Invalid = -1
    _MACRO_TALKMSG = auto()
    _MACRO_TALK_KEYWAIT = auto()
    _MACRO_EASY_OBJ_MSG = auto()
    _MACRO_ADD_CUSTUM_WIN_LABEL = auto()

    def isValid(self):
        return self != EvMacroType.Invalid