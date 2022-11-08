.mode "csv"
.separator ","
.headers off

            -- import data from csv file to table
.import  'data/clients.csv' client
.import  'data/marketingteam.csv' marketing
.import  'data/requests.csv' requests
.import  'data/regions.csv' region
.import  'data/demographics.csv' demographic
.import  'data/reqRegion.csv' reqRegion
.import  'data/reqDemo.csv' reqDemo
.import  'data/projects.csv' project
.import  'data/videos.csv' video