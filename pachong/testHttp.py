import urllib.request
import ssl
context = ssl._create_unverified_context()
# url = 'https://baike.baidu.com/item/vivo'
url ="http://9.16.15.119/shcreditunion/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(url=request,context=context)
print (response.read().decode('utf-8'))