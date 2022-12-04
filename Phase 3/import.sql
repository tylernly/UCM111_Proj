.mode "csv"
.separator ","
.headers off

            -- import data from csv file to table
.import  'newdata/CSE111clients.csv' client
.import  'newdata/CSE111marketing.csv' marketing
.import  'newdata/CSE111requests.csv' requests
.import  'newdata/CSE111regions.csv' region
.import  'newdata/CSE111demographics.csv' demographic
.import  'newdata/CSE111reqRegion.csv' reqRegion
.import  'newdata/CSE111reqDemo.csv' reqDemo
.import  'newdata/CSE111projects.csv' project
.import  'newdata/CSE111video.csv' video