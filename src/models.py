from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column (db.Integer, db.ForeignKey ('user.id'))
    fav_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    fav_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    fav_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))

class People(db.Model): 
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    birth_year = db.Column (db.Integer)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            # do not serialize the password, its a security breach
        }


class Starships (db.Model): 
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String()) 
    model = db.Column (db.String())
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))
    

    def __repr__(self):
        return '<Starships %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            # do not serialize the password, its a security breach
        }
    

class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(250))
    street_number = db.Column(db.String(250))
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))

    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "street_name": self.street_name,
            # do not serialize the password, its a security breach
        }