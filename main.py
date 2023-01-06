
import mwclient
from tqdm import tqdm
import parse_code
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt	
site = mwclient.Site('lol.fandom.com', path='/')


#parse the games with general game data in mind and then create some plots with data from them
def get_league_data():
    #blueDF, redDF = parse_code.parse_games(games_to_parse, site)
	winDF = parse_code.parse_games(games_to_parse, site)
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

#parse the games with the goal of generating data from the champions played
def get_league_champ_data(games_to_parse):
	champsDF = pd.DataFrame()
	champsDF = parse_code.parse_champs(games_to_parse, site)
	#print(champsDF['Champion Name'].value_counts())
	#print(champsDF.value_counts(['Champion Name', 'Won']))
	df = champsDF.value_counts(['Champion Name', 'Won']).rename_axis(['Champion Name', 'Won']).reset_index(name='Count')
	fig, axes = plt.subplots(4, 5, figsize=(18, 10))
	#General Champ Data
	sns.barplot(ax=axes[0,0], y=champsDF['Champion Name'].value_counts().head(10).index, x=champsDF['Champion Name'].value_counts().head(10)).set_title("Top 10 most played Champions")
	sns.barplot(ax=axes[0,1], y=champsDF['Champion Name'][champsDF['Side'] =='Blue'].value_counts().head(10).index, x=champsDF['Champion Name'][champsDF['Side'] == 'Blue'].value_counts().head(10), color="Blue").set_title("Top 10 Blue Side Champs")
	sns.barplot(ax=axes[0,2], y=champsDF['Champion Name'][champsDF['Side'] =='Red'].value_counts().head(10).index, x=champsDF['Champion Name'][champsDF['Side'] == 'Red'].value_counts().head(10), color="Red").set_title("Top 10 Red Side Champs")
	sns.barplot(ax=axes[0,3], data=df[df['Won'] == True].head(10), y='Champion Name', x='Count').set_title("Top 10 Most Winningest Champions")

	#General Champ Data
	#Lane Seperated Data
	sns.barplot(ax=axes[1,0], y=champsDF['Champion Name'][champsDF['Position'] =='Top'].value_counts().head(10).index, x=champsDF['Champion Name'][champsDF['Position'] == 'Top'].value_counts().head(10)).set_title("Most Played Top Lane Champs")
	sns.barplot(ax=axes[1,1], y=champsDF['Champion Name'][champsDF['Position'] =='Jungle'].value_counts().head(10).index, x=champsDF['Champion Name'][champsDF['Position'] == 'Jungle'].value_counts().head(10)).set_title("Most Played Jungle Champs")
	sns.barplot(ax=axes[1,2], y=champsDF['Champion Name'][champsDF['Position'] == 'Middle'].value_counts().head(10).index, x=champsDF['Champion Name'][champsDF['Position'] == 'Middle'].value_counts().head(10)).set_title("Most Played Middle Lane Champs")
	sns.barplot(ax=axes[1,3], y=champsDF['Champion Name'][champsDF['Position'] == 'Bottom'].value_counts().head(10).index, x=champsDF['Champion Name'][champsDF['Position'] == 'Bottom'].value_counts().head(10)).set_title("Most Played Bottom Lane Champs")
	sns.barplot(ax=axes[1,4], y=champsDF['Champion Name'][champsDF['Position'] == 'Support'].value_counts().head(10).index, x=champsDF['Champion Name'][champsDF['Position'] == 'Support'].value_counts().head(10)).set_title("Most Played Support Lane Champs")
	sns.histplot(ax=axes[2,0], data=champsDF[champsDF['Position'] =='Top'], x='Team Damage Percentage').set_title("Top-Team DMG % Distribution")
	sns.histplot(ax=axes[2,1], data=champsDF[champsDF['Position'] =='Jungle'], x='Team Damage Percentage').set_title("Jungle-Team DMG %  Distribution")
	sns.histplot(ax=axes[2,2], data=champsDF[champsDF['Position'] =='Middle'], x='Team Damage Percentage').set_title("Middle-Team DMG %  Distribution")
	sns.histplot(ax=axes[2,3], data=champsDF[champsDF['Position'] =='Bottom'], x='Team Damage Percentage').set_title("Bottom-Team DMG %  Distribution")
	sns.histplot(ax=axes[2,4], data=champsDF[champsDF['Position'] =='Support'], x='Team Damage Percentage').set_title("Support-Team DMG %  Distribution")
 	#Lane Seperated Data
	sns.histplot(ax=axes[3,0], data=champsDF[champsDF['Position'] =='Top'], x='Gold Per Minute').set_title("Top-GPM Distribution")
	sns.histplot(ax=axes[3,1], data=champsDF[champsDF['Position'] =='Jungle'], x='Gold Per Minute').set_title("Jungle-GPM  Distribution")
	sns.histplot(ax=axes[3,2], data=champsDF[champsDF['Position'] =='Middle'], x='Gold Per Minute').set_title("Middle-GPM Distribution")
	sns.histplot(ax=axes[3,3], data=champsDF[champsDF['Position'] =='Bottom'], x='Gold Per Minute').set_title("Bottom-GPM Distribution")
	sns.histplot(ax=axes[3,4], data=champsDF[champsDF['Position'] =='Support'], x='Gold Per Minute').set_title("Support-GPM Distribution")
	axes[0,4].set_axis_off()
	fig.tight_layout()	
	plt.show()
 
	plt.savefig("Worlds 2022 Main Event-Champion Data.png")
	plt.show()




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



print("parsing in progress...")
get_league_champ_data(games_to_parse)