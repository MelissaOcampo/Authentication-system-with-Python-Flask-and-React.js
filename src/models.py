from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True,nullable=False)
    surname = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(250), unique=False, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    favoritos = db.relationship('Favoritos', backref='usuario', lazy=True)

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            }

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (250))
    skin_color = db.Column(db.String (250))
    species = db.Column(db.String (250))
    favoritos = db.relationship('Favoritos', backref='personajes', lazy=True)

    def __repr__(self):
        return '<Personajes%r>' % self.id

    def serialize(self):

        return {
            "id": self.id,
            "name": self.name,
            "skin_color ": self.skin_color,
            "species" : self.species,
            }


class Vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_capacity = db.Column(db.String (250))
    consumables = db.Column(db.String (250))
    cost_in_credits = db.Column(db.String (250))
    favoritos = db.relationship('Favoritos', backref='vehiculos', lazy=True)

    def __repr__(self):
        return '<Vehiculos%r>' % self.id

    def serialize(self):

        return {
            "id": self.id,
            "cargo_capacity": self.cargo_capacity,
            "consumables ": self.consumables,
            "cost_in_credits" : self.cost_in_credits,
            }

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String (250))
    created = db.Column(db.String (250))
    diameter = db.Column(db.String (250))
    favoritos = db.relationship('Favoritos', backref='planetas', lazy=True)

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):

        return {
            "id": self.id,
            "climate": self.climate,
            "created ": self.created,
            "diameter" : self.diameter,
            }    

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personajes_id = db.Column(db.Integer, db.ForeignKey("personajes.id"))
    vehiculos_id = db.Column(db.Integer, db.ForeignKey("vehiculos.id"))
    planetas_id = db.Column(db.Integer, db.ForeignKey("planetas.id"))
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "personajes_id": self.personajes_id,
            "vehiculos_id": self.vehiculos_id,
            "planetas_id": self.planetas_id,
            "usuario_id ": self.usuario_id ,
            }

