from flask import Flask, render_template,request,redirect,url_for
from db import db
from localizaciones import datos


class programa:
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///localizaciones.sqlite3"
        
       
       #agregar nuestra db a la aplicacion
        db.init_app(self.app)    
    

        self.app.add_url_rule("/" , view_func=self.mapa)
        self.app.add_url_rule("/nuevo" , view_func=self.agregar, methods=["GET", "POST"])
        
        #Iniciar el servidor 
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)
        
    def mapa(self):
        return render_template("mapa.html",carnicerias=datos.query.all())
        
    def agregar(self):
        #verificar si debe enviar el formulario o procesar los datos
        if request.method=="POST":
            #crear un objeto de la clase Localizacion con los valores  del fotmulario
            latitud=request.form["latitud"]
            longitud=request.form["longitud"]
            nombre=request.form["nombre"]
            direccion=request.form["direccion"]
            horarios=request.form["horarios"]
            
            los_datos=datos(latitud,longitud,nombre,direccion,horarios)
            
            #guardar el objeto en la db
            
            db.session.add(los_datos)
            db.session.commit()
            return redirect(url_for("mapa"))
            
        
        
        return render_template("form.html")

miprograma=programa()
