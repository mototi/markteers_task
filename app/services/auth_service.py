from app.models import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    

    if not user:
        return None 

    if not check_password_hash(user.password, password):
        return None  

    access_token = create_access_token(identity=user.id)
    return access_token  
