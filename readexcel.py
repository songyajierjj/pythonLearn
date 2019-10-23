import pandas as pd
import numpy as np
import json

filepath = "d:/download/tqgdn_20180425.xlsx"

#sheetname指定为读取几个sheet，sheet数目从0开始
#如果sheetname=[0,2]，那代表读取第0页和第2页的sheet
#skiprows=[0]代表读取跳过的行数第0行，不写代表不跳过标题
data = pd.read_excel(filepath)
print(data['zc_phone'].astype(str))
