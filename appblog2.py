from flask import Flask,render_template,redirect,url_for,request, flash
from post import Post
from flask_mysqldb import MySQL
from PostForm import PostForm

app =Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blogdb'
# init MYSQL
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM blog')
    data = cur.fetchall()
    cur.close()
    return render_template('blog.html', blog=data)

@app.route('/posts/create')
def create():
    form = PostForm(request.form)
    return render_template('posts/create.html', form= form)

# @app.route('/posts', method=['POST'])
# def store():
#     return redirect(url_for('index'))

# @app.route('/posts/show/<id>')
# def show(id):
#     return render_template('show.html')

# @app.route('/posts/edit/<id>')
# def edit(id):
#     #Conseguir el post¡
#     return render_template('posts/edit.html')

# @app.route('/posts/update/<id>')
# def update(id):
#     return render_template('.html')

# @app.route('/posts/delete/<id>', methods=['POST', 'GET']) #¿?
# def destroy(id):
#     #Eliminar el post    
#     return redirect(url_for('index'))








app.run(debug=True,port=7000)



