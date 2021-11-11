"""
A list contains N players details like number(Four Digit ), matches played(50 over matches), 
matches played(20 over matches), and batting average, highest score taken.
• List out player number who got the highest batting score
• List out player number played more number of matches together 50 over and 20 over matches.
• List out the numbers of the players whose batting average is less than the average all players 
batting average.
• List out the player number who played less matches and have batting average is above 80"""

players=[
        [1,62,29,59.07,180],
        [2,73,2,50.53,183],
        [3,50,21,80.55,140],
        [4,40,30,40.34,120]
        ]
hbs=sorted(players,key=lambda x:x[4],reverse=True)
print(f"\u2022  Player number \"{hbs[0][0]}\" have the highest batting score :",hbs[0][-1])


total_matches=[]
for i in players:
    total_matches.append([i[0],i[1]+i[2],i[3]])
print(f"\u2022  Player number \"{sorted(total_matches,key=lambda x:x[1])[-1][0]}\" played more number of matches", "Number of matches played: ",sorted(total_matches,key=lambda x:x[1])[-1][1],sep="\n")

minavg=min(players,key=lambda x :x[3])
print(f"\u2022  Player number \"{minavg[0]}\" got minimum batting average than all","The average is: ",minavg[3],sep="\n")

total_matches=sorted(total_matches,key=lambda x:x[1])
for i in total_matches:
    if i[-1]>80:
        print(f"\u2022  Player number \"{i[0]}\" played less matches and having batting average is above 80","The average is: ",i[-1],"Total matches :",i[-2],sep="\n")
