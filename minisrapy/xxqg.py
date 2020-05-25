import requests
import json
import xlwt

dataList = []
with open('context.txt', mode='r', encoding='utf-8') as file_stream:
    ret = json.load(file_stream)
    dataList = ret['data']['list']

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('mySheet')
worksheet.write(0,0,label = '姓名')
worksheet.write(0,1,label = '所属支部')
worksheet.write(0,2,label = '所选时段分数')
worksheet.write(0,3,label = '月累积分数')
worksheet.write(0,4,label = '总积分')

for index in range(len(dataList)):
    item = dataList[index]
    worksheet.write(index + 1,0,label = item['ddName'])
    worksheet.write(index + 1,1,label = item['deptName'])
    worksheet.write(index + 1,2,label = item['rangeScore'])
    worksheet.write(index + 1,3,label = item['scoreMonth'])
    worksheet.write(index + 1,4,label = item['totalScore'])
workbook.save('excel.xls')


