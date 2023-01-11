from datetime import time
from threading import Thread
from flask import Flask, render_template, request
import api_request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recently_played')
def home_page():
    return render_template('recent.html', users=api_request.played_day_ago())


@app.route('/contact')
def contact_page():
    return render_template('sidenav.html')

'----------------------------------------------------Songs--------------------------------------------------'

@app.route('/top_tracks', methods=['GET', 'POST'])
def songs():
    return render_template('song_page.html')

@app.route('/short_term')
def short_term():
    return render_template('song_page.html', users=api_request.top_songs('short_term'), time="Top Tracks(Last 4 Weeks)")

@app.route('/medium_term')
def medium_term():
    return render_template('song_page.html', users=api_request.top_songs('medium_term'), time="Top Tracks(Last 6 Moths)")

@app.route('/long_term')
def long_term():
    return render_template('song_page.html', users=api_request.top_songs('long_term'), time="Top Tracks(All Time)")

'--------------------------------------------------------------------------------------------------------------'


'--------------------------------------------------Artists-----------------------------------------------------'

@app.route('/top_artists', methods=['GET', 'POST'])
def artists():
    return render_template('artists_page.html')

@app.route('/short_term_artist')
def short_term_artists():
    return render_template('artists_page.html', users=api_request.top_artists('short_term'), time="Top Artists(Last 4 Weeks)") 

@app.route('/medium_term_artist')
def medium_term_artists():
    return render_template('artists_page.html', users=api_request.top_artists('medium_term'), time="Top Artists(Last 6 Moths)")

@app.route('/long_term_artist')
def long_term_artists():
    return render_template('artists_page.html', users=api_request.top_artists('long_term'), time="Top Artists(All Time)")

'----------------------------------------------------------------------------------------------------------------------'


if __name__ == '__main__':
    app.run(debug=True, threaded=True)


