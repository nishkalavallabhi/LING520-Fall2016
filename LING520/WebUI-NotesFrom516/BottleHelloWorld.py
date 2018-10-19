from bottle import route, run, template

@route('/hello/<name>')
def hello(name):
    return template('Hello {{name}}!', name=name)
#This one above is used like this: localhost:8080/hello/sowmya shows you Hello Sowmya!
#@route: this is the one that "binds" the function to a url path. / or /hello/<name> in this example.

@route("/hello")
def index():
    return 'Hello world without a name!'

@route("/")
def whatever():
    return 'Hello world!'

#This run call starts the server.
run(host='localhost', port=8080)
#You can just say run() and it takes these as default settings.

'''
1. You can bind multiple paths to the same function.
2. You have to import route, run, template. It is not sufficient to just import bottle.
'''