from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)

@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all() #Consultamos y almacenamos todas las tareas
    #Ahora en la variable todas_las_tareas se tienen almacenadas todas las tareas.
    return render_template("index.html", lista_de_tareas=todas_las_tareas)

@app.route('/crear-tarea', methods=['POST'])
def crear():
    #tarea es un objeto de la clase Tarea (una instancia de la clase)
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False) #no es necesario asignarlo manualmente
    db.session.add(tarea) #añadir el objeto de tarea a la base de datos
    db.session.commit() #Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) #Esto nos redirecciona a la función home()

@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    # Se obtiene la tarea que se busca
    tarea.hecha = not(tarea.hecha) # Guardamos en la variable booleana de la tarea, su contrario
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) # Esto nos redirecciona a la función home()

@app.route('/editar-tarea/<int:id>', methods=['GET', 'POST'])
def editar_tarea(id):
    tarea = db.session.query(Tarea).filter_by(id=id).first()
    if request.method == 'POST':
        tarea.contenido = request.form['contenido_tarea']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('editar.html', tarea=tarea)

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete() #Busca en la base de datos y borra el id con el que coincida
    db.session.commit() #Ejecuta la operación pendiente en la base de datos
    return redirect(url_for('home')) #Esto nos redirreciona a home(), eliminando la tarea de la lista


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) #Creamos el modelo de datos
    app.run(debug=True) #el debug hace que cada vez que reiniciemos el servidor o modifiquemos el código, el servidor
    #de Flask se reinicie solo