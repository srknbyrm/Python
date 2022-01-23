class DBConnector:
    __instance = None

    @staticmethod
    def getInstance():
        if DBConnector.__instance == None:
            return DBConnector()
        return DBConnector.__instance

    def __init__(self):
        if DBConnector.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DBConnector.__instance = self