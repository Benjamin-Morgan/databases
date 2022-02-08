"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    title = Stringfield('Playlist Name', validators=[InputRequired(message='Playlist name cannot be blank')])



class SongForm(FlaskForm):
    """Form for adding songs."""

    song = Stringfield('Song', validators=[InputRequired(message='Song title required')])
    artist = Stringfield('Artist', validators=[InputRequired(message='Artist required')])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
