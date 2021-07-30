from bottle import Bottle, route, run, template, request, redirect
import Algoritm
import subprocess

app = Bottle()

@app.route('/')
#ruta pentru pagina de home din care utilizatorul poate da Start
def index():
    return template('index.html')

project_process = None

#ruta accesata la apasarea butonului start
@app.route('/proiect', method="POST")
def run_proiect():
    global project_process
    #se creeaza un nou subproces care are ca scop rularea algoritmului de generare a numarului aleator
    project_process = subprocess.Popen(["python", "proiect.py"])
    redirect('/')

#ruta accesata odata ce numerele aleatoare au fost generate si rezultatul a fost trimis catre utilizator
@app.route('/termina_proiect', method="POST")
def terminate_project():
    global project_process
    if(project_process != None):
        project_process.terminate()
        project_process = None
    redirect('/')
run(app, host='0.0.0.0', port='8080', debug=True)
