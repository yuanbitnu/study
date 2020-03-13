import time
import datetime

class ToolsHelp:
    @staticmethod
    def formateData(data:tuple,orclCloumnTitle:list):
        cloumnTitles = [item[0].lower() for item in orclCloumnTitle]
        formatedData = []
        for rowData in data:
            dictData = dict(zip(cloumnTitles,rowData))
            formatedData.append(dictData)
        return formatedData
    
    @staticmethod
    def getCurrentTime():
        timeStamp = int(time.time())
        timeArray = time.localtime(timeStamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


if __name__ == '__main__':
    res = ToolsHelp.getCurrentTime()
    print(res,type(res))