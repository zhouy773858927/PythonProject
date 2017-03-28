# 1 数据库
#   1.本地数据库   sqlite3
#   2.服务器数据库 mysql
# 2 excel

import pymysql

class DataSave(object):
    def __init__(self):
        # latin-1
        # UnicodeEncodeError:
        self.conn=pymysql.connect(host='localhost',user='root',password='',db='test',charset='utf8')
        self.cur=self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def save(self, datas):
        print(datas['title'],datas['summary'])
        sql="insert into `baike` values(NULL,'%s','%s')" %(datas['title'],datas['summary'])
        self.cur.execute(sql)
        self.conn.commit()



if __name__ == '__main__':
    # conn=pymysql.connect(host='localhost',user='root',password='',db='test',charset='utf8')
    # cur=conn.cursor()
    # 插入 insert into `table_name` values(arg0[,arg1])
    # 查询 select * from `table_name`
    # sql="select `title`,`summary` from `baike`"
    # cur.execute(sql) #执行sql语句
    # l=cur.fetchall()
    # for i in l:
    #     print(i)
    # conn.commit()
    # cur.close()
    # conn.close()
    ds=DataSave()
    ds.save({'title':'title2','summary':'summary2'})