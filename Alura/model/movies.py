from app import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    grade1 = db.Column(db.DECIMAL(10, 1))
    grade2 = db.Column(db.DECIMAL(10, 1))
    image = db.Column(db.LargeBinary)       # Coluna para armazenar dados binários da imagem

    def __repr__(self):
        return '<Name %r>' % self.name