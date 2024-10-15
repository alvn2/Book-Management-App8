from server import app

@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/register')
def register():
    return '<h1>Register Page</h1>'

@app.route('/login')
def login():
    return '<h1>Login Page</h1>'
