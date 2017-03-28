import re
import urllib.parse

from bs4 import BeautifulSoup

url="http://baike.baidu.com/"

class HtmlParser(object):
    def parser(self, content):
        datas={}
        # datas['title']
        bs=BeautifulSoup(content,'html.parser')
        datas['title']=bs.find('h1').get_text()
        l=bs.find('div',attrs={'class':'lemma-summary'}).find_all('div',class_='para')
        datas['summary']=""
        for i in l:
            datas['summary']+=i.get_text()
        l=bs.find_all('a',href=re.compile(r'/item/.*'))
        urls=[]
        for i in l:
            urls.append(urllib.parse.urljoin(url,i['href']))
        return datas,urls


if __name__ == '__main__':
    f=open('item.html','r',encoding='utf8') #打开一个文件 open(文件名,模式,[encoding]) r(ead) w(rite),encoding编码格式
    content=f.read()
    hp=HtmlParser()
    hp.parser(content)



    # bs=BeautifulSoup(content,'html.parser') #BeautifulSoup(html代码,解析器)
    # bs.find_all()
    # bs.find_all('div',attrs={}) #find_all 返回页面中所有符合条件的
    # print(bs.select('div.header-wrapper ul.wgt-userbar')) select返回的直接就是一个数组
    # class=""  传参用class_
    # bs.select()

    # print(bs.find('h1').get_text())
    # 中国国家男子足球队
    # l=bs.find('div',attrs={'class':'lemma-summary'}).find_all('div',class_='para') #find 返回寻找到的第一个
    # for i in l:
    #     print(i.get_text()) #get_text() 把当前标签下的所有标签去掉,返回文字
    # l=bs.find_all('a',href=re.compile(r'/item/.*'))
    # print(type(l)) # <class 'bs4.element.ResultSet'> 很多个Tag的集合
    # print(type(l[0])) # <class 'bs4.element.Tag'> 对于Tag类,只要是标签中的属性,都可用字典的方式进行取值
    # img=bs.find('img')
    # print(img['src'])
    # /item/.*
    # url="http://baike.baidu.com/"
    # for i in l:
    #     print(urllib.parse.urljoin(url,i['href']))

    # urllib.parse.urljoin(url,new_url) #将new_url的格式仿照成url的格式
        # print(i)
    # /item/%E5%BC%A0%E5%AE%8F%E6%A0%B9
    # r=re.compile(r'\d+')
    # re.match(r'','')
    # re.search(r'','')
    # print(r.match("asdf151981asdsad")) #match 从头开始匹配
    # print(r.search("asdf151981asdsad"))#search 在匹配串中进行查找匹配
    # None
    # <_sre.SRE_Match object; span=(4, 10), match='151981'>








# 正则表达式
# . 任意匹配
# \ 转义  取消后面一个字符的正则意义
# ASCII
# []字符集 [a-z] [A-Z] [0-9] [A-Za-z0-9]
# 预定义的字符集
# \w 表示匹配所有单词 [A-Za-z0-9_] word
# \W 表示不匹配所有单词
# \d 表示匹配所有数字 [0-9]        digit
# \D 表示不匹配
# \s 匹配空白字符                  space
# \S
# 数量词
# * 前一个匹配>=0
# +           >=1
# ?           =0||=1
# {m,n}       >=m <=n
# {m,}        >=m
# 贪婪 一直匹配到最后没有
# 非贪婪 一直匹配到第一个匹配上的
#       []*?
# 边界匹配
# ^ match
# $
# \d+cad$
# 一串数字cad
# 逻辑
# [abc]
# a|b|c
# 分组
# \d+([a-z]{5,})(\d+)
# \num
# (?P<pname>[])
# (?P=pname)
# name:phone
# (\w+):(\d{8,11})
# >=0 <1

# . * ? [] ()
