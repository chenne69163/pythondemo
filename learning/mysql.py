# -*- coding: utf-8 -*
import pymysql

class DB():

    def __init__(self,host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        #建立连接
        self.conn = pymysql.connect(
                host=host, 
                port=port, 
                db=db, 
                user=user, 
                passwd=passwd, 
                charset=charset
            )
        #创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        #返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        #提交数据库并执行
        self.conn.commit()
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    with DB(host='192.168.130.29', port=3306, db='cntest', user='root', passwd='root') as db:
        sql = 'select * from cauth'
        try:
            db.execute(sql)

            for _ in range(db.rowcount):
                row = db.fetchone()
                print(row)
        except:
            print('sql语句错误或者代码错误')
            db.close()

