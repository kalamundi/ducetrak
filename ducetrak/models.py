from ducetrak import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def __repr__(self):
        return f'<User {self.username}>'