from bottle import get, post, request, route, template, run

def what():
    return "What is this?"

@route('/')
@route('/hello')
def hello():
    name = 'Guest'
    return template('Hello {{name}}', name=name)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == "Sowmya" and password == "Sowmya":
        return "<p>Your login information was correct.</p>" + what()
    else:
        return "<p>Login failed.</p>"

run()