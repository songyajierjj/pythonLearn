import pandas as pd
import datetime
import os

filepath = os.getcwd()+"\\每日统计.xlsx"

wirtePath = os.getcwd()+"\\"

data = pd.read_excel(filepath,sheet_name=[0,0])
dataDict = {}
for k,v in data.items():
    dataDict = v.to_dict()

result = list()

for i in range(len(dataDict['姓名'])):
    value1 = str(dataDict['姓名'][i])
    value2 = str(dataDict['日期'][i])
    value3 = str(dataDict['上班1打卡时间'][i])
    value4 = str(dataDict['下班1打卡时间'][i])
    value4_1 = value4
    value5 = str(dataDict['班次'][i])
    if value3 == "nan" or value3 == "NaT":
        continue
    if value4 == "nan" or value4 == "NaT":
        continue
    if value4.find("次日") >= 0:
    	value4 = "23:59"
    morningHour = int(value3.split(":")[0])
    morningMinute = int(value3.split(":")[1])

    afterHour = int(value4.split(":")[0])
    afterMinute = int(value4.split(":")[1])
    
    if afterMinute > morningMinute:
        wucha = 0
    else:
        wucha = 1
    hours = afterHour - morningHour - wucha

    money = ""
    if value5 == '休息':
        if hours >= 4:
            money = 25
            if hours >= 9:
                money = 50
        else:
            continue
    else:
        if afterHour == 20 and afterMinute >= 30:
            money = 18
        elif afterHour > 20:
            money = 18
        else:
            continue
    time_xingqing = value2.replace("-","/").split(" ")

    result.append([time_xingqing[0],time_xingqing[1],value1,value3,value4_1,str(money)])


writhFile = wirtePath + "报销" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".xlsx"
pd.DataFrame(result).to_excel(writhFile)