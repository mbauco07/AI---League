
import mwclient
from tqdm import tqdm
import parse_code
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt	
site = mwclient.Site('lol.fandom.com', path='/')


match_overview_page = "2022 Season World Championship/Main Event"
if "LPL" in match_overview_page:
    raise Exception("Sorry, LPL does not have RiotGamesID due we can't parse it")

response = site.api(
	action = "cargoquery",
	limit = "max",
	tables = "MatchScheduleGame=MSG, MatchSchedule=MS",
	fields = "RiotPlatformGameId, Blue, Red",
	where = "MSG.OverviewPage='"+match_overview_page+"'",
	join_on = "MSG.MatchId=MS.MatchId",
	order_by = "MS.DateTime_UTC ASC"
)

games_to_parse =[]
games_data = {}

for i in response['cargoquery']:
    #print(i['title']['RiotPlatformGameId'])
    games_to_parse.append(i['title']['RiotPlatformGameId'])

winsDF = pd.DataFrame()

print("parsing in progress...")
#blueDF, redDF = parse_code.parse_games(games_to_parse, site)
winDF = parse_code.parse_games(games_to_parse, site)
print("DONE!")
#now with the data parsed let's learn some basic stats about the winning team.

print(winDF.head())
fig, axes = plt.subplots(3, 3, figsize=(18, 10))
sns.countplot(ax=axes[0,0], data=winDF, x='Side', hue='Side')
sns.countplot(ax=axes[0,1], data=winDF, x='First Tower', hue='Side').set_title("Side wins by First Tower")
sns.countplot(ax=axes[0,2], data=winDF, x='First Blood', hue='Side').set_title("Side wins by First Blood")
sns.countplot(ax=axes[1,0], data=winDF, x='First Dragon', hue='Side').set_title("Side wins by First Dragon")
sns.countplot(ax=axes[1,1], data=winDF, x='Dragon Takedowns', hue='Side').set_title("Dragon takedown when a team wins")
sns.countplot(ax=axes[1,2], data=winDF, x='First Baron', hue='Side').set_title("Side wins by First Baron")
sns.histplot(ax=axes[2,0], data=winDF, x='Gold Diff',  hue='Side').set_title("Team side wins by Gold Diff")
axes[2,1].set_axis_off()
axes[2,2].set_axis_off()

fig.suptitle('Team Side win Data for: '+match_overview_page , fontsize=16)
fig.tight_layout()

plt.savefig("Worlds 2022 Main Event.png")
plt.show()