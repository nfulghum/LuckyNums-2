from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User model"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.Text, nullable=False)
    lucky_num = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.id} name={self.name} email={self.email} year={self.year} color={self.color} lucky_num={self.lucky_num} >"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'year': self.year,
            'color': self.color,
            'lucky_num': self.lucky_num
        }
