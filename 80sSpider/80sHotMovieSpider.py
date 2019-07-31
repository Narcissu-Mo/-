import urllib.request
from lxml import etree
import time
def webdeal(fullurl):
    time.sleep(3)
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib.request.Request(fullurl,headers = headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    content = etree.HTML(html)
    link_list = content.xpath('//ul[@class="me1 clearfix"]/li/a/@href')
    for link in link_list:
        fullink = 'http://www.80s.la'+link
        movedeal(fullink)
        #print(fullink)
def movedeal(fullink):
    for times in range(5,9):
        time.sleep(times)
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib.request.Request(fullink,headers = headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    content = etree.HTML(html)
    movecode_list = content.xpath('//*[@id="myform"]/ul/li[2]/span[1]/span[1]/a/@href')
    for i in movecode_list:
        movename_list = content.xpath('//*[@id="myform"]/ul/li[2]/span[1]/span[1]/a/text()')
    for x in movename_list:
        print(x)
    movelist(i,x)
def movelist(i,x):
    with open("move.txt","a")as f:
        f.write(x+"\n")
    with open("move.txt","a")as data:
        data.write(i+"\n")
        print("保存成功！")
def pagedeal(url,beginpage,endpage):
    for page in range(beginpage,endpage+1):
        print(page)
        fullurl = url + str(page)
        webdeal(fullurl)
        print("谢谢使用!")
if __name__=="__main__":
    beginpage=int(input("请问你要从第几页开始?"))
    endpage=int(input("请问要在多少页结束呢?"))
    if beginpage>endpage:
        print("暂时不支持从页数大往页数小处下载,请重新输入！")
    url = "http://www.80s.la/movie/list/----h-p"
    pagedeal(url,beginpage,endpage)
