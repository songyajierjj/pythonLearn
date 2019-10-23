import Queue

url_queue = Queue.Queue()
seen = set()

seen.insert(initial_page)
url_queue.put(initial_page)

while(True): #一直进行直到海枯石烂
    if url_queue.size()>0:
        current_url = url_queue.get()    #拿出队例中第一个的url
        store(current_url)               #把这个url代表的网页存储好
        for next_url in extract_urls(current_url): #提取把这个url里链向的url
            if next_url not in seen:      
                seen.put(next_url)
                url_queue.put(next_url)
    else:
        break

作者：谢科
链接：https://www.zhihu.com/question/20899988/answer/24923424
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。