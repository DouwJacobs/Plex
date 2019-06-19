# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:01:42 2019

@author: DouwJ
"""

from plexapi.myplex import MyPlexAccount
from random import randint


USERNAME = <Your Username>
PASSWORD = <Your Password>
SERVERNAME = <Your Servername>


PLAYLIST_NAME = <Name of new Playlist>

SERIES_NAMES = ["Friends","Brooklyn Nine-Nine",'The Big Bang Theory']


account = MyPlexAccount(USERNAME, PASSWORD)
plex = account.resource(SERVERNAME).connect()

Series_list = []
for series_name in SERIES_NAMES:
    Series_list.append(plex.library.section("TV Shows").get(series_name).episodes())

num_series = len(Series_list)

num_episodes = 0
for i in range(0,len(Series_list)):
    num_episodes = num_episodes + len(Series_list[i])
    
random_list = []

while len(random_list) != num_episodes:
    rand = randint(0,num_series-1)
    if Series_list[rand] == []:
        random_list = random_list
    else:
        random_list.append(Series_list[rand][0])
        Series_list[rand] = Series_list[rand][1:]
        
plex.createPlaylist(PLAYLIST_NAME,random_list)
    