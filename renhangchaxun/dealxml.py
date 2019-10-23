
import sys
import glob
import os
import xml.etree.ElementTree as ET
from io import StringIO

writePath = "C:/python/result.txt"
writeFile = open(writePath,"a+",encoding='GBK')
writeData = ""
def xmlFilePath(path):
    if os.path.exists(path):
        f = glob.glob(path+"\\*.txt")
        for filePath in f:
            data = open(filePath,encoding='GBK')
            text = data.read()
            utf8_parser = ET.XMLParser(encoding='utf-8')
            tree = ET.parse(StringIO(text), parser=utf8_parser)
            root=tree.getroot()
            print(type(root))
            for child in root:
                if child.tag == "Header":
                    for child1 in child:
                        if child1.tag == "MessageHeader":
                            writeData.append(child1.find("ReportSN").text+"")



path = "D:\\千方\\风控平台\\人行征信\\1600个xml人行征信报告\\好客户\\2018-08-20-5"
xmlFilePath(path)
