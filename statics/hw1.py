import pandas as pd
import csv
from operator import itemgetter
import matplotlib.pyplot as plt
#Reading the xvs database
file = open("LaLiga_Matches_1995-2021.csv")
csvreader = csv.reader(file)
header = next(csvreader)

#reading the match row from dataset
rows = []
for row in csvreader:
    rows.append(row)
    #making a list of teams names
teams =[]
for match in rows:
    if match[2] in teams:
        pass
    else :
        teams.append(match[2])
    if match[3] in teams :
        pass
    else :
        teams.append(match[3])
"""
***********************
PROBLEM1:
***********************
"""

#this method finds the champion of every year 
def chmpion_finder(year):
    list_of_all_teams = []
    #we are making a list of lists which contain the name of a team and its point during the season
    for team in teams:
        sublist=[]
        sublist.append(team)
        sublist.append(0)
        list_of_all_teams.append(sublist)
    #here we check every match that happened in the dsired year
    for match in rows:
        if match[0] == year:
            #giving scores to teams
            if match[4] == match[5]:
                for x in list_of_all_teams:
                    if x[0]== match[2]:
                        x[1]=x[1]+1
                    elif x[0]==match[3]:
                        x[1]=x[1]+1
            if match[4]>match[5]:
                for x in list_of_all_teams:
                    if x[0]== match[2]:
                        x[1]=x[1]+3
            if match[5]>match[4]:
                for x in list_of_all_teams:
                    if x[0]== match[3]:
                        x[1]=x[1]+3
    '''
    in every season there migth be two teams which have same scores and in order to
    distinguish the champion, we have to check the final game they had with eachother, the winner of that game
    is the champion of the year!
    '''
    the_champion=[]
    max_score = 0
    the_final_champion=""
    #finding the max score of the year
    for x in list_of_all_teams:
        if x[1]> max_score:
            max_score = x[1]
    #clearfying wich teams have the max score 
    for x in list_of_all_teams:
        if x[1] == max_score:
            the_champion.append(x[0])
    #if 2 teams have the max score we check the game that they played eachother as shown below:
    if len(the_champion)>1:
        for match in rows:
            if (match[2]== the_champion[0] and match[3]==the_champion[1]) :
                if match[4]>match[5]:
                    the_final_champion=the_champion[0]
                else:
                    the_final_champion=the_champion[1]
            if (match[2]== the_champion[1] and match[3]==the_champion[0]):
                if match[4]>match[5]:
                    the_final_champion=the_champion[1]
                else:
                    the_final_champion=the_champion[0]
    #if only one team has the max score, clearly that team is the champion
    if len(the_champion)== 1:
        the_final_champion=the_champion[0]
    return the_final_champion
                
#here we are making a list of lists which contaion name of tems and number of their laliga cups
list_of_all_teams2 = []
for team in teams:
    sublist=[]
    sublist.append(team)
    sublist.append(0)
    list_of_all_teams2.append(sublist)
#here we are making valid inputs for the champion choser function to determine champions of every year 
for i in range(1995,2021):
    k = ((i % 100)+1)%100
    k2= str(k)
    if k== 0 :
        k2 ="2000"
    if 0 <k < 10:
        k2='0' + str(k) 
    champion = chmpion_finder(str(i)+'-'+k2)
    for x in list_of_all_teams2:
        if x[0] == champion:
            x[1] = x[1] + 1
#here we are sorting the teams by the number of cups they have achieved in champions leauge
print(sorted(list_of_all_teams2, key=lambda x:x[1], reverse = True))
list_of_all_teams2 = sorted(list_of_all_teams2, key=lambda x:x[1], reverse = True)
print(list_of_all_teams2)
#making a data frame to plot charts
winning_data=[]
labels = []
for x in list_of_all_teams2:
    winning_data.append(x[1])
    labels.append(x[0])
df = pd.DataFrame(winning_data, index=labels, columns=['x'])
df.plot(kind='bar', subplots=True, figsize=(8, 8))
plt.ylabel("Champions League wins")
plt.xlabel("teams")
plt.show()
df.plot(kind='pie', subplots=True, figsize=(8, 8))
plt.show()
##############################################################
"""
***********************
PROBLEM2:
***********************
"""
#this function gets a teams name and a year and returns rank of the team that year
def team_ranker(the_team,year):
    list_of_all_teams = []
    for team in teams:
        sublist=[]
        sublist.append(team)
        sublist.append(0)
        list_of_all_teams.append(sublist)
    for match in rows:
        if match[0] == year:
            if match[4] == match[5]:
                for x in list_of_all_teams:
                    if x[0]== match[2]:
                        x[1]=x[1]+1
                    elif x[0]==match[3]:
                        x[1]=x[1]+1
            if match[4]>match[5]:
                for x in list_of_all_teams:
                    if x[0]== match[2]:
                        x[1]=x[1]+3
            if match[5]>match[4]:
                for x in list_of_all_teams:
                    if x[0]== match[3]:
                        x[1]=x[1]+3
    #ordering teams by their scores that have achieved during the year
    list_of_all_teams = sorted(list_of_all_teams, key=lambda x:x[1],reverse=True)
    #here we check if two teams have same scores, the champion is the one who has won the final match!
    if list_of_all_teams[0][1]==list_of_all_teams[1][1]:
        for match in rows:
            if match[0] == year:
                if (match[2]== list_of_all_teams[0][0] and match[3]==list_of_all_teams[1][0]) :
                    if match[4]<match[5]:
                        temp = list_of_all_teams[0]
                        list_of_all_teams[0]=list_of_all_teams[1]
                        list_of_all_teams[1]=temp
                if (match[2]== list_of_all_teams[1][0] and match[3]==list_of_all_teams[0][0]) :
                    if match[5]<match[4]:
                        temp = list_of_all_teams[0]
                        list_of_all_teams[0]=list_of_all_teams[1]
                        list_of_all_teams[1]=temp 
    rank = 0
    #print(list_of_all_teams)
    for x in list_of_all_teams:
        rank = rank+1
        if x[0] == the_team:
            return rank


#generating valid imputs for team_ranker func!
real_madrid_rank = []
the_year =[]
for i in range(1995,2021):
    k = ((i % 100)+1)%100
    k2= str(k)
    if k== 0 :
        k2 ="2000"
    if 0 <k < 10:
        k2='0' + str(k) 
    real_madrid_rank.append(team_ranker('Real Madrid' ,str(i)+'-'+k2))
    the_year.append(str(i)+'-'+k2)
    print(str(i)+'-'+k2+": "+str(team_ranker('Real Madrid' ,str(i)+'-'+k2)))

df2 = pd.DataFrame(real_madrid_rank, index=the_year, columns=['x'])
df2.plot(kind='line', subplots=True, figsize=(8, 8))
plt.ylabel("rank")
plt.xlabel("year")
plt.show()    
##############################################################
"""
***********************
PROBLEM3:
***********************
"""
faza_nemoone = 0
tedad_halat =0
for match in rows: 
        if match[7]=='':
            match[7]='0'
        if match[8]=='':
            match[8]='0'
        if int(match[7], base =10)-int(match[8], base =10)>=2 :
            faza_nemoone = faza_nemoone+1
            if match[4]>match[5]:
                tedad_halat = tedad_halat+1;
        if int(match[8], base = 10) - int(match[7], base =10)>=2 :
            faza_nemoone = faza_nemoone+1
            if match[5]>match[4]:
                tedad_halat = tedad_halat+1;
print(tedad_halat)
print(faza_nemoone)
print(tedad_halat/faza_nemoone)
##############################################################
"""
***********************
PROBLEM4:
***********************
"""
Hlose=0
H_friday_lose=0
for match in rows:
        date = match[1].split("/")
        if len(date[2])==2:
            date[2]='20'+date[2]
        the_time = date[2] + '-' + date[1]+'-'+date[0]
        if date[0] =='13' and pd.Timestamp(the_time).day_name()=="Friday":
            Hlose = Hlose+1
        if match[4]<=match[5] or match[4]>=match[5]:
            H_friday_lose = H_friday_lose+1
print(H_friday_lose/Hlose)
##################################
Hlose=0
H_friday_lose=0
for match in rows:
    if match[4]<=match[5]:
        Hlose = Hlose+1
        date = match[1].split("/")
        if len(date[2])==2:
            date[2]='20'+date[2]
        the_time = date[2] + '-' + date[1]+'-'+date[0]
        if date[0] =='13' and pd.Timestamp(the_time).day_name()=="Friday":
            H_friday_lose = H_friday_lose+1
print(H_friday_lose)
print(Hlose)
print(H_friday_lose/Hlose)
file.close()