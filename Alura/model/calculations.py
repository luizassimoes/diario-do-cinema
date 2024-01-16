from app import db

class Calculations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    avg = db.Column(db.DECIMAL(10, 2))
    sd = db.Column(db.DECIMAL(10, 2))
    
    def __repr__(self):
        return '<Name %r>' % self.name