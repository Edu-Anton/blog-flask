from flask import Flask,render_template,redirect,url_for,request, flash
from post import Post
from flask_mysqldb import MySQL
from PostForm import PostForm
import os, sys
from time import time

app =Flask(__name__)
app.secret_key = 'secret'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png'])

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
    cur.execute('SELECT * FROM blog ORDER BY _id DESC')
    data = cur.fetchall()
    cur.close()
    return render_template('blog.html', blog=data)

@app.route('/list')
def list():
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM blog ORDER BY _id DESC')
  data = cur.fetchall()
  cur.close()
  return render_template('posts/list.html', blog=data)

@app.route('/posts/create')
def create():
    form = PostForm()
    return render_template('posts/create.html', form= form)

@app.route('/posts', methods=['POST'])
def store():
  form = PostForm()
  if form.validate_on_submit():
      
    picture = request.files['url']
    nombre_con_hora = str(int(time())) + picture.filename
    print(nombre_con_hora)
    base_dir = sys.path[0]
    picture.save(os.path.join(base_dir, 'static/img/' + nombre_con_hora))

    title = request.form['title']
    description = request.form['description']
    url = 'img/' + nombre_con_hora

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO blog (title, description, url) VALUES (%s, %s, %s)', (title, description, url))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))
  else:
    return render_template('posts/create.html', form=form, todos_errores=form.errors.items())

@app.route('/posts/<id>/show')
def show(id):
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM blog WHERE _id = %s', (id))
  data = cur.fetchone()
  cur.close()
  return render_template('posts/show.html', post = data)

@app.route('/posts/edit/<id>')
def edit(id):
  form = PostForm()
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM blog WHERE _id = %s', (id))
  data = cur.fetchone()
  cur.close()
  return render_template('posts/edit.html', post=data, form=form)

# @app.route('/posts/update/<id>')
# def update(id):
#     return render_template('.html')

# @app.route('/posts/delete/<id>', methods=['POST', 'GET']) #¿?
# def destroy(id):
#     #Eliminar el post    
#     return redirect(url_for('index'))








app.run(debug=True,port=7000)



