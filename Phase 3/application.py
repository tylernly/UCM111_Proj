from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow,
QLabel, QLineEdit, QVBoxLayout, QWidget)
from PyQt6.QtCore import QSize, Qt

import sys

import sqlite3
from sqlite3 import Error
import csv

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    sql = """CREATE TABLE client(c_clientid decimal(5,0) not null, 
c_clientname char(100) not null )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE requests(r_requestid decimal(5,0) not null, 
r_requestclientId decimal(5,0) not null,
r_requestbudget decimal(10,0) )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE marketing(m_teamid decimal(5,0) not null, 
m_teamname char(100) not null)"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE project(p_projectid decimal(5,0) not null, 
p_teamId decimal(5,0) not null,
p_projectrequestId decimal(5,0) not null,
p_projectcost decimal(10,0) not null)"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE video(v_videoId decimal(5,0) not null, 
v_videoFile char(30) not null,
v_videoDuration decimal(5,0) not null,
v_videoPlatform char(20) not null,
v_videoViews decimal(15,0) not null,
v_videoLanguage char(20) not null,
v_videoCost decimal(15,0) not null,
v_videoRegionId decimal(5,0),
v_videoDemographicId decimal(5,0),
v_videoProjectId decimal(5,0) )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE region(r_regionid decimal(5,0) not null, 
r_regionName char(20) not null,
r_regionLanguage char(20) not null )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE demographic(d_demographicId decimal(5,0) not null, 
d_demographicName decimal(5,0) not null )"""
    _conn.execute(sql)
    _conn.commit()
    
    sql = """CREATE TABLE reqDemo(rd_requestId decimal(5,0) not null, 
rd_demographicId decimal(5,0) not null )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE reqRegion(rr_requestId decimal(5,0) not null, 
rr_regionId decimal(5,0) not null )"""
    _conn.execute(sql)
    _conn.commit()
    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    
    sql = "DROP TABLE IF EXISTS client"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS requests"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS marketing"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS project"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS video"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS region"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS demographic"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS reqDemo"
    _conn.execute(sql)
    _conn.commit()

    sql = "DROP TABLE IF EXISTS reqRegion"
    _conn.execute(sql)
    _conn.commit()

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    cursor = _conn.cursor()
    file = open(newdata/CSE111clients.csv)
    sql = """.mode "csv"
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
            .import  'newdata/CSE111video.csv' video"""
    _conn.execute(sql)
    _conn.commit()
    
    print("++++++++++++++++++++++++++++++++++")


class MainWindow(QMainWindow):
    def __init__(self):
        database = "tpch.sqlite"

        # create a database connection
        conn = openConnection(database)
        #with conn:
            #dropTable(conn)
            #createTable(conn)
            #populateTable(conn)

        closeConnection(conn, database)
        
        #window
        super().__init__()

        self.setWindowTitle("advertisement database")

        #creates the objects
        self.text = QLabel("1)insert 2)remove 3)update 4)run preset SQLs")
        self.button = QPushButton("Enter")
        self.input = QLineEdit()
        self.menu = QLabel("0")
        self.query = QLabel("")
        self.button.clicked.connect(self.the_button_was_clicked)

        #places all the objects into one layout
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.query)

        #container now is in the layout format
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        database = "tpch.sqlite"
        conn = openConnection(database)
        
        if(self.menu.text() == "0"):
            if(self.input.text() == "1"):
                #insert
                print("Clicked!")
                self.text.setText("inserting screen")
                print("Clicked!")
            elif(self.input.text() == "2"):
                #remove
                self.text.setText("removing screen")
            elif(self.input.text() == "3"):
                #update
                self.text.setText("updating screen")
            elif(self.input.text() == "4"):
                #run presetSQL
                self.text.setText("""1)
2)
3)
4)All regions (debug)
5)For all of the marketing teams, determine their most
--profitable regions and demographics and the clients
--who made the most requests for these. The amount of
--money made per view is different for each platform,
--$0.05 for computer, $0.12 for television ads, and 
--$0.09 for phone ads. The profit by finding the amount
--made and subtracting their cost.
e) back to main screen""")
                self.menu.setText("4");
        elif(self.menu.text() == "1"):
            self.text.setText("type the table you would like to insert into")
        elif(self.menu.text() == "2"):
            self.text.setText("type the table you would like to remove from")
        elif(self.menu.text() == "3"):
            self.text.setText("type the table you would like to update from")
        elif(self.menu.text() == "4"):
            if(self.input.text() == "1"):
                #run query
                self.query.setText("test")
            if(self.input.text() == "2"):
                #run query
                self.query.setText("test")
            if(self.input.text() == "3"):
                
                self.query.setText("test")
            if(self.input.text() == "4"):
                try:
                    sql = """SELECT * FROM region"""
                    cur = conn.cursor()
                    cur.execute(sql)
                    l = '{:>10} {:>10} {:>10}'.format("ID", "region", "language")
                    output = l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row[2])
                        print(l)
                        output = output + "\n" + l

                    self.query.setText(output)
                except Error as e:
                    conn.rollback()
                    print(e)
                
            if(self.input.text() == "5"):
                try:
                    sql = """SELECT m_teamname, mProfitTable.r_regionname, mProfitTable.d_demographicname, maxProfit, c_clientName
FROM (
        SELECT m_teamname, r_regionname, d_demographicname, MAX(profit) as maxProfit
        FROM (
                SELECT table1.m_teamname, table1.r_regionname, table1.d_demographicname,
                (compIncome+tvIncome+phoneIncome-compCost-tvCost-phoneCost) as profit
                FROM (
                        SELECT m_teamName, r_regionName, d_demographicName, (0.05 * SUM(v_videoviews)) as compIncome, SUM(v_videoCost) as compCost
                        FROM marketing, project, video, region, demographic
                        WHERE m_teamid = p_teamId
                        AND v_videoProjectId = p_projectId
                        AND v_videoRegionId = r_regionId
                        AND v_videoDemographicId = d_demographicId
                        AND v_videoPlatform = "computer"
                        GROUP BY r_regionname, d_demographicname ) as table1,
                ( SELECT m_teamname, r_regionname, d_demographicname, (0.12 * v_videoviews) as tvIncome, SUM(v_videoCost) as tvCost
                        FROM marketing, project, video, region, demographic
                        WHERE m_teamid = p_teamId
                        AND v_videoProjectId = p_projectId
                        AND v_videoRegionId = r_regionId
                        AND v_videoDemographicId = d_demographicId
                        AND v_videoPlatform = "television"
                        GROUP BY r_regionname, d_demographicname) as table2,
                ( SELECT m_teamname, r_regionname, d_demographicname, (0.09 * v_videoviews) as phoneIncome, SUM(v_videoCost) as phoneCost
                        FROM marketing, project, video, region, demographic
                        WHERE m_teamid = p_teamId
                        AND v_videoProjectId = p_projectId
                        AND v_videoRegionId = r_regionId
                        AND v_videoDemographicId = d_demographicId
                        AND v_videoPlatform = "phone"
                        GROUP BY r_regionname, d_demographicname ) as table3
                GROUP BY table1.m_teamname, table1.r_regionname, table1.d_demographicname
        )
        GROUP BY m_teamname
) as mProfitTable,
(
        SELECT c_clientName, COUNT(r_requestId), r_regionName, d_demographicName
        FROM client, requests, region, demographic, reqRegion, reqDemo
        WHERE c_clientId = r_requestClientId
        AND rr_requestId = r_requestId
        AND rr_regionId = region.r_regionId
        AND rd_requestId = r_requestId
        AND rd_demographicId = d_demographicId
        GROUP BY c_clientName, r_regionName, d_demographicName
) as mRequestedTable
WHERE mProfitTable.r_regionName = mRequestedTable.r_regionName
AND mProfitTable.d_demographicName = mRequestedTable.d_demographicName;"""
                    cur = conn.cursor()
                    cur.execute(sql)
                    l = '{:>30} {:>30} {:>30} {:>30}'.format("marketing", "most profitable region",
                                               "most profitable demographic",
                                               "desired client")
                    output = l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        print("test")
                        l = '{:>30} {:>30} {:>30} {:>30}'.format(row[0], row[1], row[2], row[3])
                        print(l)
                        output = output + "\n" + l

                        self.query.setText(output)

                except Error as e:
                    conn.rollback()
                    print(e)
                
            
            if(self.input.text() == "e"):
                self.menu.setText("0");
                self.query.setText("")
                self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs")

        self.input.setText("")
          

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
