from app import db

class User(db.Model):
    __tablename__ = 'user'  

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, password={self.password})>"
    
    
class HomeTable(db.Model):
    __tablename__ = 'home_table'  

    id = db.Column(db.Integer, primary_key=True)  
    table_number = db.Column(db.Integer, nullable=False)  


    def __repr__(self):
        return f"<home_table(id={self.id}, email={self.table_number})>"