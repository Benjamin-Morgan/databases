"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablname__ = 'playlists'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.Text,
                    nullable=False)
    description = db.Column(db.Text,
                            nullable=False)
                    



class Song(db.Model):
    """Song."""

    __tablname__ = 'songs'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.Text,
                        nullable=False)
    artist = db.Column(db.Text,
                        nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey('playlists.id'))
    song_id = db.Column(db.Integer,
                        db.ForeignKey('song.id'))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
