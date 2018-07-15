import spotipy
import spotipy.util as util
import requests
import json
username = str(input("Hey what's your spotify username?"))
def list_playlists(x, y,):
    number = -1
    for i in results['items']:
        number += 1
        print(number,results['items'][number]['name'])
    playlist = int(input("select playlist"))
    return playlist
def list_songs(results, playlist, number, numreal, offset):
    while number == 99:
        trackrequest = requests.get('http://api.spotify.com/v1/users/'+username+'/playlists/'+results['items'][playlist]['id']+'/tracks', params = {'offset' : offset},  headers = {"Content-Type":"application/json", 'Authorization':"Bearer "+token})
        playresult = trackrequest.json()
        number = -1
        offset += 100
        for i in playresult['items']:
            number += 1
            numreal += 1
            print(numreal, playresult['items'][number]['track']['name'] + ' - ' + playresult['items'][number]['track']['album']['artists'][0]['name'])
while True:
    try:
        '''
        print('1. List songs \n2. Play a song')
        select = str(input('What do you want to do? '))
        result = []
        if select == '1':'''
        token = util.prompt_for_user_token(username,'playlist-read-private',client_id='723d300829e842f8abb20a1d9dc8f80d',client_secret='23901c4170be4a27bc907e656797c640',redirect_uri='http://localhost')
        sp = spotipy.Spotify(auth=token)
        request = requests.get('https://api.spotify.com/v1/me/playlists' , headers = {'Authorization': 'Bearer ' + token})
        results = request.json()
        playlist = list_playlists(request, results)
        number = 99
        offset = 0
        numreal = 0
        print('-------------------------------------------------------------------------------------------------------------')
        list_songs(results, playlist, number, numreal, offset)
        print('-------------------------------------------------------------------------------------------------------------')
    except:
        print('uh oh. Something has gone wrong.')

