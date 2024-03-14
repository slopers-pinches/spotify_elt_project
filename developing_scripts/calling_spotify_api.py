from common.spotify_api.functions import get_token
import requests
import pandas as pd
import os

# Declare Spotify Token Variable
token = get_token()

### Get Artist ###

# Spotify API Endpoint Headers
headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {token}".format(token=token)
}

# Delcare Artists' Spotify ID (ex. Bad Omens, Spiritbox, Angelmaker, etc.)
bad_omens_id = "3Ri4H12KFyu98LMjSoij5V"
the_devil_wears_parada_id = "0NbQe5CNgh4YApOCDuHSjb"
spirit_box_id = "4MzJMcHQBl9SIYSjwWn8QW"
paleface_swiss_id = "467M2s2YxXdlL2ZpDUNL3A"
make_them_suffer_id = "0FZcPgWI3BsFQl4rOAGSHT"
angel_maker_id = "1AdrYGYDz4oa9dvW2jfFrG"

# Concatenate artists
artists_ids = bad_omens_id + "," + the_devil_wears_parada_id + "," + spirit_box_id + "," + paleface_swiss_id + "," + make_them_suffer_id + "," + angel_maker_id

# Calling Spotify Artist Endpoint
r = requests.get("https://api.spotify.com/v1/artists/?ids={artist_id}".format(artist_id=artists_ids),
                 headers=headers)
data = r.json()

# Extract relevant info
spotify_artist_id = []
artist_name = []
popularity = []
followers = []
genres = []
type = []

for artist in data["artists"]:
    spotify_artist_id.append(artist["id"])
    artist_name.append(artist["name"])
    popularity.append(artist["popularity"])
    followers.append(artist["followers"]["total"])
    genres.append(artist["genres"])
    type.append(artist["type"])

# Create a dictionary before creating into a panda dataframe
artists_dict = {
    "spotify_artist_id" : spotify_artist_id,
    "artist_name" : artist_name,
    "popularity" : popularity,
    "followers" : followers,
    "genres" : genres,
    "type" : type
}

# Create panada dataframe for artists
column_name = ["spotify_artist_id", "artist_name", "popularity", "followers", "genres", "type"]

artists_df = pd.DataFrame(artists_dict,
                          columns = column_name)

# Export panada dataframe to csv files
file_path = f"{os.getcwd()}/spotify_data"
artists_file_name = "artists"

artists_df.to_csv(path_or_buf=f"{file_path}/{artists_file_name}.csv",
                  index=False
                  )