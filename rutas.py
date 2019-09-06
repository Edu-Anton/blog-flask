from flask import Flask ,request

#Inicio de la Aplicacion
app = Flask(__name__)
#Decorador & Ruta
@app.route('/')
def home():
    return "Esta es el Home Principal"
#Ejecutar el Servidor Default port=5000    

@app.route('/Login')
def login():
    return "Estoy en la pagina de Login"

@app.route('/Usuarios')
def usuarios():
    return "Estoy en la pagina de usuarios"

@app.route('/Productos')
def productos():
    return "Estoy en la pagina de productos"

@app.route('/blog')
def blog():
    param =request.args.get('usuario','campo usuario vacio')
    param2 =request.args.get('clave','el campo clave es  vacio')
    return "El Usuario es:{},{}" .format(param,param2)

@app.route('/portafolio')
@app.route('/portafolio/<perfil>')
@app.route('/portafolio/<perfil>/<int:edad>')
def portafolio(perfil='El Perfil defult operador',edad=0):
    return 'El portafolio de: {},{}'.format(perfil,edad)





app.run(debug=True,port=8000)    
