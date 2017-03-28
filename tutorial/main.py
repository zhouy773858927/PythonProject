from tutorial.dataSave import DataSave
from tutorial.htmlDownload import HtmlDownload
from tutorial.htmlParser import HtmlParser
from tutorial.urlManager import UrlManager

import sqlite3

import pymysql

class Spider(object):
    def __init__(self):
        self.urlManager=UrlManager()
        self.htmlDownload=HtmlDownload()
        self.htmlParser=HtmlParser()
        self.dataSave=DataSave()

    def paqu(self,url):
        self.urlManager.add_url(url)
        while self.urlManager.has_url():
            new_url=self.urlManager.get_newurl()
            content=self.htmlDownload.download(new_url)
            datas,urls=self.htmlParser.parser(content)
            self.dataSave.save(datas)
            self.urlManager.add_urls(urls)


if __name__ == '__main__':
    s=Spider()
    s.paqu("http://baike.baidu.com/item/物理量")