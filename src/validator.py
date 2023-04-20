from evAssembler import EvCmd, evAssembler
from ev_argtype import EvArgType
from ev_cmd import EvCmdType
from gdatamanger import GDataManager

def validate_talk_msg(cmd: EvCmd, strList: list, scripts: list):
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

def validate_talk_keywait(cmd: EvCmd, strList: list, scripts: list):
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

def validate_easy_obj_msg(cmd: EvCmd, strList: list, scripts: list):
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

def validate_add_custum_win_label(cmd: EvCmd, strList: list, scripts: list):
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

def is_valid_comparator(string):
    return string in ('GE', 'GT', 'LE', 'LT', 'EQ', 'NE')

def validate_label(cmd, argIdx, strList, scripts):
    if cmd.args[argIdx].argType != EvArgType.String:
        raise RuntimeError('Unknown label: {} passed to {} at {} at Line {}, Col {}'.format(cmd.args[argIdx].data, cmd.cmdType.name, cmd.filename, cmd.line, cmd.column))
    msgIdx = cmd.args[argIdx].data
    msg = strList[msgIdx]
    if msg not in scripts:
        raise RuntimeError('Unknown label: {} passed to {} at {} at Line {}, Col {}'.format(msg, cmd.cmdType.name, cmd.filename, cmd.line, cmd.column))

def validate_jump(cmd: EvCmd, strList: list, scripts: list):
    # Destination label should always be arg0
    validate_label(cmd, 0, strList, scripts)

def validate_obj_anime(cmd: EvCmd, strList: list, scripts: list):
    # TODO: Validate object from placedatas

    # Destination label should always be arg1
    validate_label(cmd, 1, strList, scripts)

def validate_ifflag(cmd: EvCmd, strList: list, scripts: list):
    # Destination label should always be arg1
    validate_label(cmd, 1, strList, scripts)

def validate_ifval(cmd: EvCmd, strList: list, scripts: list):
    # Comparator should always be arg1
    msgIdx = cmd.args[1].data
    msg = strList[msgIdx]

    if not is_valid_comparator(msg):
        raise RuntimeError('Bad comparator: {} passed to {} in {} at Line {}, Col {}'.format(msg, cmd.cmdType.name, cmd.filename, cmd.line, cmd.column))

    # Destination label should always be arg3
    validate_label(cmd, 3, strList, scripts)

VALIDATE_MESSAGES = {
    EvCmdType._TALKMSG : validate_talk_msg,
    EvCmdType._TALK_KEYWAIT : validate_talk_keywait,
    EvCmdType._EASY_OBJ_MSG : validate_easy_obj_msg,
    EvCmdType._ADD_CUSTUM_WIN_LABEL : validate_add_custum_win_label
}

VALIDATE_TABLE = {
    EvCmdType._IF_FLAGOFF_CALL : validate_ifflag,
    EvCmdType._IF_FLAGOFF_JUMP : validate_ifflag,
    EvCmdType._IF_FLAGON_CALL : validate_ifflag,
    EvCmdType._IF_FLAGON_JUMP : validate_ifflag,
    EvCmdType._IFVAL_CALL : validate_ifval,
    EvCmdType._IFVAL_JUMP : validate_ifval,
    EvCmdType._JUMP : validate_jump,
    EvCmdType._CALL : validate_jump,
    EvCmdType._OBJ_ANIME : validate_obj_anime
}

class Validator:
    def __init__(self, validateMessages=False):
        self.validate_table = VALIDATE_TABLE
        if validateMessages:
            self.validate_table.update(VALIDATE_MESSAGES)

    def validate_command(self, cmd, strList, scripts):
        evCmdType = cmd.cmdType
        if evCmdType in self.validate_table:
            valid_func = self.validate_table[evCmdType]
            try:
                valid_func(cmd, strList, scripts)
            except RuntimeError as exc:
                print(exc)