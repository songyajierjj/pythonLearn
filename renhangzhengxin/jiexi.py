# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:45:34 2018

@author: admi
"""
import datetime as dt
"""
姓名
"""
def function_name(root):
    return root.find("Header").find("QueryReq").find("Name").text



"""
证件类型
"""
def function_Certtype(root):
    return root.find("Header").find("QueryReq").find("Certtype").text

"""
证件号码
"""
def function_Certno(root):
    return root.find("Header").find("QueryReq").find("Certno").text


    
"""
贷款记录
"""
def functon_LoanNum(root):
    LoanNum = 0
    try:
        root.find("CreditDetail").findall("Loan")
    except Exception:
        LoanNum = 0
    else:
        x = root.find("CreditDetail").findall("Loan")
        for i in x:
            LoanNum=LoanNum+1
    return LoanNum

"""
贷记卡记录
"""
def functon_LoancardNum(root):
    Loancard = 0
    try:
        root.find("CreditDetail").findall("Loancard")
    except Exception:
        Loancard = 0
    else:
        x = root.find("CreditDetail").findall("Loancard")
        for i in x:
            Loancard=Loancard+1
    return Loancard
"""
当前贷款是否逾期
"""
def functon_Loanisyuqi(root):
    yq = 0
    try:
        root.find("CreditDetail").findall("Loan")
    except Exception:
        yq = 0
    else:
        x = root.find("CreditDetail").findall("Loan")
        for i in x:
            try:
                a = i.find("Latest24MonthPaymentState").find("Latest24State").text
                if(a[len(a)-1].isdigit()):
                    yq = yq +1
            except Exception:
                yq = yq
            else:
                if((i.find("State").text=="逾期")
                |(i.find("State").text=="止付")
                |(i.find("State").text=="呆账")
                |(i.find("State").text=="冻结")
                |(i.find("State").text=="担保人代偿")
                |(i.find("State").text=="以资抵债")):
                    yq = yq +1
    if(yq>0):
        return "逾期"
    else:
        return "正常"

"""
当前贷记卡是否逾期
"""
def functon_Loancardisyuqi(root):
    yq = 0
    try:
        root.find("CreditDetail").findall("Loancard")
    except Exception:
        yq = 0
    else:
        x = root.find("CreditDetail").findall("Loancard")
        for i in x:
            try:
                a = i.find("Latest24MonthPaymentState").find("Latest24State").text
                if(a[len(a)-1].isdigit()):
                    yq = yq +1
            except Exception:
                yq = yq
            else:
                if((i.find("State").text=="逾期")
                |(i.find("State").text=="止付")
                |(i.find("State").text=="呆账")
                |(i.find("State").text=="冻结")
                |(i.find("State").text=="担保人代偿")
                |(i.find("State").text=="以资抵债")):
                    yq = yq +1
    if(yq>0):
        return "逾期"
    else:
        return "正常"
"""
当前贷款连二累四次数
"""
def functon_Loanl2l4(root):
    ll = 0
    try:
        root.find("CreditDetail").findall("Loan")
    except Exception:
        ll = 0
    else:
        x = root.find("CreditDetail").findall("Loan")
        for i in x:
            try:
                a = i.find("Latest24MonthPaymentState").find("Latest24State").text 
                b=0
                for j in a:
                    if(j.isdigit()):
                        b=b+1
                if((a.find('3')!=-1)|(b>=4)):
                    ll=ll+1
            except Exception:
                ll = ll
            else:
                ll = ll            
    return ll
"""
当前贷记卡连二累四次数
"""
def functon_Loancardl2l4(root):
    ll = 0
    try:
        root.find("CreditDetail").findall("Loancard")
    except Exception:
        ll = 0
    else:
        x = root.find("CreditDetail").findall("Loancard")
        for i in x:
            try:
                a = i.find("Latest24MonthPaymentState").find("Latest24State").text 
                b=0
                for j in a:
                    if(j.isdigit()):
                        b=b+1
                if((a.find('3')!=-1)|(b>=4)):
                    ll=ll+1
            except Exception:
                ll = ll
            else:
                ll = ll           
    return ll

#未结清贷款
def functon_UnpaidLoan(root):
    try:
        root.find("InfoSummary").find("ShareAndDebt")
    except Exception:
        UnpaidLoan = 0
    else:
        s = root.find("InfoSummary").find("ShareAndDebt")
        UnpaidLoan = 0
        try:
            s.find("UnpaidLoan").find("AccountCount")
        except Exception:
            UnpaidLoan = UnpaidLoan + 0
        else:
            num = s.find("UnpaidLoan").find("AccountCount").text
            UnpaidLoan = UnpaidLoan + int(num)
    return UnpaidLoan


#逾期(透支)信息汇总-贷款
def funs_LoanSum(root):
    LoanSum = list()
    try:
        root.find("InfoSummary").find("OverdueAndFellback")
    except Exception as e:
        LoanSum.append(0)
        LoanSum.append(0)
        LoanSum.append(0)
        LoanSum.append(0)
    else:
        o = root.find("InfoSummary").find("OverdueAndFellback")
        try:
            o.find("OverdueSummary").find("LoanSum")
        except Exception as e:
            LoanSum.append(0)
            LoanSum.append(0)
            LoanSum.append(0)
            LoanSum.append(0)
        else:
            LoanSum.append(int(o.find("OverdueSummary").find("LoanSum").find("Count").text))
            try:
                o.find("OverdueSummary").find("LoanSum").find("Months").text
            except Exception as e:
                LoanSum.append(0)
            else:
                LoanSum.append(int(o.find("OverdueSummary").find("LoanSum").find("Months").text))
            try:
                o.find("OverdueSummary").find("LoanSum").find("HighestOverdueAmountPerMon").text
            except Exception as e:
                LoanSum.append(0)
            else:
                LoanSum.append(int(o.find("OverdueSummary").find("LoanSum").find("HighestOverdueAmountPerMon").text))
            try:
                o.find("OverdueSummary").find("LoanSum").find("MaxDuration").text
            except Exception as e:
                LoanSum.append(0)
            else:
                LoanSum.append(int(o.find("OverdueSummary").find("LoanSum").find("MaxDuration").text))
    return LoanSum

#逾期(透支)信息汇总-贷记卡
def funs_LoancardSum(root):
    LoancardSum = list()       
    try:
        root.find("InfoSummary").find("OverdueAndFellback")
    except Exception as e:
        LoancardSum.append(0)
        LoancardSum.append(0)
        LoancardSum.append(0)
        LoancardSum.append(0)
    else:
        o = root.find("InfoSummary").find("OverdueAndFellback")
        try:
            o.find("OverdueSummary").find("LoancardSum")
        except Exception as e:
            LoancardSum.append(0)
            LoancardSum.append(0)
            LoancardSum.append(0)
            LoancardSum.append(0)
        else:
            LoancardSum.append(int(o.find("OverdueSummary").find("LoancardSum").find("Count").text))
            try:
                o.find("OverdueSummary").find("LoancardSum").find("Months").text
            except Exception as e:
                LoancardSum.append(0)
            else:
                LoancardSum.append(int(o.find("OverdueSummary").find("LoancardSum").find("Months").text))
            try:
                o.find("OverdueSummary").find("LoancardSum").find("HighestOverdueAmountPerMon").text
            except Exception as e:
                LoancardSum.append(0)
            else:
                LoancardSum.append(int(o.find("OverdueSummary").find("LoancardSum").find("HighestOverdueAmountPerMon").text))
            try:
                o.find("OverdueSummary").find("LoancardSum").find("MaxDuration").text
            except Exception as e:
                LoancardSum.append(0)
            else:
                LoancardSum.append(int(o.find("OverdueSummary").find("LoancardSum").find("MaxDuration").text))   
    return LoancardSum

"""
=====多头查询
"""
#查询次数
def function_RecordCount(root,tar_time):
    try:
        root.find("QueryRecord").find("RecordInfo").findall("RecordDetail")
    except Exception as e:
        RecordCount = 0
    else:
        q = root.find("QueryRecord").find("RecordInfo").findall("RecordDetail")
        RecordCount = 0    
        for i in q:
            QueryDate = i.find("QueryDate").text
            Query_time = dt.datetime.strptime(QueryDate, "%Y-%m-%d")
            if Query_time >= (dt.datetime.today() - dt.timedelta(days=tar_time)):
                RecordCount = RecordCount + 1
            else:
                RecordCount = RecordCount + 0
    return RecordCount
#查询机构数
def function_OrdCount(root,tar_time):
    try:
        root.find("QueryRecord").find("RecordInfo").findall("RecordDetail")
    except Exception as e:
        OrgCount = 0
    else:
        q = root.find("QueryRecord").find("RecordInfo").findall("RecordDetail")
        OrgCount = 0  
        Org_list = list()
        for i in q:
            Querier = i.find("Querier").text
            QueryDate = i.find("QueryDate").text
            Query_time = dt.datetime.strptime(QueryDate, "%Y-%m-%d")
            if (Query_time >= (dt.datetime.today() - dt.timedelta(days=tar_time)))&(Querier not in Org_list):
                OrgCount = OrgCount + 1
            else:
                OrgCount = OrgCount + 0
            Org_list.append(Querier)
    return OrgCount

#本人查询次数
def fun_LatestMonthQueryCount(root):
    try:
        root.find("QueryRecord").find("RecordSummary").findall("LatestMonthQueryrecordSum")
    except Exception as e:
        LatestMonthQueryCount = 0
    else:
        r = root.find("QueryRecord").find("RecordSummary").findall("LatestMonthQueryrecordSum")
        for i in r:
            if i.find("QueryReason").text=="本人查询":
                LatestMonthQueryCount = int(i.find("Sum").text)
    return LatestMonthQueryCount            
#两年内贷后管理查询次数	
def fun_TwoyearQueryCount(root):
    try:
        root.find("QueryRecord").find("RecordSummary").findall("TwoyearQueryrecordSum")
    except Exception as e:
        TwoyearQueryCount = 0
    else:
        r = root.find("QueryRecord").find("RecordSummary").findall("TwoyearQueryrecordSum")
        for i in r:
            if i.find("QueryReason").text=="贷后管理":
                TwoyearQueryCount = int(i.find("Sum").text)
    return TwoyearQueryCount

"""
单行最高授信额度
"""
def functon_MaxCreditLimit(root):
    Loancard = 0
    try:
        Loancard = root.find("InfoSummary").find("ShareAndDebt").find("UndestoryLoancard").find("maxCreditLimitPerOrg")
    except Exception:
        Loancard = 0
    return Loancard