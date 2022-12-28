
import mwclient
from tqdm import tqdm
import parse_code
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt	
site = mwclient.Site('lol.fandom.com', path='/')

response = site.api(
	action = "cargoquery",
	limit = "max",
	tables = "MatchScheduleGame=MSG, MatchSchedule=MS",
	fields = "RiotPlatformGameId, Blue, Red",
	where = "MSG.OverviewPage='LCS/2022 Season/Championship'",
	join_on = "MSG.MatchId=MS.MatchId",
	order_by = "MS.DateTime_UTC ASC"
)

games_to_parse =[]
games_data = {}
for i in response['cargoquery']:
    #print(i['title']['RiotPlatformGameId'])
    games_to_parse.append(i['title']['RiotPlatformGameId'])

winsDF = pd.DataFrame()
blueDF = pd.DataFrame()
redDF = pd.DataFrame()
print("parsing in progress...")
#blueDF, redDF = parse_code.parse_games(games_to_parse, site)
winDF = parse_code.parse_games(games_to_parse, site)
print("DONE!")
#now with the data parsed let's learn some basic stats about the winning team.

print(winDF.head())
sns.histplot(data=winDF, x='Side', hue='Side')
plt.show()
