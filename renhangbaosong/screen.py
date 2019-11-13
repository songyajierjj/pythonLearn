import os

def readAllFolder(path,accountDict):
    i = 0
    count = 0 
    for dirs in os.walk(path):
        if i == 0:
            i = i + 1
            continue
        count = count + dealTxt(dirs[0]+"\\",dirs[0]+"\\"+dirs[2][0],dirs[0]+"\\"+dirs[2][1],dirs[0]+"\\"+dirs[2][2],dirs[0]+"\\"+dirs[2][3],accountDict)
    return count

def dealTxt(path,path1,path2,path3,path4,accountDict):
    readTradeInfo = open(path4,"r",encoding='GBK')
    writeTradeInfo = open(path+"EXPORTTRADEINFONew.txt","a",encoding='GBK')
    count = 0
    i = 0
    certNoDict = {}
    for tradeInfo in readTradeInfo:
        if i == 0:
            i = i + 1
            writeTradeInfo.write(tradeInfo)
            continue
        datalist = tradeInfo.split(",")
        if datalist[6] in accountDict:
            writeTradeInfo.write(tradeInfo)
            count = count + 1
            certNoDict[datalist[2]] = datalist[2]
    readTradeInfo.close()
    writeTradeInfo.close()  
        
    readAddressInfo = open(path1,"r",encoding='GBK')
    writeAddressInfo = open(path+"EXPORTADDRESSINFONew.txt","a",encoding='GBK')
    i = 0
    for addressInfo in readAddressInfo:
        if i == 0:
            i = i + 1
            writeAddressInfo.write(addressInfo)
            continue
        datalist = addressInfo.split(",")
        if datalist[2] in certNoDict:
            writeAddressInfo.write(addressInfo)
    readAddressInfo.close()
    writeAddressInfo.close()

    readTempInfo = open(path2,"r",encoding='GBK')
    writeTempInfo = open(path+"EXPORTEMPINFONew.txt","a",encoding='GBK')
    i = 0
    for tempInfo in readTempInfo:
        if i == 0:
            i = i + 1
            writeTempInfo.write(tempInfo)
            continue
        datalist = tempInfo.split(",")
        if datalist[2] in certNoDict:
            writeTempInfo.write(tempInfo)
    readTempInfo.close()
    writeTempInfo.close()

    readPersonInfo = open(path3,"r",encoding='GBK')
    writePersonInfo = open(path+"EXPORTPERSONINFONew.txt","a",encoding='GBK')
    i = 0
    for personInfo in readPersonInfo:
        if i == 0:
            i = i + 1
            writePersonInfo.write(personInfo)
            continue
        datalist = personInfo.split(",")
        if datalist[2] in certNoDict:
            writePersonInfo.write(personInfo)
    readPersonInfo.close()
    writePersonInfo.close()

    os.remove(path1)
    os.remove(path2)
    os.remove(path3)
    os.remove(path4)
    os.rename(path+"EXPORTPERSONINFONew.txt",path+"EXPORTPERSONINFO.txt")
    os.rename(path+"EXPORTTRADEINFONew.txt",path+"EXPORTTRADEINFO.txt")
    os.rename(path+"EXPORTEMPINFONew.txt",path+"EXPORTEMPINFO.txt")
    os.rename(path+"EXPORTADDRESSINFONew.txt",path+"EXPORTADDRESSINFO.txt")
    return count

def getAccountDict(path):
    readAccountInfo = open(path,"r",encoding='UTF-8')
    accountDict = {}
    for accountInfo in readAccountInfo:
        accountDict[accountInfo.split(",")[2].replace("\n","")] = "1"
    return accountDict;


if __name__ == "__main__":
    # accountDict = getAccountDict("D:\\project\\git\\python\\renhangbaosong\\lmk.txt")
    # print("lmk="+str(len(accountDict)))
    # count = readAllFolder("D:\\project\\git\\python\\renhangbaosong\\lmkexport\\",accountDict)
    # print("lmk="+str(count))

    # accountDict = getAccountDict("D:\\project\\git\\python\\renhangbaosong\\cyd.txt")
    # print("cyd="+str(len(accountDict)))
    # count = readAllFolder("D:\\project\\git\\python\\renhangbaosong\\cydexport\\",accountDict)
    # print("cyd="+str(count))

    # accountDict = getAccountDict("D:\\project\\git\\python\\renhangbaosong\\data\\all.txt")
    # print("all="+str(len(accountDict)))
    # count = readAllFolder("D:\\project\\git\\python\\renhangbaosong\\data\\export\\",accountDict)
    # print("count="+str(count))

    # li = ["ety", "xyz", "hello", "world"]
    # s = ",".join(li)
    # print(s)

    readTradeInfo = open("D:\\project\\git\\python\\renhangbaosong\\data\\开户数据.txt","r",encoding='utf-8')
    # updateSql = "update from rh_trade_info set billing_date = '20190921',recent_pay_date='20190921' where report_date = '20190922' and account in ("
    updateSql = ""
    for tradeInfo in readTradeInfo:
    	updateSql = updateSql + "'" + tradeInfo.split(",")[2].replace("\n","") + "',"
    print(updateSql)

    # print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


