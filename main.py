import datetime
import discum
import os.path
import random
import os
import time
from rich import print
from dotenv import load_dotenv
from termcolor import colored


data=[]
memberz = []

load_dotenv()


dictionary={}

timez=0
messagz=''
channelz=[]
guildz=''

dictionary["channel_id"]=os.getenv('CHANNEL_ID')
dictionary["server_id"]=os.getenv('GUILDID')
dictionary["token"]=os.getenv('TOKEN')
dictionary["time"]=os.getenv('TIME')

tempmessage=''

print(colored("==============================================",'blue','on_grey'))
print(colored("==============================================",'blue','on_grey'))
print(colored("==============================================",'blue','on_grey'))
print(colored("                                              ",'blue','on_grey'))
print(colored("		        Welcome                     ",'blue','on_grey',attrs=['bold']))
print(colored("                                              ",'blue','on_grey'))
print(colored("    Discord auto messaging tool version 1.0.0 ",'blue','on_grey'))
print(colored("                                              ",'blue','on_grey'))
print(colored("==============================================",'blue','on_grey'))
print(colored("==============================================",'blue','on_grey'))
print(colored("==============================================",'blue','on_grey'))
print(colored("			      by Luka Mladenovic",'blue','on_grey'))
print()



print(colored("Imporing TOKEN....",'yellow','on_grey'))
if "token" in dictionary.keys() and dictionary["token"] !='' and len(dictionary["token"]):

    print(colored(f'Imported token=','blue','on_grey') ,end='' )
    print(colored(dictionary["token"],'magenta'))
    token=dictionary["token"]
    print(colored("--->Token imported successfully", 'green', 'on_grey'))
else:
    print(colored( "Failed to import token! How to fix it - Add him in .env file",'red','on_grey'))
    exit(1)
print(colored("Imporing GUILDID....",'yellow','on_grey'))
if "server_id" in dictionary.keys() and dictionary["server_id"]!='\n' and len(dictionary["server_id"]):

    print(colored(f'Imported server_id=', 'blue', 'on_grey'), end='')
    print(colored(dictionary["server_id"], 'magenta'))
    print(colored("--->GUILDID imported successfully", 'green', 'on_grey'))
    guildz=dictionary["server_id"]
else:
    print(colored("Failed to import GUILDID! How to fix it - Add him in .env file", 'red', 'on_grey'))
    exit(1)
print(colored("Imporing TIME....", 'yellow', 'on_grey'))
if "time" in dictionary.keys() and len(dictionary["time"]):

    print(colored(f'Imported TIME=', 'blue', 'on_grey'), end='')
    print(colored(dictionary["time"], 'magenta'))
    print(colored("--->TIME imported successfully", 'green', 'on_grey'))


    timez=int(dictionary["time"])
    if timez<=0:
        print(colored("Failed to import TIME! Value can not be negative!", 'red', 'on_grey'))
        exit(1)
else:
    print(colored("Failed to import time! How to fix it - Add him in .env file", 'red', 'on_grey'))
    exit(1)
print(colored("Imporing CHANNEL_ID....", 'yellow', 'on_grey'))
if  "channel_id" in dictionary.keys()and len(dictionary["channel_id"]):

    print(colored(f'Imported CHANNEL_ID=', 'blue', 'on_grey'), end='')
    print(colored(dictionary["channel_id"], 'magenta'))
    print(colored("--->CHANNEL_ID imported successfully", 'green', 'on_grey'))

    channelz.append( dictionary["channel_id"])
else:
    print(colored("Failed to import CHANNEL_ID! How to fix it - Add him in .env file", 'red', 'on_grey'))
    exit(1)

file_message_in=open("text.txt","r",encoding='utf-8')
print(colored("Importing file text.txt",'yellow','on_grey'))
if file_message_in is None:
    print(colored( "Text.txt file is deleted/non existing! How to fix it? - create a text.txt file and enter message in it!",'red','on_grey'))
    exit(1)
print(colored("--->File imported successfully",'green','on_grey'))
for e in file_message_in:
    tempmessage+=e
dictionary["message"]=tempmessage

if "message" in dictionary.keys()and len(dictionary["message"]):
    messagz=dictionary["message"]
else:
    print(colored( "Message in text.txt is empty",'red','on_grey'))
    exit(1)



print(colored("===================Creating request====================", 'green', 'on_grey'))
bot = discum.Client(token=token, log=False)
if bot:
    print(colored("==============Succesfully created request==============", 'green', 'on_grey'),end='')
    print()
else:
    print("Error in Fetching Discord API , please check internet connection")
    exit(1)

fin1=open(os.path.dirname(__file__)+"\\src\\username"+"\\"+dictionary["server_id"]+"\\username.txt","r",encoding='utf-8');
name_dict={}
for e in fin1:
    x=e.split()
    memberz.append(x[0])
    name_dict[x[0]]=x[2]
starting_time_for_connecting_to_discord=time.time()
print(colored("Connecting to Discord.....",'yellow','on_grey'))

@bot.gateway.command
def memberTest(resp):
    if resp.event.ready_supplemental:
        for channel in channelz:
            bot.gateway.fetchMembers(guildz, channel)
    if bot.gateway.finishedMemberFetching(guildz):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()


bot.gateway.run()
if(starting_time_for_connecting_to_discord>15):
    print(colored("Loading....",'yellow','on_grey'))
ending_time_for_connecting_to_discord=time.time()
print(colored(f'Time elapsed {ending_time_for_connecting_to_discord-starting_time_for_connecting_to_discord}s','yellow','on_grey'))
print(colored("Connected!", 'green', 'on_grey'))

howmany=0
print(colored("Starting to DM.", 'green', 'on_grey'))



for x in memberz:
    howmany+=1
    try:
        rand = random.randint(0, 20)
        if rand == 10 and howmany>10:
            print(colored(f'Sleeping for 600 seconds to prevent rate-limiting.','yellow','on_grey'))
            time.sleep(600)


        print(colored(f"Preparing to DM {name_dict[x]}.", 'yellow', 'on_grey'))
        newDM = bot.createDM([f"{x}"]).json()["id"]
        bot.sendMessage(newDM,
                        f"{messagz} ")
        print(colored(f'--->DMed {name_dict[x]}.', 'green', 'on_grey'))
        print(colored(f'Sleeping for {int(timez)} seconds to prevent rate-limiting.', 'yellow', 'on_grey'))
        time.sleep(int(timez))
        print(colored('--------------------------------------------------------','magenta','on_grey'))
    except Exception as E:
        print(colored(E, 'green', 'on_grey'))
        print(colored(f'Couldn\'t DM {name_dict[x]}.', 'green', 'on_grey'))


print(colored("DMed all active users!", 'green'))
print(colored("Thank you for using this software!",'green'))

fin1.close()
file_message_in.close()



def log_id(reason,id,name,discriminator,guild):
    now=datetime.time
    current_time=now.strftime("%H:%M")
    try:
        with open("blacklistedids.json","r") as file:
            if id not in file:
                pass
            elif id in file:
                return
        with open("usernames.txt","r+") as file:
            time.sleep(0.1)
            if id not in file:
                data.append(id)
                time.sleep(0.1)
        with open(os.path.dirname(__file__)+"\\src\\database\\"+guild+"\\database.json","r") as file:
            try:
                print(current_time+guild+"reason of failure - "+reason)
            except (Exception):
                print(Exception)
    except:
        return



