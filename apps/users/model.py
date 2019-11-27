from apps import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'fk_user1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User(uname: %s)>" % self.uname
