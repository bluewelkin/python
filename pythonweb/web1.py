# -*- coding: utf-8 -*-
import web
render = web.template.render('templates')

urls = (

    '/(.*)', 'index'
)

class index:
    def GET(self,name):
        # if not name:
        #     name = "world"
        # return "Hello, "+ name +"!"
        return open('1.html', 'r').read()
class image:
    def GET(self):
        return render.image()
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()