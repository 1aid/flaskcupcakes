"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False, default='https://tinyurl.com/demo-cupcake')

    def to_dict(self):
        """Serialize cupcake to a dict of cupcake info."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "rating": self.rating,
            "size": self.size,
            "image": self.image,
        }


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)