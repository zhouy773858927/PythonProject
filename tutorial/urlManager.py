class UrlManager(object):
    def __init__(self):#构造一个new_urls和old_urls的函数
        self.old_urls=set()# 一个集合之中不能有两个相同的元素
        self.new_urls=set()

    def add_url(self, url):#新传一个URL
        if url in self.old_urls:#判断新传URL是否在old_urls中包含
            return
        self.new_urls.add(url)

    def add_urls(self, urls):#传入多个URL
        for url in urls:#在urls中遍历url
            self.add_url(url)

    def has_url(self):#有URL
        if len(self.new_urls) == 0:#new_urls为空
            return False
        return True

    def get_newurl(self):#获取新的URL
        url=self.new_urls.pop()#pop移除并返回
        self.old_urls.add(url)
        return url


if __name__ == '__main__':
    um=UrlManager()
    urls=["http://baike.baidu.com/item/%E7%8E%B0%E8%B1%A1/2808631","http://baike.baidu.com/item/%E4%B9%89%E9%A1%B9","http://baike.baidu.com/item/%E4%B9%89%E9%A1%B9%E5%90%8D"]
    um.add_urls(urls)
    url=urls[0]
    um.add_url(url)
    for i in um.new_urls:
        print(i)
# http://baike.baidu.com/item/%E7%8E%B0%E8%B1%A1/2808631
# url=new_urls[0]
# del(new_urls[0])

# new_urls=[]
# spider.pq(1)
# new_urls=[1]
# get_newurl()
# new_urls=[] old_urls=[1]
# ....1
# add_urls(1,2,3,4,5)
# new_urls=[2,3,4,5] old_urls=[1]
# not_has_url()
# get_newurl() ->2
# new_urls=[3,4,5] old_urls=[1,2]
# .....2
# add_urls(5,6,7,8,9)
# new_urls[3,4,5,6,7,8,9] old_urls=[1,2]

# new_urls[9] old_urls=[1,2,3,4,5,6,7,8]
# not_has_url()
# get_newurl() ->9
# new_urls[] old_urls=[1,2,3,4,5,6,7,8,9]
# ......9
# add_urls(3,5,6,7)
# new_urls=[] old_urls=[1,2,3,4,5,6,7,8,9]
# not_has_url()
# 结束
