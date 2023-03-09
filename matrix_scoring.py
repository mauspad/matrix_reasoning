# -*- coding: utf-8 -*-
"""
justin fixed my shit :3

mar 1 2023

@author: mauspad
"""
print("This script loops over every csv in the data directory. IF YOU GET AN ERROR, CHECK TO SEE IF THE CSV IS BUGGED")

#import packages
import pandas as pd
import glob

#set directory
path = "data/*.csv"
for fname in glob.glob(path):

	# turn csv into dataframe
	df = pd.read_csv(fname)

	# set up some variables
	corrans =["A5_2","A3_2","A4_2","A4_2","A1_2","A5_2","A2_2","A1_2","A5_2","A1_2","A3_2","A5_2","A2_2","A3_2","A1_2","A4_2","A2_2","A1_2","A5_2","A4_2","A2_2","A3_2","A4_2"]

	Score = 0

	key_resp = df["mouse_trials.clicked_name"].tolist() # list of responses

	# loop!
	for i in range(1,len(key_resp)):
		if key_resp[i]==corrans[i-1]:
			Score+=1
	print(fname)
	print(Score)