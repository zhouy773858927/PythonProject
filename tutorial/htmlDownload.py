import requests
from bs4 import BeautifulSoup
import pymysql

class HtmlDownload(object):
    def download(self, new_url):
        res=requests.get(new_url,timeout=10)
        return res.text.encode(res.encoding).decode("utf8")

#     encode 编码  decode 解码
# res.text
#   页面的HTML代码
# res.encoding
#   页面编码格式
# res.status_code 访问状态码
#    成功 200 错误 404 重定向30x
# res.cookies
#    访问网站后设置的cookies数据

# python3 unicode

if __name__ == '__main__':
    url="http://weibo.cn/"
    # m={
    #     'ie':'utf-8',
    #     'f':'8',
    #     'rsv_bp':'0',
    #     'rsv_idx':'1',
    #     'tn':'baidu',
    #     'wd':'数据',
    #     'rsv_pq':'8add31a000035e59',
    #     'rsv_t':'4ef3p48Cw9VYXu46d2Ax1Ndafola5CPxXEz5%2F0h2spC3f%2FsH7lnLPi1c7gc',
    #     'rqlang':'cn',
    #     'rsv_enter':'1',
    #     'rsv_sug3':'9',
    #     'rsv_sug1':'7',
    #     'rsv_sug7':'100',
    # }
    requests.get(url,params={},headers={})
    # requests.post(url,data={},[headers,timeout,proxies])
    # requests.get (url,params={},[headers,timeout,proxies])
    #               url,参数表     超时时长 代理
    # proxy 代理 防止网站封IP
    # proxy={
    #     "http":"106.46.136.156",
    # }
    # [] 数组 ()元组 {}字典
    # 吃饭


# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# Accept-Encoding:gzip, deflate, sdch
# Accept-Language:zh-CN,zh;q=0.8
# Cache-Control:max-age=0
# Connection:keep-alive
# Cookie:_T_WM=2aa34efc08fc872fd6d4cc773323e7c7; ALF=1492609825; SCF=ApuEXqVZzbOAlQb-zjiTHBVhOaNDx4sXJBqTWmLe8miip1BshcFKrhgxRPc5_n7As0H4aQz9pHemX3bgTtbVwxE.; SUB=_2A251y655DeRxGeNP6VoQ8yrKzz2IHXVXNzIxrDV6PUJbktBeLWn1kW1AlfETTAhUrag7FT7suhz0AZhzZw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWOWBpuckEqiRiauoB6NUTw5JpX5o2p5NHD95QfeKzReKeXSoBpWs4Dqcjs-N9AS0MN; SUHB=0btMTtSsKELQ5x; SSOLoginState=1490017834
# DNT:1
# Host:weibo.cn
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36