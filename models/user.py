from db import db
# from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from flask_bcrypt import generate_password_hash, check_password_hash
import uuid

class UserModel(db.Model):
    __tablename__ = 'users'

    def generate_uuid():
        return str(uuid.uuid4())
    
    id = db.Column(db.Integer, primary_key=True) # default=generate_uuid()
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Binary(60), nullable=False)
    fullname = db.Column(db.String(80))

    def __init__(self, email, plaintext_password, fullname=''):
        self.email = email
        self.password = generate_password_hash(plaintext_password)
        self.fullname = fullname
    
    # @hybrid_property
    # def password(self):
    #     return self._password

    # def set_password(self, plaintext_password):
    #     self._password = generate_password_hash(plaintext_password)
    
    # @hybrid_method
    def is_correct_password(self, plaintext_password):
        print("inside is_correct_password function")
        return check_password_hash(self.password, plaintext_password)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
