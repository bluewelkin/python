import web
render = web.template.render('templates/')
urls = ('/(.*)', 'hello')
app= web.application(urls,globals())
class hello:
    def GET(self, name):
     
        i = web.input(times=1)
        if not name: name = 'world'
        for c in xrange(int(i.times)):
            print render.index(name)
            return 'hello ,%s' % name
if __name__ == "__main__":    
    app.run()
