#########################
# LOLstats by David Oyos
#########################

#import statements
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

#return data frame with champion names and links
def openExcel():
    #read in excel sheet
    sheet = pd.read_excel(r'C:\Users\davidoyos\projects\LOLstat_PYTHON\LOL_CHAMP_LINKS.xlsx')
    df = pd.DataFrame(sheet,columns= ['champ','link'])
    return df

#use Excel sheet to find link of desired champion
def getLink(champion,frame):
    for row in frame.itertuples():
        if (row.champ == champion.capitalize()):
            champ_index = row.Index
    champ_link = frame.at[champ_index,'link']
    return champ_link

#use Excel sheet to find index of desired champion
def getIndex(champion,frame):
    for row in frame.itertuples():
        if (row.champ == champion.capitalize()):
            champ_index = row.Index
    return champ_index

#Use link to find statistics from games
def getData(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', attrs={'class':'value'})
    # in data:
    #   0- win rate
    #   1- rank
    #   2- pick rate
    #   3- ban rate
    #   4- matches
    return data

def winRate(champion):
    desired_link = getLink(champion.capitalize(),openExcel())
    desired_index = getIndex(champion.capitalize(),openExcel())
    ugg_data = getData(desired_link)
    #extract just the percentage for win rate
    win_rate = ugg_data[0].text
    matches = ugg_data[4].text
    return(openExcel().at[desired_index,'champ'] + "'s current win rate: " + win_rate + " out of " +
    matches + " matches.")

def pickRate(champion):
    desired_link = getLink(champion.capitalize(),openExcel())
    desired_index = getIndex(champion.capitalize(),openExcel())
    ugg_data = getData(desired_link)
    #extract just the percentage for win rate
    win_rate = ugg_data[2].text
    matches = ugg_data[4].text
    return(openExcel().at[desired_index,'champ'] + "'s current pick rate: " + win_rate + " out of " +
    matches + " matches.")

def banRate(champion):
    desired_link = getLink(champion.capitalize(),openExcel())
    desired_index = getIndex(champion.capitalize(),openExcel())
    ugg_data = getData(desired_link)
    #extract just the percentage for win rate
    win_rate = ugg_data[3].text
    matches = ugg_data[4].text
    return(openExcel().at[desired_index,'champ'] + "'s current ban rate: " + win_rate + " out of " + 
    matches + " matches.")