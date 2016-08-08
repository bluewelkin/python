import web
urls= ('/(.*)','index')
 
app= web.application(urls,globals())
class index:   
    def GET(self, name):
        if not name:
            name = 'world'
        web.header('Content-Type','text/html; charset=UTF-8')
        return 'python web dgx'
 
if __name__ == "__main__":
    app.run()