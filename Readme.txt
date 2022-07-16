Instalation:
======================================================================================
Do not run project until you finished all steps!!!
======================================================================================


---------------------
Installing Python
---------------------


1. Install Pycharm - https://www.jetbrains.com/pycharm/download/#section=windows
 1.a Open folder "Joseph_Oluwasegun_project_discord_bot"
 1.b Click Trust project
 1.c Setup interpreter to default install location (mine is C:\Python310)
 1.d Setup Python 3.10
2. Click (run as Administrator) .bat file "click here" to install neccesary python modules
--->Alternative: 1<---
2.1 Type in terminal in Pycharm
copy and paste line by line:
_________________________________
pip install discord
pip install os
pip install colorama
pip install requests
pip install time
pip install termcolor
pip install python-dotenv
python -m pip install rich
pip install termcolor
pip install DateTime
__________________________________
--->Alternative: 2<---
2.2 Move cursor on uninstalled packages for example (from dotenv import load_dotenv)-> move cursos on dotenv. It will popup install dotenv package. Click on it! Repeat for all red underlined modules.
Exception is dotenv module that requiers advance->install python-dotenv module


---------------------
Installing Javascript
---------------------


3. Install Visual Studio Code - https://code.visualstudio.com
4. Install NodeJs - https://nodejs.org/en/ #
4.1 IMPORTNANT ! - Check Automatically install the neccessary tools. Note that this will also install Chocolately. The script will pop-up in a new window afte the installation completes.

5. Type Windows Power shell in search bat and run it as administrator
copy and paste line by line:
_________________________________
npm install chalk
npm install chalk-animation
npm install discord.js-selfbot-v13
npm install dotenv
npm install easy-json-database
npm install follow-redirects
npm install fs
npm install fs-extra
npm install gradient-string
npm install nanospinner
npm install uniqid
__________________________________
--->Alternative: 1<---
Click (run as Administrator) .bat file "click here 2" to install neccesary python modules

-----------------------
Getting neccessary info
-----------------------

6. Open Discord in browser
7. Click on settings 
8. Select Advanced tab
9. Click enable Developer Mode
10. Click 'F5' / Reload the page
11. Click CTR+SHIFT+I
12. Click on Network
13. Click 'F5' / Reload the page
14. Write /api
15. Click 'F5' / Reload the page
16. Scroll down to authorization:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
17. Your token is XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
18. Close, and reload the page
19. To get SERVERID/GUILDID right click on server and click Copy ID
20. To get CHANNELID right click on channel and clicl Copy ID
21. Put this data to .env file along with Time( time between two messages, more is better)






=======================================================================================
Instalation video: https://drive.google.com/file/d/18M8Ycm8980sCBDbuLdY9KkaJ1YyU8yNe/view?usp=sharing





Running for first time:
=======================================================================================
1.Open project in Visual Studio Code and enter manually:
	a)Discord Token (showed in video how do you get it)
	b)Guild Id
	c)Channel Id
	d)Time for each message (Tip: In order not to get noticed by discord auto timeout bot, I am suggesting you to put minimum 30s=more it is better to avoid discord auto shaddowing (8h of daily work=8 * 60minutes=8 * 60 * 60 sec=28800s -> 960 messages sent)- However you can change it to whatever value you want :) !
2.Run opened project with Node.js debugger
3.Enter desired text in text.txt file<-------------------------------------------------
4.Open project in Pycharm
5.Run the program - > In the console will be all information you provided+current proccesses
6.You can leave the program in background
7.After you are done close the project (exit) and repeat step 1) next time you want to run this tool
=======================================================================================
Setup & demo video: https://drive.google.com/file/d/11dqDkhbMwc5dXKFg8cYX7Kl8DI_chH5e/view?usp=sharing
























