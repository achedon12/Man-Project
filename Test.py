def test_creation_object(settings: list):
    for setting in settings:
        settingType = type(setting)
        if settingType == int:
            if setting is None:
                return True
        elif settingType == str:
            if setting is None or setting == "":
                return True
        elif settingType == list:
            if setting is None or len(setting) == 0:
                return True
            for element in setting:
                if element is None:
                    return True
        elif settingType == dict:
            instance = setting["type"]
            values = setting["values"]
            if not isinstance(values, list) or values is None or len(values) == 0:
                return True
            for value in values:
                if not isinstance(value, instance):
                    return True
        else:
            return False
