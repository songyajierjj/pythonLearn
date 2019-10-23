from urllib.request import urlopen
from urllib.parse import urlencode
import re
wd = '12305'
wd = urlencode({'wd':wd})
url = 'http://www.baidu.com/s?'+wd
page = urlopen(url).read()
content = (page.decode('utf-8')).replace("\n","").replace("\t","")
print("1231")
print(content)
title = re.findall(r'<h3 class="t",*?h3',content)
title = [item[item.find('href=')+6:item.find('target=')] for item in title] #正则表达式处理
title = [item.replace(' ','').replace('"','') for item in title] #正则表达式处理
for item in title:
    print(item)
