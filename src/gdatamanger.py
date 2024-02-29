import json

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