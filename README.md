# AI & League
 More in-depth league of legends scripts that may use some AI based learning for predictions later on.
 
 
 ## Simple Report
  After creating some simple data visualizations let's deterime some quick findings about the data.
  
  -Some general caveats first
   - Data from sourced from lol.fandom API information here[^1].
   - I have no intention of using this for profit/monetary reasons, just want to practice my python and data analysis skills. 
   
  -Some notes about that Data
   - I am not generating any new data from the data given to me via the API only some manipulation to normalize it all (Everything is base-10 for example).
   - The data regarding champions only contains information about when a Champion is **picked** not banned.
   - The graphs about dragon takedowns information:
     - When a team get's 4 dragons that is getting dragon soul (which is a very powerfull boost which was added to the game in order to help teams close out games)
     - The 5<sup>th</sup> dragon is Elder Dragon which **only**  spawns after a team have already taken 4 dragons (acquired dragon soul)
   
## General Information about a giving league
-The goal of this data is to see how winning teams in a given league stack up against other regions.
 - With this data we should be able to see how important certain metrics for winnig a game(first blood, first dragon, etc), as well as how many times do upsets occur.
 - 
 
### LCS
![LCS 2022 Summer Championship](https://user-images.githubusercontent.com/31773670/211049375-4a771c0b-c6a5-4992-8eca-0f80ccef406b.png)

### This data is from the LCS 2022 Summer Championship (which is what they call the playoffs)
-Conclusions from the data.
 - Blue side is favoured when it comes to winning
 - Most games in the LCS Championship came down to dragon soul and rarely Elder Dragon.
 - There were no real upsets when a team was already down gold.
 - Blue side won almost the same amount of games regardless of if they got the first dragon or not.
   - However based on dragon takedowns that had more presence for all subsequent dragons after the first.


### LEC
   ![LEC 2022 Summer Playoffs](https://user-images.githubusercontent.com/31773670/211051383-e09e8041-18dc-4b85-8073-478a9b9bafe9.png)
   
-Conclusions from the data.
 - Blue side is favoured when it comes to winning
 - Most games in the LCS Championship came down to dragon soul and rarely Elder Dragon.
 - There were no real upsets when a team was already down gold.
 - Blue side won almost the same amount of games regardless of if they got the first dragon or not.
   - However based on dragon takedowns that had more presence for all subsequent dragons after the first.
   - Blue side had a lot more presence when it came to all "first" categories.
   - Red side only won their matches when they had a **considerable** gold lead, whereas Blue side gold difference was more varied.
   - In the LEC majority of the games again came down to dragon soul.

### LCK
**Please note the colours for the teams have been flipped (apolgies I will fixed this in a later update)**
![LCK 2022 Summer Playoffs](https://user-images.githubusercontent.com/31773670/211051901-bf2d58f2-0bc8-4f2c-87d0-6d157cd7aaf0.png)
-Conclusions from the data.
 - Blue side was more victorious overall 
 - Blue side again won many of their games when they had "firsts"
 - Elder Dragon was not an important winning factor.
 - Baron however was much more important for winning teams


### Worlds 2022 Main Event (Play-In Stage not included).
**Please note the colours for the teams have been flipped (apolgies I will fixed this in a later update)**
![Worlds 2022 Main Event](https://user-images.githubusercontent.com/31773670/211052572-43919853-643c-4cd5-9c4f-21c87bc257d7.png)
-Conclusions from the data.
 - Blue side still is favoured when it comes to winning.
 - Blue side won more agains when they didn't get first dragon.
   - This could be do to focus on other objectives during that time like towers or kills.
 - Regardless of the side teams won with **massive** gold advantages.
   - This could mean that snowballing the game was an important factor.
 



[^1]: https://lol.fandom.com/wiki/Help:Leaguepedia_API
