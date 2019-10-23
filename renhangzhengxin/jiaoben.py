import datetime as dt
import xml.etree.ElementTree as ET
from io import StringIO
from dateutil.relativedelta import relativedelta
import os
import glob
import pandas as pd
import re

def days(str1,str2):
    date1=dt.datetime.strptime(str1[0:10],"%Y-%m-%d")
    date2=dt.datetime.strptime(str2[0:10],"%Y-%m-%d")
    num=(date1-date2).days
    return num

def months(str1,str2):
    year1=dt.datetime.strptime(str1[0:10],"%Y-%m-%d").year
    year2=dt.datetime.strptime(str2[0:10],"%Y-%m-%d").year
    month1=dt.datetime.strptime(str1[0:10],"%Y-%m-%d").month
    month2=dt.datetime.strptime(str2[0:10],"%Y-%m-%d").month
    num=(year1-year2)*12+(month1-month2)
    return num

def getHeader(root):
    name = ""
    certType = ""
    certNo = ""
    Header = root.find("Header")
    if Header is not None:
        QueryReq = Header.find("QueryReq")
        if QueryReq is not None:
            name = QueryReq.find("Name").text # 姓名
            certType = QueryReq.find("Certtype").text # 证件类型
            certNo = QueryReq.find("Certno").text  # 证件号码
    return name+","+certType+","+certNo

def getPersonalInfo(root):
    MaritalState = "" #婚姻状况
    Mobile = "" #手机号
    EduLevel = "" #最高学历
    PostAddress = "" #邮编地址
    RegisteredAddress = "" #注册地址
    industry = "" #行业
    occupation = "" #职业
    duty = "" #职务
    title = "" #职称
    PersonalInfo = root.find("PersonalInfo")
    if PersonalInfo is not None:
        Identity = PersonalInfo.find("Identity")
        if Identity is not None:
            MaritalState = Identity.find("MaritalState").text
            Mobile = Identity.find("Mobile").text
            EduLevel = Identity.find("EduLevel").text
            PostAddress = Identity.find("PostAddress").text
            RegisteredAddress = Identity.find("RegisteredAddress").text

        Professional = PersonalInfo.findall("Professional")
        if len(Professional) > 0:
            industry = Professional[0].find("Industry").text
            occupation = Professional[0].find("Occupation").text
            duty = Professional[0].find("Duty").text
            title = Professional[0].find("Title").text

    result = MaritalState + "," + Mobile + "," + EduLevel + "," + PostAddress + "," + RegisteredAddress +","
    result = result + industry +"," +occupation +"," + duty +"," + title
    return result

def getLoan(root):
    isHaveLoan = "否"
    loanNum = 0 #贷款记录
    loanCurrOverdueCount = 0 #贷款当前逾期期数
    loanTwoFour = 0 # 当前贷款连二累四次数
    loanLaterMaxOverdueMonth = 0 #贷款近二十四个月贷款最长逾期月数
    loanExceptionStatusCount = 0 #所有贷款/担保贷款五级分类出现关注以上的状态（包括“关注”，"可疑"，“次级”，“损失”）
    overdueAmount = 0 # 逾期总额
    overdue31To60Amount = 0 # 逾期31-60金额
    overdue61To90Amount = 0
    overdue91To180Amount = 0
    overdueOver180Amount = 0

    m6LoanCount = 0 # M6+以上账户数
    m6Count = 0 # M6+以上次数

    creditDetail = root.find("CreditDetail")
    if creditDetail is not None:
        loanList = creditDetail.findall("Loan")
        if len(loanList) > 0:
            isHaveLoan = "是"
            loanNum = len(loanList)
            for i in range(len(loanList)):

                CurrOverdue = loanList[i].find("CurrOverdue")
                if CurrOverdue is not None:
                    loanCurrOverdueCount = loanCurrOverdueCount + int(CurrOverdue.find("CurrOverdueCyc").text)
                    CurrOverdueAmount = CurrOverdue.find("CurrOverdueAmount")
                    if CurrOverdueAmount is not None:
                        overdueAmount = overdueAmount + int(CurrOverdueAmount.text.replace(",",""))
                    Overdue31To60Amount = CurrOverdue.find("Overdue31To60Amount")
                    if Overdue31To60Amount is not None:
                        overdue31To60Amount = overdue31To60Amount + int(Overdue31To60Amount.text.replace(",",""))
                    Overdue61To90Amount = CurrOverdue.find("Overdue61To90Amount")
                    if Overdue61To90Amount is not None:
                        overdue61To90Amount = overdue61To90Amount + int(Overdue61To90Amount.text.replace(",",""))
                    Overdue91To180Amount = CurrOverdue.find("Overdue91To180Amount")
                    if Overdue91To180Amount is not None:
                        overdue91To180Amount = overdue91To180Amount + int(Overdue91To180Amount.text.replace(",",""))
                    OverdueOver180Amount = CurrOverdue.find("OverdueOver180Amount")
                    if OverdueOver180Amount is not None:
                        overdueOver180Amount = overdueOver180Amount + int(OverdueOver180Amount.text.replace(",",""))
                Latest24MonthPaymentState = loanList[i].find("Latest24MonthPaymentState")
                if Latest24MonthPaymentState is not None:
                    Latest24State = Latest24MonthPaymentState.find("Latest24State").text
                    b = 0
                    a = 0
                    m6 = 0
                    for j in Latest24State:
                        if j.isdigit():
                            b = b + 1
                            a = a + 1
                        else:
                            if a < 2:
                                a = 0
                        if j == "7":
                            m6 = m6 + 1
                    if a >= 2 or b >= 4:
                        loanTwoFour = loanTwoFour + 1
                    Latest24State = re.sub("\D","",Latest24State) #把非字母去掉
                    for j in Latest24State:
                        if loanLaterMaxOverdueMonth < int(j):
                            loanLaterMaxOverdueMonth = int(j)
                    if m6 > 0:
                        m6LoanCount = m6LoanCount + 1
                    m6Count = m6Count + m6

                CurrAccountInfo = loanList[i].find("CurrAccountInfo")
                if CurrAccountInfo is not None:
                    Class5State = CurrAccountInfo.find("Class5State")\
                    if Class5State is not None:
                        Class5State = Class5State.text
                    else:
                        Class5State = ""
                    if Class5State == "关注" or Class5State == "可疑" or Class5State == "次级" or Class5State == "损失":
                        loanExceptionStatusCount += 1

    result = isHaveLoan + "," + str(loanNum)+',' + str(loanCurrOverdueCount) + "," + str(loanTwoFour) + "," + str(loanLaterMaxOverdueMonth) + ","
    result = result + str(loanExceptionStatusCount) + "," + str(overdueAmount) + "," + str(overdue31To60Amount) + ","
    result = result + str(overdue61To90Amount) + "," + str(overdue91To180Amount) + "," + str(overdueOver180Amount) + ","
    result = result + str(m6LoanCount) + "," + str(m6Count)
    return result

def getLoanCard(root):
    isHaveLoanCard = "否" # 是否有贷记卡
    isHaveUnCancelLoanCard = "否" # 是否有未销户贷记卡
    loanCardNum = 0  # 贷记卡记录
    loanCardCurrOverdueCount = 0  # 贷记卡当前逾期期数
    loanCardTwoFour = 0  # 记卡当前连二累四次数
    loanCardLaterMaxOverdueMonth = 0  # 贷记卡近二十四个月贷款最长逾期月数
    userLoanCardNum = 0  # 使用中的贷记卡张数

    creditDetail = root.find("CreditDetail")
    if creditDetail is not None:
        LoancardList = creditDetail.findall("Loancard")
        if len(LoancardList) > 0:
            isHaveLoanCard = "是"
            loanCardNum = len(LoancardList)
            avgRateList = []
            for i in range(len(LoancardList)):
                State = LoancardList[i].find("State")
                if State is not None:
                    State = State.text
                    if State != "销户":
                        isHaveUnCancelLoanCard = "是"
                        userLoanCardNum = userLoanCardNum + 1

                CurrOverdue = LoancardList[i].find("CurrOverdue")
                if CurrOverdue is not None:
                    loanCardCurrOverdueCount = loanCardCurrOverdueCount + int(CurrOverdue.find("CurrOverdueCyc").text)
                Latest24MonthPaymentState = LoancardList[i].find("Latest24MonthPaymentState")
                if Latest24MonthPaymentState is not None:
                    Latest24State = Latest24MonthPaymentState.find("Latest24State").text
                    b = 0
                    a = 0
                    for j in Latest24State:
                        if j.isdigit():
                            b = b + 1
                            a = a + 1
                        else:
                            if a < 2:
                                a = 0
                    if a >= 2 or b >= 4:
                        loanCardTwoFour = loanCardTwoFour + 1
                    Latest24State = re.sub("\D", "", Latest24State)  # 把非字母去掉
                    for j in Latest24State:
                        if loanCardLaterMaxOverdueMonth < int(j):
                            loanCardLaterMaxOverdueMonth = int(j)

    result = isHaveLoanCard + "," + isHaveUnCancelLoanCard + "," + str(loanCardNum) + "," + str(loanCardCurrOverdueCount) + "," + str(loanCardTwoFour) + ","
    result = result + str(loanCardLaterMaxOverdueMonth) + "," + str(userLoanCardNum)
    return result

def getGuaranteeInfo(root):
    fiveClass = "" #担保贷款五级分类
    contractMoney = 0 #担保贷款合同金额
    guananteeMoney = 0 #担保金额
    guaranteeBalance = 0 #担保本金余额
    count = 0 #担保笔数
    creditDetail = root.find("CreditDetail")
    if creditDetail is not None:
        GuaranteeInfo = creditDetail.findall("GuaranteeInfo")
        if len(GuaranteeInfo) > 0:
            for i in range(len(GuaranteeInfo)):
                GuaranteeFormat = GuaranteeInfo[i].find("GuaranteeFormat")
                if GuaranteeFormat is not None and GuaranteeFormat.text == "对外贷款担保":
                    Guarantee = GuaranteeInfo[i].findall("Guarantee")
                    if Guarantee is not None:
                        count = len(Guarantee)
                        for j in range(len(Guarantee)):
                            fiveClass = fiveClass + Guarantee[i].find("Class5State").text + "&"
                            contractMoney = contractMoney + int(Guarantee[i].find("ContractMoney").text.replace(",",""))
                            guananteeMoney = guananteeMoney + int(Guarantee[i].find("GuananteeMoney").text.replace(",",""))
                            guaranteeBalance = guaranteeBalance + int(Guarantee[i].find("GuaranteeBalance").text.replace(",",""))
    return fiveClass[0:len(fiveClass)-1] + "," + str(contractMoney) + "," + str(guananteeMoney) + "," + str(guaranteeBalance) + "," + str(count)

def getInfoSummary(root):
    houseLoanCount = "0"  # 房贷数量
    otherLoanCount = "0"  # 其他贷款数量
    firstLoanMonths = "--"  # 第一笔贷款放款距今月份
    unClearLoanCount = "0"  # 未结清贷款
    unClearSumLoanAmount = "0"  # 当前未结清贷款的原始本金金额
    unClearSumLoanBalance = "0"  # 当前未结清贷款余额
    loanLatest6MonthUsedAvgAmount = "0"  # 过去六个月未结清贷款的平均还款金额
    loanOverdueCount = "0"  # 贷款历史逾期数量
    loanOverdueMonths = "0"  # 贷款历史逾期月份数
    loanMaxOverdueAmount = "0"  # 贷款历史最高单月逾期金额
    loanMaxOverdueMonth = "0"  # 贷款历史最长逾期月数
    rateLoanCount = "--" # 未结清贷款占比
    rateLoanAmount = "--" # 未结清贷款金额占比
    rateLoanOverdue = "--" # 逾期贷款笔数占比

    loanCardCount = "0" # 贷记卡数量
    firstLoanCardMonths = "--"  # 第一张贷记卡开卡距今月份
    useLoanCardCount = "0" # 已开通的贷记卡数量
    useLoanCardCreditAmount = "0" # 已开通贷记卡额度合计
    useLoanCardMaxAmount = "0" # 已开通贷记卡最大额度
    useLoanCardMinAmount = "0" # 已开通贷记卡最小额度
    useLoanCardUsedAmount = "0" # 已开通贷记卡合计已用金额
    loanCardLatest6MonthUsedAvgAmount = "0" # 过去六个月贷记卡的平均使用金额
    loanCardOverdueCount = "0"  # 贷记卡历史逾期数量
    loanCardOverdueMonths = "0"  # 贷记卡历史逾期月份数
    loanCardMaxOverdueAmount = "0"  # 贷记卡历史最高单月逾期金额
    loanCardMaxOverdueMonth = "0"  # 贷记卡历史最长逾期月数
    rateLoanCardCount = "--"  # 未结清贷记卡占比
    rateLoanCardAmount = "--"  # 未结清贷记卡金额占比
    rateLoanCardOverdue = "--"  # 逾期贷记卡笔数占比

    standardLoancardCount = "0" # 准贷记卡数量
    firstStandardLoanCardMonths = "--" # 第一张准借记卡开卡距今月份
    useStandardLoanCardCount = "0"  # 已开通的准借记卡数量
    useStandardLoanCardCreditAmount = "0"  # 已开通准借记卡额度合计
    useStandardLoanCardMaxAmount = "0"  # 已开通准借记卡最大额度
    useStandardLoanCardMinAmount = "0"  # 已开通准借记卡最小额度
    useStandardLoanCardUsedAmount = "0"  # 已开通准借记卡合计已用金额
    standardLoanCardLatest6MonthUsedAvgAmount = "0"  # 过去六个月准借记卡的平均使用金额
    standardLoanCardOverdueCount = "0"  # 准贷记卡历史逾期数量
    standardLoanCardOverdueMonths = "0"  # 准贷记卡历史逾期月份数
    standardLoanCardMaxOverdueAmount = "0"  # 准贷记卡历史最高单月逾期金额
    standardLoanCardMaxOverdueMonth = "0"  # 准贷记卡历史最长逾期月数
    rateStandardLoanCardCount = "--"  # 未结清准贷记卡占比
    rateStandardLoanCardAmount = "--"  # 未结清准贷记卡金额占比
    rateStandardLoanCardOverdue = "--"  # 逾期准贷记卡笔数占比

    InfoSummary = root.find("InfoSummary")
    if InfoSummary is not None:
        CreditCue = InfoSummary.find("CreditCue")
        if CreditCue is not None:
            CreditSummaryCue = CreditCue.find("CreditSummaryCue")
            if CreditSummaryCue is not None:
                houseLoanCount = str(int(CreditSummaryCue.find("PerHouseLoanCount").text)+int(CreditSummaryCue.find("PerBusinessHouseLoanCount").text))
                otherLoanCount = CreditSummaryCue.find("OtherLoanCount").text
                if otherLoanCount != "0" or houseLoanCount != "0":
                    firstLoanMonths = str(months(str(dt.datetime.today()), CreditSummaryCue.find("FirstLoanOpenMonth").text.replace(".","-") + "-01"))

                loanCardCount = CreditSummaryCue.find("LoancardCount").text
                if loanCardCount != "0":
                    if len(CreditSummaryCue.find("FirstLoancardOpenMonth").text) == 7:
                        firstLoanCardMonths = str(months(str(dt.datetime.today()), CreditSummaryCue.find("FirstLoancardOpenMonth").text.replace(".","-") + "-01"))

                standardLoancardCount = CreditSummaryCue.find("StandardLoancardCount").text
                if standardLoancardCount != "0":
                    firstStandardLoanCardMonths = str(months(str(dt.datetime.today()), CreditSummaryCue.find("FirstStandardLoancardOpenMonth").text.replace(".","-") + "-01"))

        OverdueAndFellback = InfoSummary.find("OverdueAndFellback")
        if OverdueAndFellback is not None:
            OverdueSummary = OverdueAndFellback.find("OverdueSummary")
            if OverdueSummary is not None:
                LoanSum = OverdueSummary.find("LoanSum")
                if LoanSum is not None:
                    loanOverdueCount = LoanSum.find("Count").text
                    loanOverdueMonths = LoanSum.find("Months").text
                    loanMaxOverdueAmount = LoanSum.find("HighestOverdueAmountPerMon").text.replace(",","")
                    loanMaxOverdueMonth = LoanSum.find("MaxDuration").text

                LoancardSum = OverdueSummary.find("LoancardSum")
                if LoancardSum is not None:
                    loanCardOverdueCount = LoancardSum.find("Count").text
                    loanCardOverdueMonths = LoancardSum.find("Months").text
                    loanCardMaxOverdueAmount = LoancardSum.find("HighestOverdueAmountPerMon").text.replace(",","")
                    loanCardMaxOverdueMonth = LoancardSum.find("MaxDuration").text

                StandardLoancardSum = OverdueSummary.find("StandardLoancardSum")
                if StandardLoancardSum is not None:
                    standardLoanCardOverdueCount = StandardLoancardSum.find("Count").text
                    standardLoanCardOverdueMonths = StandardLoancardSum.find("Months").text
                    standardLoanCardMaxOverdueAmount = StandardLoancardSum.find("HighestOverdueAmountPerMon").text.replace(",","")
                    standardLoanCardMaxOverdueMonth = StandardLoancardSum.find("MaxDuration").text

        ShareAndDebt = InfoSummary.find("ShareAndDebt")
        if ShareAndDebt is not None:
            UnpaidLoan = ShareAndDebt.find("UnpaidLoan")
            if UnpaidLoan is not None:
                AccountCount = UnpaidLoan.find("AccountCount")
                if AccountCount is not None:
                    unClearLoanCount = AccountCount.text
                CreditLimit = UnpaidLoan.find("CreditLimit")
                if CreditLimit is not None:
                    unClearSumLoanAmount = CreditLimit.text.replace(",","")
                Balance = UnpaidLoan.find("Balance")
                if Balance is not None:
                    unClearSumLoanBalance = Balance.text.replace(",","")
                Latest6MonthUsedAvgAmount = UnpaidLoan.find("Latest6MonthUsedAvgAmount")
                if Latest6MonthUsedAvgAmount is not None:
                    loanLatest6MonthUsedAvgAmount = Latest6MonthUsedAvgAmount.text.replace(",", "")

            UndestoryLoancard = ShareAndDebt.find("UndestoryLoancard")
            if UndestoryLoancard is not None:
                AccountCount = UndestoryLoancard.find("AccountCount")
                if AccountCount is not None:
                    useLoanCardCount = AccountCount.text

                CreditLimit = UndestoryLoancard.find("CreditLimit")
                if CreditLimit is not None:
                    useLoanCardCreditAmount = CreditLimit.text.replace(",","")

                MaxCreditLimitPerOrg = UndestoryLoancard.find("MaxCreditLimitPerOrg")
                if MaxCreditLimitPerOrg is not None:
                    useLoanCardMaxAmount = MaxCreditLimitPerOrg.text.replace(",","")

                MinCreditLimitPerOrg = UndestoryLoancard.find("MinCreditLimitPerOrg")
                if MinCreditLimitPerOrg is not None:
                    useLoanCardMinAmount = MinCreditLimitPerOrg.text.replace(",","")

                UsedCreditLimit = UndestoryLoancard.find("UsedCreditLimit")
                if UsedCreditLimit is not None:
                    useLoanCardUsedAmount = UsedCreditLimit.text.replace(",","")

                Latest6MonthUsedAvgAmount = UndestoryLoancard.find("Latest6MonthUsedAvgAmount")
                if Latest6MonthUsedAvgAmount is not None:
                    loanCardLatest6MonthUsedAvgAmount = Latest6MonthUsedAvgAmount.text.replace(",","")

            UndestoryStandardLoancard = ShareAndDebt.find("UndestoryStandardLoancard")
            if UndestoryStandardLoancard is not None:
                AccountCount = UndestoryLoancard.find("AccountCount")
                if AccountCount is not None:
                    useStandardLoanCardCount = AccountCount.text

                CreditLimit = UndestoryLoancard.find("CreditLimit")
                if CreditLimit is not None:
                    useStandardLoanCardCreditAmount = CreditLimit.text.replace(",", "")

                MaxCreditLimitPerOrg = UndestoryLoancard.find("MaxCreditLimitPerOrg")
                if MaxCreditLimitPerOrg is not None:
                    useStandardLoanCardMaxAmount = MaxCreditLimitPerOrg.text.replace(",", "")

                MinCreditLimitPerOrg = UndestoryLoancard.find("MinCreditLimitPerOrg")
                if MinCreditLimitPerOrg is not None:
                    useStandardLoanCardMinAmount = MinCreditLimitPerOrg.text.replace(",", "")

                UsedCreditLimit = UndestoryLoancard.find("UsedCreditLimit")
                if UsedCreditLimit is not None:
                    useStandardLoanCardUsedAmount = UsedCreditLimit.text.replace(",", "")

                Latest6MonthUsedAvgAmount = UndestoryLoancard.find("Latest6MonthUsedAvgAmount")
                if Latest6MonthUsedAvgAmount is not None:
                    standardLoanCardLatest6MonthUsedAvgAmount = Latest6MonthUsedAvgAmount.text.replace(",", "")


    if houseLoanCount != "0" or otherLoanCount != "0":
        rateLoanCount = str(round(int(unClearLoanCount)*100/(int(houseLoanCount) + int(otherLoanCount)),2))+"%"
        rateLoanOverdue = str(round(int(loanOverdueCount)*100/(int(houseLoanCount) + int(otherLoanCount)),2))+"%"
    if unClearSumLoanAmount != "0":
        rateLoanAmount = str(round(int(unClearSumLoanBalance)*100/(int(unClearSumLoanAmount)),2))+"%"
    if loanCardCount != "0":
        rateLoanCardCount = str(round(int(useLoanCardCount)*100/(int(loanCardCount)),2))+"%"
        rateLoanCardOverdue = str(round(int(loanCardOverdueCount)*100/(int(loanCardCount)),2))+"%"
    if useLoanCardUsedAmount != "0":
        rateLoanCardAmount = str(round(int(loanCardLatest6MonthUsedAvgAmount)*100/(int(useLoanCardUsedAmount)),2))+"%"
    if standardLoancardCount != "0":
        rateStandardLoanCardCount = str(round(int(useStandardLoanCardCount)*100/(int(standardLoancardCount)),2))+"%"
        rateStandardLoanCardOverdue = str(round(int(standardLoanCardOverdueCount)*100/(int(standardLoancardCount)),2))+"%"
    if useStandardLoanCardUsedAmount != "0":
        rateStandardLoanCardAmount = str(round(int(standardLoanCardLatest6MonthUsedAvgAmount)*100/(int(useStandardLoanCardUsedAmount)),2))+"%"
    result = houseLoanCount + "," + otherLoanCount + "," + firstLoanMonths + "," + unClearLoanCount + ","
    result = result + unClearSumLoanAmount + "," + unClearSumLoanBalance + "," + loanLatest6MonthUsedAvgAmount + ","
    result = result + loanOverdueCount + "," + loanOverdueMonths + "," + loanMaxOverdueAmount + "," + loanMaxOverdueMonth + ","
    result = result + rateLoanCount + "," + rateLoanAmount + "," + rateLoanOverdue + ","

    result = result + loanCardCount + "," + firstLoanCardMonths + "," + useLoanCardCount + "," + useLoanCardCreditAmount + ","
    result = result + useLoanCardMaxAmount + "," + useLoanCardMinAmount + "," + useLoanCardUsedAmount + "," + loanCardLatest6MonthUsedAvgAmount + ","
    result = result + loanCardOverdueCount + "," + loanCardOverdueMonths + "," + loanCardMaxOverdueAmount + "," + loanCardMaxOverdueMonth + ","
    result = result + rateLoanCardCount + "," + rateLoanCardAmount + "," + rateLoanCardOverdue + ","

    result = result + standardLoancardCount + "," + firstStandardLoanCardMonths + "," + useStandardLoanCardCount + "," + useStandardLoanCardCreditAmount + ","
    result = result + useStandardLoanCardMaxAmount + "," + useStandardLoanCardMinAmount + "," + useStandardLoanCardUsedAmount + "," + standardLoanCardLatest6MonthUsedAvgAmount + ","
    result = result + standardLoanCardOverdueCount + "," + standardLoanCardOverdueMonths + "," + standardLoanCardMaxOverdueAmount + "," + standardLoanCardMaxOverdueMonth+","
    result = result + rateStandardLoanCardCount + "," + rateStandardLoanCardAmount + "," + rateStandardLoanCardOverdue
    return result

def getQueryRecord(root):
    queryCount = 0  # 查询次数
    queryOrgCount = 0  # 查询机构数
    personQueryCount = 0  # 本人查询次数
    twoYearAfterLoanQueryCount = 0  # 两年内贷后管理查询次数
    sixMonthsSpecialQueryCount = 0  # 非贷后管理、非异议核查、非公积金提取复核、非特约商户实名审查近6个月审批查询总次数
    oneMonthsPersonQueryCount = 0 # 最近1个月内的本人查询的查询次数
    sixMonthsQueryCount = 0 # 最近6个月进行审批查询次数
    sixMonthsQueryOrgCount = 0 # 最近6个月进行审批查询机构
    twelveMonthsQueryCount = 0  # 最近12个月进行审批查询次数
    twelveMonthsQueryOrgCount = 0  # 最近12个月进行审批查询机构
    oneMonthsLoanApprovalOrgCount = 0 # 过去一个月进行贷款审批查询的机构数量
    oneMonthsLoanCardApprovalOrgCount = 0 # 过去一个月进行贷记卡审批查询的机构数量
    oneMonthsLoanApprovalQueryCount = 0 # 过去一个月进行贷款审批查询次数
    oneMonthsLoanCardApprovalQueryCount = 0 # 过去一个月进行贷记卡审批查询次数
    twoYearsAfterLoanQueryCount = 0 # 过去24个月贷后检查查询次数
    twoYearsGuaranteeQueryCount = 0 # 过去24个月担保人资质查询次数
    QueryRecord = root.find("QueryRecord")
    if QueryRecord is not None:
        RecordInfo = QueryRecord.find("RecordInfo")
        if RecordInfo is not None:
            RecordDetailList = RecordInfo.findall("RecordDetail")
            if len(RecordDetailList) > 0:
                QuerierList = []
                SixQuerierList = []
                TwelveQuerierList = []
                OneLoanApprovalQuerilerList = []
                OneLoanCardApprovalQuerilerList = []
                for i in RecordDetailList:
                    QueryDate = i.find("QueryDate").text.replace("-","").replace(".","")
                    Query_time = dt.datetime.strptime(QueryDate, "%Y%m%d")
                    Querier = i.find("Querier").text
                    queryCount = queryCount + 1
                    QuerierList.append(Querier)
                    if i.find("QueryReason").text == "本人查询":
                        personQueryCount = personQueryCount + 1
                    if Query_time >= dt.datetime.strptime(str(dt.datetime.today() - relativedelta(months=+1))[0:10], "%Y-%m-%d"):
                        if i.find("QueryReason").text == "本人查询":
                            oneMonthsPersonQueryCount = oneMonthsPersonQueryCount + 1
                        if i.find("QueryReason").text == "贷款审批":
                            OneLoanApprovalQuerilerList.append(Querier)
                            oneMonthsLoanApprovalQueryCount = oneMonthsLoanApprovalQueryCount +1
                        if i.find("QueryReason").text == "贷记卡审批":
                            OneLoanCardApprovalQuerilerList.append(Querier)
                            oneMonthsLoanCardApprovalQueryCount = oneMonthsLoanCardApprovalQueryCount + 1
                    if Query_time >= dt.datetime.strptime(str(dt.datetime.today() - relativedelta(months=+6))[0:10], "%Y-%m-%d"):
                        if i.find("QueryReason").text != "贷后管理" and i.find("QueryReason").text != "异议核查" and i.find(
                                "QueryReason").text != "公积金提取复核" and i.find("QueryReason").text != "特约商户实名审查":
                            sixMonthsSpecialQueryCount = sixMonthsSpecialQueryCount + 1
                        sixMonthsQueryCount = sixMonthsQueryCount + 1
                        SixQuerierList.append(Querier)
                    if Query_time >= dt.datetime.strptime(str(dt.datetime.today() - relativedelta(months=+12))[0:10], "%Y-%m-%d"):
                        twelveMonthsQueryCount = twelveMonthsQueryCount + 1
                        TwelveQuerierList.append(Querier)
                    if Query_time >= dt.datetime.strptime(str(dt.datetime.today() - relativedelta(years=+2))[0:10], "%Y-%m-%d"):
                        if i.find("QueryReason").text == "贷后管理":
                            twoYearAfterLoanQueryCount = twoYearAfterLoanQueryCount + 1
                        if i.find("QueryReason").text == "贷后检查":
                            twoYearsAfterLoanQueryCount = twoYearsAfterLoanQueryCount + 1
                        if i.find("QueryReason").text == "担保资格审查":
                            twoYearsGuaranteeQueryCount = twoYearsGuaranteeQueryCount + 1

                queryOrgCount = len(list(set(QuerierList)))
                sixMonthsQueryOrgCount = len(list(set(SixQuerierList)))
                twelveMonthsQueryOrgCount = len(list(set(TwelveQuerierList)))
                oneMonthsLoanApprovalOrgCount = len(list(set(OneLoanApprovalQuerilerList)))
                oneMonthsLoanCardApprovalOrgCount = len(list(set(OneLoanCardApprovalQuerilerList)))
    result =  str(queryCount)+","+str(queryOrgCount)+","+str(personQueryCount)+","+str(twoYearAfterLoanQueryCount)+","+str(sixMonthsSpecialQueryCount)+","
    result = result + str(oneMonthsPersonQueryCount)+","+str(sixMonthsQueryCount)+","+str(sixMonthsQueryOrgCount)+","+str(twelveMonthsQueryCount)+","+str(twelveMonthsQueryOrgCount)+","
    result = result + str(oneMonthsLoanApprovalOrgCount)+","+str(oneMonthsLoanCardApprovalOrgCount)+","
    result = result + str(oneMonthsLoanApprovalQueryCount)+","+str(oneMonthsLoanCardApprovalQueryCount)+","
    result = result + str(twoYearsAfterLoanQueryCount)+","+str(twoYearsGuaranteeQueryCount)
    return result

if __name__ == "__main__":
    os.chdir("d:/download/")
    f =glob.glob("xml文件/*")
    result = []
    headerTitle = ["姓名","身份证类型","身份证号"]

    personTitle = ["婚姻状况","手机号","最高学历","邮编地址","注册地址","行业","职业","职务","职称"]

    loanTitle = ["是否有贷款","贷款记录","贷款当前逾期期数","当前贷款连二累四次数","贷款近二十四个月贷款最长逾期月数","所有贷款/担保贷款五级分类出现关注以上的状态"]
    loanTitle.extend(["贷款逾期总额","贷款逾期31到60总额","贷款逾期61到90总额","贷款逾期91到180总额","贷款逾期180以上总额"])
    loanTitle.extend(["M6+以上账户数","M6+以上次数"])

    loanCardTitle = ["是否有贷记卡","是否有未销户贷记卡","贷记卡记录","贷记卡当前逾期期数","贷记卡当前连二累四次数","贷记卡近二十四个月贷款最长逾期月数","使用中的贷记卡张数"]

    guaranteeTitle = ["担保贷款五级分类","担保贷款合同金额","担保金额","担保本金余额","担保笔数"]

    infoSummaryTitle = ["房贷数量", "其他贷款数量", "第一笔贷款放款距今月份","未结清贷款" ]
    infoSummaryTitle.extend(["当前未结清贷款的原始本金金额","当前未结清贷款余额","过去六个月未结清贷款的平均还款金额"])
    infoSummaryTitle.extend(["贷款历史逾期期数","贷款历史逾期月份数","贷款历史最高单月逾期金额","贷款历史最长逾期月数",])
    infoSummaryTitle.extend(["未结清贷款占比","未结清贷款金额占比","逾期贷款笔数占比"])
    infoSummaryTitle.extend(["贷记卡数量", "第一张贷记卡开卡距今月份", "已开通的贷记卡数量","已开通贷记卡额度合计"])
    infoSummaryTitle.extend(["已开通贷记卡最大额度", "已开通贷记卡最小额度", "已开通贷记卡合计已用金额","过去六个月贷记卡的平均使用金额"])
    infoSummaryTitle.extend(["贷记卡历史逾期数量", "贷记卡历史逾期月份数", "贷记卡历史最高单月逾期金额","贷记卡历史最长逾期月数"])
    infoSummaryTitle.extend(["已开通信用卡占比", "过去六个月已开通信用卡使用金额比例", "逾期信用卡笔数占比"])
    infoSummaryTitle.extend(["准贷记卡数量", "第一张准借记卡开卡距今月份", "已开通的准借记卡数量","已开通准借记卡额度合计"])
    infoSummaryTitle.extend(["已开通准借记卡最大额度", "已开通准借记卡最小额度", "已开通准借记卡合计已用金额","过去六个月准借记卡的平均使用金额"])
    infoSummaryTitle.extend(["准贷记卡历史逾期数量", "准贷记卡历史逾期月份数", "准贷记卡历史最高单月逾期金额","准贷记卡历史最长逾期月数"])
    infoSummaryTitle.extend(["已开通准借记卡占比", "过去六个月已开通准借记卡使用金额比例", "逾期准借记卡笔数占比"])

    queryRecordTitle = ["查询次数","查询机构数","本人查询次数","两年内贷后管理查询次数","非贷后管理、非异议核查、非公积金提取复核、非特约商户实名审查近6个月审批查询总次数"]
    queryRecordTitle.extend(["最近1个月内的本人查询的查询次数","最近6个月进行审批查询次数","最近6个月进行审批查询机构"])
    queryRecordTitle.extend(["最近12个月进行审批查询次数","最近12个月进行审批查询机构"])
    queryRecordTitle.extend(["过去一个月进行贷款审批查询的机构数量","过去一个月进行贷记卡审批查询的机构数量"])
    queryRecordTitle.extend(["过去一个月贷款审批查询次数","过去一个月贷记卡审批查询次数"])
    queryRecordTitle.extend(["过去24个月贷后检查查询次数","过去24个月担保人资质查询次数"])

    titleList = []
    titleList.extend(headerTitle)
    titleList.extend(personTitle)
    titleList.extend(loanTitle)
    titleList.extend(loanCardTitle)
    titleList.extend(guaranteeTitle)
    titleList.extend(infoSummaryTitle)
    titleList.extend(queryRecordTitle)
    result.append(titleList)
    for filePath in f :
        data = open(filePath,encoding='GBK')
        text = data.read()
        text = text.replace("&","*")
        utf8_parser = ET.XMLParser(encoding='utf-8')
        tree = ET.parse(StringIO(text), parser=utf8_parser)
        root=tree.getroot()
        resultList = []
        resultList.extend(getHeader(root).split(","))
        resultList.extend(getPersonalInfo(root).split(","))
        resultList.extend(getLoan(root).split(","))
        resultList.extend(getLoanCard(root).split(","))
        resultList.extend(getGuaranteeInfo(root).split(","))
        resultList.extend(getInfoSummary(root).split(","))
        resultList.extend(getQueryRecord(root).split(","))
        result.append(resultList)
    pd.DataFrame(result).to_excel(dt.datetime.now().strftime("%Y%m%d_%H%M%S")+"解析结果.xlsx")

