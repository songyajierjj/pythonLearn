#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

city = "北京,河南,河北,海南,山西"

str1 = '{"北京":"4","石家庄":"2"}'

str2 = '{"合肥":"3","郑州":"1"}'

s = json.loads(str1)

result = "false"

for key in s:
	if city.find(key) > -1:
		result = "success"
		break;
print(result)

result = "false"
s = json.loads(str2)

for key in s:
	if city.find(key) > -1:
		result = "success"
		break;
print(result)
