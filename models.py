import db
from sqlalchemy import Column, Integer, String, Boolean

class Tarea(db.Base):
    __tablename__="tarea"
    id = Column(Integer, primary_key=True) #Identificador unico de cada tarea
    #(no puede haber dos tareas con el mismo id, por eso es primary key)
    contenido = Column(String(200), nullable=False) #Contenido de la tarea, un texto de máximo 200 caracteres
    hecha = Column(Boolean) #Booleano indica si una tarea ha sido hecha o no

    def __init__(self, contenido, hecha):
        #recordemos que el id no es necesario crearlo manualmente, lo añade la base de datos automáticamente
        self.contenido = contenido
        self.hecha = hecha

    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)