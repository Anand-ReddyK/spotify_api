import requests
import utc_converter

# get a new token from here
# https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/?type=tracks&time_range=long_term&limit=10&offset=0

token = "BQAr9WeusM0G7p7rbtT1vxO7ht2rslPHwjQTgdJLpLbNXLoatO49hhlQePkA8begclybUeCca770xvnLZYrE-ekApYn0UGNhj_EGliv5_xn-SW_cliA3VrQQy2cgbsmNWeKI_9w5gW1XVcWZoFnl3zZq2CSEv0Cx4NZKkr_Kx07QDdt8oKNWiD3ZbYyk-p-GotyfszXl6Q"

def top_songs(time):

    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {token}"
    }

    r = requests.get(f"https://api.spotify.com/v1/me/top/tracks?time_range={time}&limit=50", headers=headers)

    data = r.json()

    item_i_need = {}
    i = 1
    for item in data['items']:

        names = [x['name'] for x in item['artists']]
        a = ', '
        a = a.join(names)

        
        item_i_need[item['name']] = {'url' : item['external_urls']['spotify'], 'song_img' : item['album']['images'][1]['url'], 'num': str(i), 'artist': a}

        i += 1
       
        

#     items_sorted = sorted(item_i_need.items(), key= lambda x: x[1]['popularity'], reverse=True)

#     for i in range(len(items_sorted)):
#         items_sorted[i][1]['num'] = str(i + 1)

    return item_i_need.items()



def top_artists(time):
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {token}"
    }

    r = requests.get(f"https://api.spotify.com/v1/me/top/artists?time_range={time}&limit=30", headers=headers)

    data = r.json()

    item_i_need = {}
    i = 1

    for item in data['items']:
        # print(item['name'])
        # print(item['images'][1])
        # print(item['external_urls']['spotify'])
        item_i_need[item['name']] = {'image': item['images'][1], 'url': item['external_urls']['spotify'], 'num': str(i)}

        i += 1

    return item_i_need.items()


def played_day_ago():
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {token}"
    }
    time = utc_converter.yestr_unix_stam()
    r = requests.get(f"https://api.spotify.com/v1/me/player/recently-played?limit=50&before={time}", headers=headers)

    data = r.json()
    # print(data, 'llllllll')

    items_i_need = {}
    for item in data['items']:
        names = ''
        date_time = utc_converter.utc_to_local(item['played_at'])
        # print(item['played_at'])
        for name in item['track']['album']['artists']:
            names += name['name'] + ', '
        
        names = names[:-2]
        
        # print(item['track']['name'])
        
        items_i_need[item['track']['name']] = {'artists': names, 'time': date_time}
        
    # print(list(items_i_need.items())[0][1]['time'], 'llllllll')
    recent_songs = list(items_i_need.items())

    recent_songs = sorted(recent_songs, key= lambda x: x[1]['time'], reverse=True)
    # print(recent_songs)

    return recent_songs
    # return items_i_need.items()

        


played_day_ago()

# if __name__ == "__main__":
#     played_day_ago()
#     # a = top_songs('long_term')
#     # for user in a:
#     #     print(user)
#     #     break
#     a = top_artists('long_term')
#     for i in a:
#         print(i)
#         break
