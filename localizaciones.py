from db import db

class datos(db.Model):
    
    #Nombre de tabla 
    __tablename__="datos"
    
    #Conjunto de atributos que van a hacer los campos de la tabla
    
    #llave primaria 
    id=db.Column(db.Integer , primary_key=True)
    latitud=db.Column(db.Float(100))
    longitud=db.Column(db.Float(100))
    nombre=db.Column(db.String(30))
    direccion=db.Column(db.String(30))
    horarios=db.Column(db.String(30))
    #Metodo constructor para mapear datos alos campos definidos
    
    def __init__(self, latitud, longitud, nombre, direccion,horarios):
        self.latitud=latitud
        self.longitud=longitud
        self.nombre=nombre
        self.direccion=direccion
        self.horarios=horarios
    
    