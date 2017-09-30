from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/oldhello')
def oldhello():
    print(url_for('static', filename='site.css'))

    return 'hello world!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # example of url_for to generate urls for route methods
    print(url_for('hello'))

    return 'Post %d' % post_id

# example of VERBS
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do the login'
    else:
        return 'show the login form'
# template example
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/logging')
def logging():
    app.logger.debug('debug message')
    app.logger.warning('A warning occured (%d apples)', 42)
    app.logger.error('This is an error damnit!')
    return 'check the console'

@app.errorhandler(404)
def not_found(error):
    return 'shit not found!'



# set this envvar
# export FLASK_APP=main.py
# enables reload on save and debug info
# export FLASK_DEBUG=1
