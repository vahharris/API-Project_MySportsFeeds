# import the modules 

from ohmysportsfeedspy import MySportsFeeds
import csv
import json


 
# create a my sports feed object with api version 
msf = MySportsFeeds(version="1.2")

#  authenticate
msf.authenticate("967deecf-93c4-4410-a443-4118c9", "Temp123!")

# get 2016-2017 stats for steph curry

output = msf.msf_get_data(league='nba',season='2018-2019-regular',feed='cumulative_player_stats',format='csv',player='stephen-curry')

# print out the data
print(str(output))
# open a file to place the data in the csv file with write method
csv1= open("/Users/javarharris/Desktop/stephcurry.csv","w")

# use the csv object to write he output data to the csv file
writer = csv.writer(csv1, delimiter = ",")

#Use a for loop to write the data in the file
for line in output:
    writer.writerow((line))

#close the file so the data is saved
csv1.close()


    

