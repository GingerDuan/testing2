from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))

class CandyLand(db.Model):
    """Not a real Board game."""

    __tablename__ = "Candy_Land"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    test_game = CandyLand(name = "candyland", description = "Pull a random card from the pile and the card will tell you how many spaces you can move up the board. If you get the 'cookie' card the game will end for you.", )

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
