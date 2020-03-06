class ToolsHelp:
    @staticmethod
    def formateData(data:tuple,orclCloumnTitle:list,tableName:str = None):
        cloumnTitles = [item[0] for item in orclCloumnTitle]
        formatedData = []
        for rowData in data:
            dictData = dict(zip(cloumnTitles,rowData))
            formatedData.append(dictData)
        if tableName == None:
            return formatedData
        else:
            return {tableName:formatedData}
