from poplib import POP3
import re,email,email.header
from p_email import mypass
def jie(msg_src,names):
    ms = email.message_from_bytes(msg_src)
    result = {}
    fro name in names:
        content = msg.get(name)
        info = email.header.decode_header(content)
    if info[0][1]:
        if info[0][1].find('unknown-') == -1:
            result[name] = info[0][0].decode(info[0][1])
        else:
            try:
                result[name] = info[0][0],decode('gbk')
            except:
                result[name] = info[0][0].decode('utf-8')
    else:
        result[name] = info[0][0]
    return result;
if __name__ == "__main__":
    pp = POP3("pop.sina.com")
    pp.user('sfs@sina.com')
    pp.pass_ (mypass)
    total,totalnum = pp.stat()
    print(total,totalnum)
    for i in range(total-2,total):
        hinfo,msgs,octee = pp.top(i+1,0)
        b = b''
        for msg in msgs:
            b += msg + b'\n'
        items = jie(b,['subject','from'])
        print(items['subject'],'\nFrom:',item['form'])
        print()
    pp.close()
