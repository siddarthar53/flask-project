from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash


# User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    
    # Relationship with the Password model
    password = db.relationship('Password', backref='user', uselist=False)

    def __repr__(self):
        return f'<User {self.first_name} {self.email}>'

# Password model
class Password(db.Model):
    __tablename__ = 'passwords'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return f'<Password for User ID {self.user_id}>'

    @classmethod
    def set_password(cls, plain_password):
        # Generate password hash
        return generate_password_hash(plain_password)

# Create tables
db.create_all()

# Example of how you might add a user and a password
def add_user_and_password(email, first_name, password):
    user = User(email=email, first_name=first_name)
    db.session.add(user)
    db.session.commit()

    # Create password entry
    hashed_password = Password.set_password(password)
    password_entry = Password(password_hash=hashed_password, user_id=user.id)
    db.session.add(password_entry)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
