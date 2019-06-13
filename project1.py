import json

myplayer=json.load(open("nbaplayer.json"))

def PlayerSearch(name):
    i=1
    search=0
    for k in range(0,len(myplayer)):
        if( (myplayer[k]['firstName'].lower()+' '+myplayer[k]['lastName'].lower())==name.lower()):
            print(myplayer[k])
            search=1
    if(search==0):
        print("invalid entery...PLease try again")

playsearch=input("enter player name")

print(PlayerSearch(playsearch))
