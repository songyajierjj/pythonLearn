import pandas as pd
import numpy as np
import json


readData = json.loads(open("D:/清结算资料/产品/联名卡/path.txt").read())

filepath = readData['filepath']
wrongOrderPath = readData['wrongOrderPath']
resultPath = readData['resultPath']


#sheetname指定为读取几个sheet，sheet数目从0开始
#如果sheetname=[0,2]，那代表读取第0页和第2页的sheet
#skiprows=[0]代表读取跳过的行数第0行，不写代表不跳过标题

# print(type(data))

wrongOrderNoList = []
wrongSanFangList = []

dictRepaySanFang = {}
dictRepayAmount = {}
dictSanFangAmount = {}
dictPayRepay = {}
dictRepayDate = {}
dictRepayStatus = {}


payOrderNoList = []
repayOrderNoList = []
repayAmountList = []
repayDate = []
repayStatus = []

data3 = pd.read_excel(filepath,sheet_name=[3,3])
for k,v in data3.items():
    repayOrderNoList = v['还款请求号'].tolist()
    repayAmountList = v['还款金额'].tolist()
    payOrderNoList = v['借款订单号'].tolist()
    repayDate = v['还款开始时间'].tolist()
    repayStatus = v['还款状态'].tolist()


zjOrderNoList = []
zjSanFangList = []
zjAmountList = []
data6 = pd.read_excel(filepath,sheet_name=[6,6])
for k,v in data6.items():
    zjOrderNoList = v['外系统业务订单号'].tolist()
    zjSanFangList = v['订单号'].tolist()
    zjAmountList = v['记账交易金额'].tolist()

for i in range(len(zjOrderNoList)):
    dictRepaySanFang[zjOrderNoList[i]] = zjSanFangList[i]
    dictRepayAmount[zjOrderNoList[i]] = zjAmountList[i]


qfOrderNoList = []
qfSanFangList = []
qfAmountList = []
data7 = pd.read_excel(filepath,sheet_name=[7,7])
for k,v in data7.items():
    qfOrderNoList = v['外系统业务订单号'].tolist()
    qfSanFangList = v['订单号'].tolist()
    qfAmountList = v['记账交易金额'].tolist()

for i in range(len(qfOrderNoList)):
    dictRepaySanFang[qfOrderNoList[i]] = qfSanFangList[i]
    dictRepayAmount[qfOrderNoList[i]] = qfAmountList[i]


for i in range(len(repayOrderNoList)):
    if repayOrderNoList[i] in dictRepaySanFang:
        if dictRepayAmount[repayOrderNoList[i]] == repayAmountList[i]:
            if dictRepaySanFang[repayOrderNoList[i]] in dictSanFangAmount:
                continue
            else:
                dictSanFangAmount[dictRepaySanFang[repayOrderNoList[i]]] = repayAmountList[i]
        else:
            wrongOrderNoList.append(repayOrderNoList[i])
    else:
        wrongOrderNoList.append(repayOrderNoList[i])

    if payOrderNoList[i] in dictPayRepay:
        dictPayRepay[payOrderNoList[i]] = dictPayRepay[payOrderNoList[i]] +","+repayOrderNoList[i]
    else:
        dictPayRepay[payOrderNoList[i]] = repayOrderNoList[i]

    dictRepayDate[repayOrderNoList[i]] = repayDate[i]
    dictRepayStatus[repayOrderNoList[i]] = repayStatus[i]


baofuOrderList = []
baofuAmountList = []
dictBaofu = {}
data8 = pd.read_excel(filepath,sheet_name=[8,8])
for k,v in data8.items():
    baofuOrderList = v['商户订单号'].tolist()
    baofuAmountList = v['收入(元)'].tolist()

for i in range(len(baofuOrderList)):
    dictBaofu[baofuOrderList[i]] = baofuAmountList[i]

xinlianOrderList = []
xinlianAmountList = []
dictXinlian = {}
data11 = pd.read_excel(filepath,sheet_name=[11,11])
for k,v in data11.items():
    xinlianOrderList = v['商户订单号'].tolist()
    xinlianAmountList = v['订单金额'].tolist()

for i in range(len(xinlianOrderList)):
    dictXinlian[xinlianOrderList[i]] = xinlianAmountList[i]

wangjinsheOrderList = []
wangjinsheAmountList = []
dictWangjinshe = {}
data12 = pd.read_excel(filepath,sheet_name=[12,12])
for k,v in data12.items():
    wangjinsheOrderList = v['商户订单号'].tolist()
    wangjinsheAmountList = v['收入(元)'].tolist()

for i in range(len(wangjinsheOrderList)):
    dictWangjinshe[wangjinsheOrderList[i]] = wangjinsheAmountList[i]

data2 = pd.read_excel(filepath,sheet_name=[2,2])
sheet2Dict = {}
for k,v in data2.items():
    sheet2Dict = v.to_dict()

dictCountPay2 = sheet2Dict['借款订单号']
dictPayCount2 = {}
for k,v in dictCountPay2.items():
    dictPayCount2[v] = k


wrongOrderFile = open(wrongOrderPath,"a+",encoding='GBK')
for i in range(len(wrongOrderNoList)):
    wrongOrderFile.write(wrongOrderNoList[i]+"\n")
wrongOrderFile.close()

resultFile = open(resultPath,"a+",encoding='GBK')

writeData = ""
payNo = ""
sanFang = ""
count0 = ""
count1 = ""
count2 = ""
repayList = []
#充值日期
recharge = ""
#用户名称
userName = ""
#会员编号
userNo = ""
#用户手机号
userPhone = ""
#充值订单号
rechargeNo = ""
#油卡卡号
cardNo = ""
#充值金额
rechargeAmount = ""
#充值状态
rechargeStatus = ""
#用户类型
userType = ""
#资金渠道
channelType = ""
#到期时间
repayDate = ""



repayNo1 = ""
repayDate1 = ""
repayAmount1 = ""
repayStatus1 = ""
repayChannel = ""
repayNo2 = ""
repayDate2 = ""
repayAmount2 = ""
repayStatus2 = ""
repayChanne2 = ""
repayAmount = ""
interest = ""
fine = ""


for k,v in dictPayRepay.items():
    writeData = ""
    repayList = []
    sanFang = ""
    count0 = ""
    count1 = ""
    count2 = ""

    recharge = ""
    userType = ""
    userName = ""
    userNo = ""
    userPhone = ""
    channelType = ""
    payNo = ""
    rechargeNo = ""
    cardNo = ""
    rechargeAmount = ""
    rechargeStatus = ""
    repayDate = ""
    repayNo1 = ""
    repayDate1 = ""
    repayAmount1 = ""
    repayNo2 = ""
    repayDate2 = ""
    repayAmount2 = ""
    repayAmount = ""
    interest = ""
    fine = ""
    repayStatus1 = ""
    repayChannel = ""
    repayStatus2 = ""
    repayChanne2 = ""
    

    payNo = k
    if payNo in dictPayCount2:
        count2 = dictPayCount2[payNo]
        userType = sheet2Dict['用户类型'][count2]
        channelType = sheet2Dict['资金渠道'][count2]
        repayDate = sheet2Dict['到期还款日'][count2]
        recharge = sheet2Dict['创建时间'][count2]
        userName = sheet2Dict['借款人姓名'][count2]
        userNo = sheet2Dict['会员编号'][count2]
        # userPhone = sheet1Dict['注册手机号'][count1]
        rechargeNo = sheet2Dict['充值订单号'][count2]
        # cardNo = sheet1Dict['油卡卡号'][count1]
        rechargeAmount = sheet2Dict['借款金额'][count2]
        # rechargeStatus = sheet1Dict['充值状态'][count1]

        repayAmount = sheet2Dict['还款金额'][count2]
        interest = sheet2Dict['利息'][count2]
        fine = sheet2Dict['罚息'][count2]

    repayList = v.split(",")
    if len(repayList) == 2:
        if repayList[0] in dictRepaySanFang:
            repayNo1 = repayList[0]
            repayDate1 = dictRepayDate[repayNo1]
            repayAmount1 = dictRepayAmount[repayNo1]
            repayStatus1 = dictRepayStatus[repayNo1]
            sanFang = dictRepaySanFang[repayList[0]]
            if sanFang in dictBaofu:
                repayChannel = "宝付"
            elif sanFang in dictXinlian:
                repayChannel = "信联"
            elif sanFang in dictWangjinshe:
                repayChannel = "网金社"
            else:
                repayChannel = "中交"

        if repayList[1] in dictRepaySanFang:
            repayNo2 = repayList[1]
            repayDate2 = dictRepayDate[repayNo2]
            repayAmount2 = dictRepayAmount[repayNo2]
            repayStatus2 = dictRepayStatus[repayNo2]
            sanFang = dictRepaySanFang[repayList[1]]
            if sanFang in dictBaofu:
                repayChanne2 = "宝付"
            elif sanFang in dictXinlian:
                repayChanne2 = "信联"
            elif sanFang in dictWangjinshe:
                repayChanne2 = "网金社"
            else:
                repayChanne2 = "中交"
    else:
        if repayList[0] in dictRepaySanFang:
            repayNo1 = repayList[0]
            repayDate1 = dictRepayDate[repayNo1]
            repayAmount1 = dictRepayAmount[repayNo1]
            repayStatus1 = dictRepayStatus[repayNo1]
            sanFang = dictRepaySanFang[repayList[0]]
            if sanFang in dictBaofu:
                repayChannel = "小贷宝付"
            elif sanFang in dictXinlian:
                repayChannel = "小贷信联"
            elif sanFang in dictWangjinshe:
                repayChannel = "好孕邦网金社"
            else:
                repayChannel = "中交"

    writeData = ","+str(recharge) +","+str(userType)+","+str(userName)+","+str(userNo)+",,,"+str(channelType)+","+str(payNo)+","+str(rechargeNo)+",,"+str(rechargeAmount)+", ,"
    writeData = writeData + "充值成功"+", ,"+str(repayDate)+","+str(repayNo1)+","+str(repayDate1)+","+str(repayAmount1)+","+str(repayNo2)+","+str(repayDate2)+", ,"+str(repayAmount2) +","
    writeData = writeData + str(repayAmount) +","+str(interest)+","+str(fine)+", ,"+str(repayStatus1)+","+str(repayChannel)+","+str(repayStatus2)+","+str(repayChanne2)+"\n"
    resultFile.write(writeData)

resultFile.close()







