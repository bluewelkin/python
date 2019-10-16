# -*- coding: utf-8 -*-
import web
import pymysql
render = web.template.render('templates') #定义模板
pymysql.install_as_MySQLdb()
urls = (
    '/index', 'index',  #精确匹配
    '/article', 'article',  # 精确匹配
    '/blog/\d+','blog',  #模糊匹配-带组
    '/(.*)','hello' #模糊匹配-不带组
) # 注意：url里有多个使用模糊匹配，模糊匹配范围大的要放在小的后面
app = web.application(urls, globals())

# http://127.0.0.1:8080/index?name=dgx&city=gzhou
class index:
    def GET(self):
        query = web.input()
        # return query
        return web.seeother('/article')
class blog:
    def GET(self):
        query = web.input()
        return query
    def POST(self):
        data = web.input()
        return data
class hello:
    def GET(self, name):
        return open(r'2.html').read()

class article:
    def GET(self):
        conn =pymysql.connect(host='localhost',user='root',passwd='root',db='redis',cursorclass=pymysql.cursors.DictCursor)
        cur=conn.cursor()
        cur.execute('select * from articles')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print(r)
        # return  open(r'article.html').read()

        return render.article(r)
if __name__ == "__main__":
    app.run()