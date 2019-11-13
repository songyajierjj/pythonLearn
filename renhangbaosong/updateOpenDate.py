


if __name__ == "__main__":

    readTradeInfo = open("D:\\project\\git\\python\\renhangbaosong\\data\\开户数据.txt","r",encoding='utf-8')
    updateSql = ""
    for tradeInfo in readTradeInfo:
        dataList = tradeInfo.replace("\n","").split(",")
        updateSql = updateSql + "update rh_trade_info set date_opened ='" + dataList[8] + "',month_duration = month_duration -1 where account = '" 
        updateSql = updateSql + dataList[6] + "' and report_date in ('20191008','20191015','20191022','20191101');\n"
    # print(updateSql)

    writeTradeInfo = open("D:\\project\\git\\python\\renhangbaosong\\data\\开户update.txt","a",encoding='GBK')
    writeTradeInfo.write(updateSql)