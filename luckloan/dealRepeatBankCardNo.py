import pymysql

conn = pymysql.connect(host='172.17.4.63', port=3306, user='root', passwd='root', db='qfxd_luckloan', charset='utf8')
cursor = conn.cursor()

loanDict = {}
userBankDict = {}
bankId = ""
bankIdRepeat = ""
sql = "SELECT BANK_CARD_ID from t_loan UNION SELECT BANK_CARD_ID from t_repay_order"
loan = cursor.execute(sql)
loanInfo = cursor.fetchmany(loan)
for ii in loanInfo:
    loanDict[ii[0]] = ii[0]

sql = "SELECT id,USER_ID,bank_card_no,bank_card_view from tmp_bank_card1 order by user_id "
bankCard = cursor.execute(sql)
bankCardInfo = cursor.fetchmany(bankCard)
for ii in bankCardInfo:
    if ii[0] in loanDict:
        if ii[1] in userBankDict:
            bankId = bankId + str(userBankDict[ii[1]])+","
    else:
        if ii[1] in userBankDict:
            bankId = bankId + str(ii[0])+","
        else:
            userBankDict[ii[1]] = ii[0]

print(bankId)