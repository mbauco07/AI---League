import mwclient
import time
import datetime as dt
from datetime import date, timedelta
import json 
from tqdm import tqdm
import pandas as pd
import datetime

"""
parse_games
def: Takes in a list of games and the site url and returns a pandas DataFrame of the games with only specified data.
"""
def parse_games(games_to_parse, site):
    games_data = []
    for i in tqdm(range(len(games_to_parse))):
    #for i in tqdm(range(0,10)):
        game_response = site.api(
            action = "query",
            format = "json",
            prop = "revisions",
            titles = "V5_data:"+games_to_parse[i],
            rvprop = "content",
            rvslots = "main"
            )
        page_id = 0
        for j in game_response['query']['pages']:
            page_id = j
        #this holds the actual game information which itself is a list.
        game_data = game_response['query']['pages'][page_id]['revisions'][0]['slots']['main']['*']

        with open("f.txt", "w") as text_file:
            text_file.write(game_data)

        f = open("f.txt")
        dict = json.load(f)
        #now with the dictionary lets generate the data for the game
        game_list = { 
            'blue': {
                'won' : False,
                'first_tower': False,
                'tower_takedowns': 0,
                'first_blood': False,
                'kills': 0,
                'first_dragon': False,
                'dragon_takedowns': 0,
                'first_baron': False,
                'baron_takedowns': 0,
                'total_gold': 25000,
            },
            'red':{
                'won' : False,
                'first_tower': False,
                'tower_takedowns': 0,
                'first_blood': False,
                'kills': 0,
                'first_dragon': False,
                'dragon_takedowns': 0,
                'first_baron': False,
                'baron_takedowns': 0,
                'total_gold': 25000,
            },
            'id' : games_to_parse[i],
            'duration': 0
        }
        #print(game_list['blue']['first_turret'])
        game_list['blue']['won'] = dict['teams'][0]['win']
        game_list['blue']['first_tower'] = dict['teams'][0]['objectives']['tower']['first']
        game_list['blue']['tower_takedowns'] = dict['teams'][0]['objectives']['tower']['kills']
        game_list['blue']['first_blood'] = dict['teams'][0]['objectives']['champion']['first']
        game_list['blue']['kills'] = dict['teams'][0]['objectives']['champion']['kills']
        game_list['blue']['first_dragon'] = dict['teams'][0]['objectives']['dragon']['first']
        game_list['blue']['dragon_takedowns'] = dict['teams'][0]['objectives']['dragon']['kills']
        game_list['blue']['first_baron'] = dict['teams'][0]['objectives']['baron']['first']
        game_list['blue']['baron_takedowns'] = dict['teams'][0]['objectives']['baron']['kills']

        game_list['red']['won'] = dict['teams'][1]['win']
        game_list['red']['first_tower'] = dict['teams'][1]['objectives']['tower']['first']
        game_list['red']['tower_takedowns'] = dict['teams'][1]['objectives']['tower']['kills']
        game_list['red']['first_blood'] = dict['teams'][1]['objectives']['champion']['first']
        game_list['red']['kills'] = dict['teams'][1]['objectives']['champion']['kills']
        game_list['red']['first_dragon'] = dict['teams'][1]['objectives']['dragon']['first']
        game_list['red']['dragon_takedowns'] = dict['teams'][1]['objectives']['dragon']['kills']
        game_list['red']['first_baron'] = dict['teams'][1]['objectives']['baron']['first']
        game_list['red']['baron_takedowns'] = dict['teams'][1]['objectives']['baron']['kills']

        #now we determine the total gold of each time from each players individual gold income.
        #blue side:
        for i in range(0,5):
            game_list['blue']['total_gold'] += dict['participants'][i]['goldEarned']
        #red side:
        for i in range(4,9):
            game_list['red']['total_gold'] += dict['participants'][i]['goldEarned']

        game_list['id'] =  games_to_parse[i]
        game_list['duration'] =  dict['gameDuration']
        #print(game_list['blue'])   

        #print(game_list['red'])
    
        #clear file so we can reuse it later
        with open("f.txt",'r+') as file:
            file.truncate(0)
        games_data.append(game_list)
    winDF = pd.DataFrame(columns=[ 'id', 'Side', 'Duration', 'Gold Diff', 'First Blood', 'Kills','First Tower', 'Tower Takedowns', 'First Dragon', 'Dragon Takedowns', 'First Baron', 'Baron Takedowns'])
    blueWinsDF = pd.DataFrame(columns=[ 'id', 'Gold Diff', 'First Blood', 'Kills','First Tower', 'Tower Takedowns', 'First Dragon', 'Dragon Takedowns', 'First Baron', 'Baron Takedowns'])
    redWinsDF = pd.DataFrame(columns=['id', 'Gold Diff', 'First Blood', 'Kills','First Tower', 'Tower Takedowns', 'First Dragon', 'Dragon Takedowns', 'First Baron', 'Baron Takedowns'])
    for game in games_data:
        if game['blue']['won'] == True : 
            new_row = pd.DataFrame([
                    {
                    'id':  game['id'],
                    'Side' : 'BLUE',
                    'Duration':  str(datetime.timedelta(seconds = game['duration'])),
                    'Gold Diff': (game['blue']['total_gold'] - game['red']['total_gold']),
                    'First Blood': True,
                    'Kills': game['blue']['kills'],
                    'First Tower': game['blue']['first_tower'],
                    'Tower Takedowns' : game['blue']['tower_takedowns'],
                    'First Dragon': game['blue']['first_dragon'],
                    'Dragon Takedowns' : game['blue']['dragon_takedowns'],
                    'First Baron': game['blue']['first_baron'],
                    'Baron Takedowns' : game['blue']['baron_takedowns']
                }
                ]
                )
            winDF = pd.concat([winDF, new_row])
        else: 
            new_row = pd.DataFrame([
                    {
                    'id':  game['id'],
                    'Side' : 'RED',
                    'Duration':  str(datetime.timedelta(seconds = game['duration'])),
                    'Gold Diff':(game['red']['total_gold'] - game['blue']['total_gold']),
                    'First Blood': True,
                    'Kills': game['red']['kills'],
                    'First Tower': game['red']['first_tower'],
                    'Tower Takedowns' : game['red']['tower_takedowns'],
                    'First Dragon': game['red']['first_dragon'],
                    'Dragon Takedowns' : game['red']['dragon_takedowns'],
                    'First Baron': game['red']['first_baron'],
                    'Baron Takedowns' : game['red']['baron_takedowns']
                }
            ]
            )
            winDF = pd.concat([winDF, new_row])
    #return blueWinsDF, redWinsDF
    return winDF

#Helper function that returns the String value of the position the a champion Played in a given game.
def return_position(i):
    if i == 0 or i == 5:
        return "Top"
    elif i == 1 or i == 6:
        return "Jungle"
    elif i == 2 or i == 7:
        return "Middle"
    elif i == 3 or i == 8:
        return "Bottom"
    elif i == 4 or i == 9:
        return "Support"
    return "ERROR"

def parse_champs(games_to_parse, site):
    champDF = pd.DataFrame(columns=[ 'id', 'Side', 'Champion Name', 'Kills',  'Deaths', 'Assists', 'Position', 'Gold Per Minute', 'Damage Per Minute', 'Team Damage Percentage', 'Won'])   
    for i in tqdm(range(len(games_to_parse))):
    #for i in tqdm(range(0,20)):
        game_response = site.api(
            action = "query",
            format = "json",
            prop = "revisions",
            titles = "V5_data:"+games_to_parse[i],
            rvprop = "content",
            rvslots = "main"
            )
        page_id = 0
        for j in game_response['query']['pages']:
            page_id = j
        #this holds the actual game information which itself is a list.
        game_data = game_response['query']['pages'][page_id]['revisions'][0]['slots']['main']['*']
        with open("f.txt", "w") as text_file:
            text_file.write(game_data)

        f = open("f.txt")
        dict = json.load(f)
        #this is a list of every champ and theior corresponding data for a given game (each entry is a new champ even if its already in the list)
        #We can also say because the data for each game is ordered the same way the order in which the champs are ordered also gives us the position the champions played.
        #i.e 0 & 5 were Top, 1 & 6 were Jungle, 2 & 7 were Middle, 3 & 8 were Bottom, 4 & 9 were Support
        for i in range (0,10):
            if i <=4:
                #print("BLUE SIDE")
                new_row = pd.DataFrame([
                        {
                        'id':  games_to_parse[i],
                        'Side' : 'Blue',
                        'Champion Name': dict['participants'][i]['championName'],
                        'Kills': dict['participants'][i]['kills'],
                        'Deaths': dict['participants'][i]['deaths'],
                        'Assists': dict['participants'][i]['assists'], 
                        'Position': return_position(i),
                        'Gold Per Minute': round(dict['participants'][i]['challenges']['goldPerMinute'],2), 
                        'Damage Per Minute':  round(dict['participants'][i]['challenges']['damagePerMinute'],2),
                        'Team Damage Percentage': round(dict['participants'][i]['challenges']['teamDamagePercentage']*100,2),
                        'Won': dict['participants'][i]['win']       
                        }
                    ]       
                )
            elif i > 4:
                #print("RED SIDE")
                new_row = pd.DataFrame([
                        {
                        'id':  games_to_parse[i],
                        'Side' : 'Red',
                        'Champion Name': dict['participants'][i]['championName'],
                        'Kills': dict['participants'][i]['kills'],
                        'Deaths': dict['participants'][i]['deaths'],
                        'Assists': dict['participants'][i]['assists'], 
                        'Position': return_position(i),
                        'Gold Per Minute': round(dict['participants'][i]['challenges']['goldPerMinute'],2), 
                        'Damage Per Minute':  round(dict['participants'][i]['challenges']['damagePerMinute'],2),
                        'Team Damage Percentage': round(dict['participants'][i]['challenges']['teamDamagePercentage']*100,2),
                        'Won': dict['participants'][i]['win']       
                        }
                    ]       
                )
            champDF = pd.concat([champDF, new_row])
    return champDF

def generate_details_champs(df):
    
    return None