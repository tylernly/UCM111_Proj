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
p_projectRequestId decimal(5,0) not null,
p_projectCost decimal(10,0) not null)"""
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
    file = open("newdata/CSE111clients.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO client(c_clientId, c_clientName) 
        VALUES (?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111marketing.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO marketing(m_teamId, m_teamName) 
        VALUES (?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111requests.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO requests(r_requestId, r_requestClientId, r_requestBudget) 
        VALUES (?,?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111regions.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO region(r_regionId, r_regionName, r_regionLanguage) 
        VALUES (?,?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111demographics.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO demographic(d_demographicId, d_demographicName) 
        VALUES (?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111reqRegion.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO reqRegion(rr_regionId, rr_requestId) 
        VALUES (?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111reqDemo.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO reqDemo(rd_requestId, rd_demographicId) 
        VALUES (?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111projects.csv")
    contents = csv.reader(file)
    sql = """INSERT INTO project(p_projectId, p_teamId,
                                p_projectRequestId, p_projectCost) 
        VALUES (?,?,?,?);"""
    cursor.executemany(sql,contents)
    file = open("newdata/CSE111video.csv", encoding="utf8")
    contents = csv.reader(file)
    sql = """INSERT INTO video(v_videoId, v_videoFile, v_videoDuration,
                                   v_videoPlatform, v_videoViews, v_videoLanguage,
                                   v_videoCost, v_videoRegionId, v_videoDemographicId,
                                   v_videoProjectId) 
        VALUES (?,?,?,?,?,?,?,?,?,?);"""
    cursor.executemany(sql,contents)
    
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
    _conn.commit()
    
    print("++++++++++++++++++++++++++++++++++")

def insert_client(_conn, _id, _name):
    print("TEST")
    try:
        sql = """INSERT INTO client(c_clientId, c_clientName) 
        VALUES (?,?);"""
        args = [_id, _name]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_marketing(_conn, _id, _name):
    print("TEST")
    try:
        sql = """INSERT INTO marketing(m_teamId, m_teamName) 
        VALUES (?,?);"""
        args = [_id, _name]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_requests(_conn, _id, _clientId, _budget):
    try:
        sql = """INSERT INTO requests(r_requestId, r_requestClientId, r_requestBudget) 
        VALUES (?,?,?);"""
        args = [_id, _clientId, _budget]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_project(_conn, _id, _teamId, _requestId, _cost):
    try:
        sql = """INSERT INTO project(p_projectId, p_teamId,
                                p_projectRequestId, p_projectCost) 
        VALUES (?,?,?,?);"""
        args = [_id, _teamId, _requestId, _cost]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_video(_conn, _id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId, _projectId):
    try:
        sql = """INSERT INTO video(v_videoId, v_videoFile, v_videoDuration,
                                   v_videoPlatform, v_videoViews, v_videoLanguage,
                                   v_videoCost, v_videoRegionId, v_videoDemographicId,
                                   v_videoProjectId) 
        VALUES (?,?,?,?,?,?,?,?,?,?);"""
        args = [_id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId, _projectId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_region(_conn, _id, _name, _language):
    try:
        sql = """INSERT INTO region(r_reigonId, r_regionName, r_regionLanguage) 
        VALUES (?,?,?);"""
        args = [_id, _name, _language]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


def insert_demographic(_conn, _id, _name):
    try:
        sql = """INSERT INTO demographic(d_demographicId, d_demographicName) 
        VALUES (?,?);"""
        args = [_id, _name]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_reqDemo(_conn, _requestId, _demographicId):
    try:
        sql = """INSERT INTO reqDemo(rd_requestId, rd_demographicId) 
        VALUES (?,?);"""
        args = [_requestId, _demographicId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_reqRegion(_conn, _requestId, _regionId):
    try:
        sql = """INSERT INTO reqRegion(rr_requestId, rr_regionId) 
        VALUES (?,?);"""
        args = [_requestId, _regionId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_client(_conn, _id, _name):
    try:
        sql = """UPDATE client SET c_clientName = ? WHERE c_clientId = ?;"""
        args = [_name,_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_marketing(_conn, _id, _name):
    try:
        sql = """UPDATE marketing SET m_teamName = ? WHERE m_teamId = ?;"""
        args = [_name, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_requests(_conn, _id, _clientId, _budget):
    try:
        sql = """UPDATE requests SET r_requestClientId = ?, r_requestBudget = ? WHERE r_requestId = ?;"""
        args = [_clientId, _budget, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_project(_conn, _id, _teamId, _requestId, _cost):
    try:
        sql = """UPDATE project SET p_teamId = ?,
                 p_projectRequestId = ?, p_projectCost = ? WHERE p_projectId = ?;"""
        args = [_teamId, _requestId, _cost, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_video(_conn, _id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId, _projectId):
    try:
        sql = """UPDATE video SET v_videoFile = ?, v_videoDuration = ?,
                                   v_videoPlatform = ?, v_videoViews = ?, v_videoLanguage = ?,
                                   v_videoCost = ?, v_videoRegionId = ?, v_videoDemographicId = ?,
                                   v_projectId = ?
                                   WHERE v_videoId = ?"""
        args = [_file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId, _projectId, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_region(_conn, _id, _name, _language):
    try:
        sql = """UPDATE region SET r_regionName = ?, r_regionLanguage = ? WHERE r_regionId = ?;"""
        args = [_name, _language, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


def update_demographic(_conn, _id, _name):
    try:
        sql = """UPDATE demographic SET d_demographicName = ? WHERE d_demographicId = ?;""" 
        args = [_name, _id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_reqRegion(_conn, _requestId, _regionId, new_requestId, new_regionId):
    try:
        sql = """UPDATE reqRegion SET rr_requestId = ?, rr_regionId = ?
        WHERE rr_requestId = ? AND rr_regionId = ?;"""
        args = [new_requestId, new_regionId, _requestId, _regionId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def update_reqDemo(_conn, _requestId, _demographicId, new_requestId, new_demographicId):
    try:
        sql = """UPDATE reqDemo SET rd_requestId = ?, rd_demographicId = ?
        WHERE rd_requestId = ? AND rd_demographicId = ?;"""
        args = [new_requestId,new_demographicId, _requestId, _demographicId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_client(_conn, _id):
    try:
        sql = """DELETE FROM client WHERE c_clientId = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_marketing(_conn, _id):
    try:
        sql = """DELETE FROM marketing WHERE m_teamId =?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_requests(_conn, _id):
    print("TEST")
    try:
        sql = """DELETE FROM requests WHERE r_requestId = ?;""" 
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_project(_conn, _id):
    try:
        sql = """DELETE FROM project WHERE p_projectId = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_video(_conn, _id):
    try:
        sql = """DELETE FROM video WHERE v_videoId = ?;""" 
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_region(_conn, _id):
    try:
        sql = """DELETE FROM region WHERE r_regionId = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


def delete_demographic(_conn, _id):
    try:
        sql = """DELETE FROM demographic WHERE d_demographicId = ?;"""
        args = [_id]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_reqDemo(_conn, _requestId, _demographicId):
    try:
        sql = """DELETE FROM reqDemo WHERE rd_requestId = ? AND rd_demographicId = ?;""" 
        args = [_requestId, _demographicId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def delete_reqRegion(_conn, _requestId, _regionId):
    try:
        sql = """DELETE FROM reqRegion WHERE rr_requestId = ? AND rr_regionId = ?;"""
        args = [_requestId, _regionId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


class MainWindow(QMainWindow):
    def __init__(self):
        database = "tpch.sqlite"

        # create a database connection
        conn = openConnection(database)
        with conn:
            dropTable(conn)
            createTable(conn)
            populateTable(conn)

        closeConnection(conn, database)
        
        #window
        super().__init__()

        self.setWindowTitle("advertisement database")

        #creates the objects
        self.text = QLabel("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        self.button = QPushButton("Enter")
        self.input = QLineEdit()
        self.menu = QLabel("0")
        self.ID = QLabel("")
        self.ID2 = QLabel("")
        self.ID3 = QLabel("")
        self.ID4 = QLabel("")
        self.name = QLabel("")
        self.money = QLabel("")
        self.number = QLabel("")
        self.number2 = QLabel("")
        self.platform = QLabel("")
        self.language = QLabel("")
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
                self.text.setText("""inserting screen, select a table to add to
                                  1)client
                                  2)marketing
                                  3)requests
                                  4)region
                                  5)demographic
                                  6)reqRegion
                                  7)reqDemo
                                  8)project
                                  9)video""")
                self.menu.setText("1")
            elif(self.input.text() == "2"):
                #remove
                self.text.setText("""deleting screen, select a table to remove from
                                  1)client
                                  2)marketing
                                  3)requests
                                  4)region
                                  5)demographic
                                  6)reqRegion
                                  7)reqDemo
                                  8)project
                                  9)video""")
                self.menu.setText("2")
            elif(self.input.text() == "3"):
                #update
                self.text.setText("""updating screen, select a table to update
                                  1)client
                                  2)marketing
                                  3)requests
                                  4)region
                                  5)demographic
                                  6)reqRegion
                                  7)reqDemo
                                  8)project
                                  9)video""")
                self.menu.setText("3")
            elif(self.input.text() == "4"):
                #run presetSQL
                self.text.setText("""1) List projects who did not cover all of the requested regions
2)Find the regions who have not been targeted by Hand Inc or Anderson Group
3)Find the top 10 client who have set the biggest request budget
4)Delete projects that have gone over budget
5)For the marketing teams who have targeted all platforms,
  determine their most profitable regions and demographics
  and the clients who made the most requests for these regions
  and demographics. The amount of money made per view is
  different for each platform, $0.05 for computer, $0.12 for
  television ads, and $0.09 for phone ads. The profit by
  finding the amount made and subtracting their cost.
e) back to main screen""")
                self.menu.setText("4");

                    #counting screen
            elif(self.input.text() == "5"):
                try:
                    output = "client: "
                    sql = "SELECT COUNT(*)FROM client"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + l;
                    sql = "SELECT COUNT(*)FROM marketing"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n marketing: " + l
                    sql = "SELECT COUNT(*)FROM requests"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n requests: " + l
                    sql = "SELECT COUNT(*)FROM region"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n region: " + l
                    sql = "SELECT COUNT(*)FROM demographic"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n demographic: " + l
                    sql = "SELECT COUNT(*)FROM reqRegion"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n reqRegion: " + l
                    sql = "SELECT COUNT(*)FROM reqDemo"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n reqDemo: " + l
                    sql = "SELECT COUNT(*)FROM project"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n project: " + l
                    sql = "SELECT COUNT(*)FROM video"
                    cur = conn.cursor()
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        output = output + "\n video" + l

                    print(output)
                    self.query.setText(output)

                except Error as e:
                    conn.rollback()
                    print(e)

            elif(self.input.text() == "6"):
                self.menu.setText("6")
                self.text.setText("""selecting screen select a table to search through
                                  1)client
                                  2)marketing
                                  3)requests
                                  4)region
                                  5)demographic
                                  61)reqRegion using requestId
                                  62)reqRegion using regionId
                                  71)reqDemo using requestId
                                  72)reqDemo using demographicId
                                  8)project
                                  9)video""")
        #select
        elif(self.menu.text() == "6"):
            self.text.setText("enter the id number of the item to look for")
            if(self.input.text() == "1"):
                self.menu.setText("61")
            elif(self.input.text() == "2"):
                self.menu.setText("62")
            elif(self.input.text() == "3"):
                self.menu.setText("63")
            elif(self.input.text() == "4"):
                self.menu.setText("64")
            elif(self.input.text() == "5"):
                self.menu.setText("65")
            elif(self.input.text() == "61"):
                self.menu.setText("661")
            elif(self.input.text() == "62"):
                self.menu.setText("662")
            elif(self.input.text() == "71"):
                self.menu.setText("671")
            elif(self.input.text() == "72"):
                self.menu.setText("672")
            elif(self.input.text() == "8"):
                self.menu.setText("68")
            elif(self.input.text() == "9"):
                self.menu.setText("69")
        elif(self.menu.text() == "61"):
            sql = "SELECT * FROM client WHERE c_clientId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10}'.format("id", "name")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10}'.format(row[0], row[1])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)                   
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "62"):
            sql = "SELECT * FROM marketing WHERE m_teamId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10}'.format("id", "name")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10}'.format(row[0], row[1])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)                   
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "63"):
            sql = "SELECT * FROM requests WHERE r_requestId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10} {:<10}'.format("request id", "client id", "budget")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10} {:<10}'.format(row[0], row[1], row[2])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "64"):
            sql = "SELECT * FROM region WHERE r_regionId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10} {:<10}'.format("id", "name", "language")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10} {:<10}'.format(row[0], row[1], row[2])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "65"):
            sql = "SELECT * FROM demographic WHERE d_demographicId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10}'.format("id", "demographic")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10}'.format(row[0], row[1])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "661"):
            sql = "SELECT * FROM reqRegion WHERE rr_requestId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10}'.format("request", "region")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10}'.format(row[0], row[1])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "662"):
            sql = "SELECT * FROM reqRegion WHERE rr_regionId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10}'.format("request", "region")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10}'.format(row[0], row[1])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "671"):
            sql = "SELECT * FROM reqDemo WHERE rd_requestId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10}'.format("request", "demopraphic")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10}'.format(row[0], row[1])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "672"):
            sql = "SELECT * FROM reqDemo WHERE rd_demographicId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10}'.format("request", "demopraphic")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10}'.format(row[0], row[1])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "68"):
            sql = "SELECT * FROM project WHERE p_projectId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10} {:<10} {:<10}'.format("ID", "marketing team",
                                                         "request ID", "cost")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10} {:<10} {:<10}'.format(row[0], row[1], row[2], row[3])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
        elif(self.menu.text() == "69"):
            sql = "SELECT * FROM video WHERE v_videoId = ?"
            try:
                cur = conn.cursor()
                self.ID.setText(self.input.text())
                args = [self.ID.text()]
                cur.execute(sql, args)
                l = '{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format("ID",
                                                        "file", "duration", "platform", "views",
                                                        "language", "cost", "region", "demographic", "project")
                output = l
                print(l)
                rows = cur.fetchall()
                for row in rows:
                    l = '{:<10} {:<10} {:<10} {:<10} {:<10}{:<10} {:<10} {:<10} {:<10} {:<10}'.format(row[0],
                                                        row[1], row[2], row[3], row[4], row[5], row[6],
                                                        row[7], row[8], row[9])
                    print(l)
                    output = output + "\n" + l
                self.query.setText(output)           
            except Error as e:
                conn.rollback()
                print(e)
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
                
        #inserting screen
        elif(self.menu.text() == "1"):
            if(self.input.text() == "1"):
                self.menu.setText("11")
                self.text.setText("enter the ID number of the new client")
            elif(self.input.text() == "2"):
                self.menu.setText("12")
                self.text.setText("enter the ID number of the new marketing team")
            elif(self.input.text() == "3"):
                self.menu.setText("13")
                self.text.setText("enter the ID number of the new request")
            elif(self.input.text() == "4"):
                self.menu.setText("14")
                self.text.setText("enter the ID number of the new region")
            elif(self.input.text() == "5"):
                self.menu.setText("15")
                self.text.setText("enter the ID number the demographic")
            elif(self.input.text() == "6"):
                self.menu.setText("16")
                self.text.setText("enter the request ID")
            elif(self.input.text() == "7"):
                self.menu.setText("17")
                self.text.setText("enter the request ID")
            elif(self.input.text() == "8"):
                self.menu.setText("18")
                self.text.setText("enter the ID number of the new project")
            elif(self.input.text() == "9"):
                self.menu.setText("19")
                self.text.setText("enter the ID number of the video")

        #insert client
        elif(self.menu.text() == "11"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the client")
            self.menu.setText("111")

        elif(self.menu.text() == "111"):
            self.name.setText(self.input.text())
            insert_client(conn,self.ID.text(),self.name.text())
            self.query.setText("added client")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
            

        #insert marketing
        elif(self.menu.text() == "12"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the marketing team")
            self.menu.setText("121")

        elif(self.menu.text() == "121"):
            self.name.setText(self.input.text())
            insert_marketing(conn,self.ID.text(),self.name.text())
            self.query.setText("added marketing team")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #insert request
        elif(self.menu.text() == "13"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the client ID of the request")
            self.menu.setText("131")

        elif(self.menu.text() == "131"):
            self.ID2.setText(self.input.text())
            self.text.setText("enter the budget of the request")
            self.menu.setText("132")
            
        elif(self.menu.text() == "132"):
            self.money.setText(self.input.text())
            insert_requests(conn,self.ID.text(),self.ID2.text(),self.money.text())
            self.query.setText("added request")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #insert project
        elif(self.menu.text() == "18"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the ID of the marketing team")
            self.menu.setText("181")

        elif(self.menu.text() == "181"):
            self.ID2.setText(self.input.text())
            self.text.setText("enter the ID of the request")
            self.menu.setText("182")

        elif(self.menu.text() == "182"):
            self.ID3.setText(self.input.text())
            self.text.setText("enter the cost of the project")
            self.menu.setText("183")

        elif(self.menu.text() == "183"):
            self.money.setText(self.input.text())
            insert_project(conn,self.ID.text(),self.ID2.text(),self.ID3.text(),self.money.text())
            self.query.setText("added project")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #insert video
        elif(self.menu.text() == "19"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the video file name")
            self.menu.setText("191")

        elif(self.menu.text() == "191"):
            self.name.setText(self.input.text())
            self.text.setText("enter the duration")
            self.menu.setText("192")

        elif(self.menu.text() == "192"):
            self.number.setText(self.input.text())
            self.text.setText("enter the platform name")
            self.menu.setText("193")

        elif(self.menu.text() == "193"):
            self.platform.setText(self.input.text())
            self.text.setText("enter the number of views the video got")
            self.menu.setText("194")

        elif(self.menu.text() == "194"):
            self.number2.setText(self.input.text())
            self.text.setText("enter the language")
            self.menu.setText("195")

        elif(self.menu.text() == "195"):
            self.language.setText(self.input.text())
            self.text.setText("enter the cost")
            self.menu.setText("196")

        elif(self.menu.text() == "196"):
            self.money.setText(self.input.text())
            self.text.setText("enter the region ID")
            self.menu.setText("197")

        elif(self.menu.text() == "197"):
            self.ID2.setText(self.input.text())
            self.text.setText("enter the demographic ID")
            self.menu.setText("198")

        elif(self.menu.text() == "198"):
            self.ID3.setText(self.input.text())
            self.text.setText("enter the project ID")
            self.menu.setText("199")

        elif(self.menu.text() == "199"):
            self.ID4.setText(self.input.text())
            insert_video(conn,self.ID.text(),self.name.text(),
                           self.number.text(),self.platform.text(),
                           self.number2.text(),self.language.text(),
                           self.money.text(),self.ID2.text(),
                           self.ID3.text(),self.ID4.text())
            self.query.setText("added video")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #insert region
        elif(self.menu.text() == "14"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the region")
            self.menu.setText("141")

        elif(self.menu.text() == "141"):
            self.name.setText(self.input.text())
            self.text.setText("enter the language of the region")
            self.menu.setText("142")

        elif(self.menu.text() == "142"):
            self.language.setText(self.input.text())
            insert_region(conn,self.ID.text(),self.name.text(),self.language.text())
            self.query.setText("added region")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #insert demographic
        elif(self.menu.text() == "15"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the demographic")
            self.menu.setText("151")
        elif(self.menu.text() == "151"):
            self.name.setText(self.input.text())
            insert_demographic(conn,self.ID.text(),self.name.text())
            self.query.setText("added demographic")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #insert reqDemo
        elif(self.menu.text() == "17"):
            self.ID.setText(self.input.text())
            self.text.setText("enter ID of the demographic")
            self.menu.setText("171")
        elif(self.menu.text() == "171"):
            self.ID2.setText(self.input.text())
            insert_reqDemo(conn,self.ID.text(),self.ID2.text())
            self.query.setText("added request/demographic")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #insert reqRegion
        elif(self.menu.text() == "16"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the ID of the Region")
            self.menu.setText("161")
        elif(self.menu.text() == "161"):
            self.ID2.setText(self.input.text())
            insert_reqRegion(conn,self.ID.text(),self.ID2.text())
            self.query.setText("added request/region")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #delete screen
        elif(self.menu.text() == "2"):
            if(self.input.text() == "1"):
                self.menu.setText("21")
                self.text.setText("enter the ID number of the client to delete")
            elif(self.input.text() == "2"):
                self.menu.setText("22")
                self.text.setText("enter the ID number of the marketing team to delete")
            elif(self.input.text() == "3"):
                self.menu.setText("23")
                self.text.setText("enter the ID number of the request to delete")
            elif(self.input.text() == "4"):
                self.menu.setText("24")
                self.text.setText("enter the ID number of the region to delete")
            elif(self.input.text() == "5"):
                self.menu.setText("25")
                self.text.setText("enter the ID number of the demographic to delete")
            elif(self.input.text() == "6"):
                self.menu.setText("26")
                self.text.setText("enter the request ID of the request/region")
            elif(self.input.text() == "7"):
                self.menu.setText("27")
                self.text.setText("enter the request ID of the request/demographic")
            elif(self.input.text() == "8"):
                self.menu.setText("28")
                self.text.setText("enter the ID number of the project to delete")
            elif(self.input.text() == "9"):
                self.menu.setText("29")
                self.text.setText("enter the ID number of the video to delete")
        #delete client
        elif(self.menu.text() == "21"):
            self.ID.setText(self.input.text())
            delete_client(conn,self.ID.text())
            self.query.setText("deleted client")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #delete marketing
        elif(self.menu.text() == "22"):
            self.ID.setText(self.input.text())
            delete_marketing(conn,self.ID.text())
            self.query.setText("deleted marketing")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #delete requests
        elif(self.menu.text() == "23"):
            self.ID.setText(self.input.text())
            delete_requests(conn,self.ID.text())
            self.query.setText("deleted request")
            print("END")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #delete region
        elif(self.menu.text() == "24"):
            self.ID.setText(self.input.text())
            delete_region(conn,self.ID.text())
            self.query.setText("deleted region")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #delete demographic
        elif(self.menu.text() == "25"):
            self.ID.setText(self.input.text())
            delete_demographic(conn,self.ID.text())
            self.query.setText("deleted demographic")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
                                
        #delete reqRegion
        elif(self.menu.text() == "26"):
            self.ID.setText(self.input.text())
            self.menu.setText("261")
        elif(self.menu.text() == "261"):
            self.ID2.setText(self.input.text())
            delete_reqRegion(conn,self.ID.text(),self.ID2.text())
            self.query.setText("deleted request/region")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #delete reqDemographic
        elif(self.menu.text() == "27"):
            self.ID.setText(self.input.text())
            self.menu.setText("271")
        elif(self.menu.text() == "271"):
            self.ID2.setText(self.input.text())
            delete_reqDemo(conn,self.ID.text(),self.ID2.text())
            self.query.setText("deleted request/demographic")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")               

        #delete project
        elif(self.menu.text() == "28"):
            self.ID.setText(self.input.text())
            delete_project(conn,self.ID.text())
            self.query.setText("deleted project")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
                                
        #delete video
        elif(self.menu.text() == "29"):
            self.ID.setText(self.input.text())
            delete_video(conn,self.ID.text())
            self.query.setText("deleted project")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
                                
        
        #updating screen
        elif(self.menu.text() == "3"):
            if(self.input.text() == "1"):
                self.menu.setText("31")
                self.text.setText("enter the ID number of the client to update")
            elif(self.input.text() == "2"):
                self.menu.setText("32")
                self.text.setText("enter the ID number of the marketing team to update")
            elif(self.input.text() == "3"):
                self.menu.setText("33")
                self.text.setText("enter the ID number of the request to update")
            elif(self.input.text() == "4"):
                self.menu.setText("34")
                self.text.setText("enter the ID number of the region to update")
            elif(self.input.text() == "5"):
                self.menu.setText("35")
                self.text.setText("enter the ID number the demographic to update")
            elif(self.input.text() == "6"):
                self.menu.setText("36")
                self.text.setText("enter the request ID")
            elif(self.input.text() == "7"):
                self.menu.setText("37")
                self.text.setText("enter the request ID")
            elif(self.input.text() == "8"):
                self.menu.setText("38")
                self.text.setText("enter the ID number of the new project")
            elif(self.input.text() == "9"):
                self.menu.setText("39")
                self.text.setText("enter the ID number of the video")

        #update client
        elif(self.menu.text() == "31"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the client")
            self.menu.setText("311")

        elif(self.menu.text() == "311"):
            self.name.setText(self.input.text())
            update_client(conn,self.ID.text(),self.name.text())
            self.query.setText("updated client")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
            

        #update marketing
        elif(self.menu.text() == "32"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the marketing team")
            self.menu.setText("321")

        elif(self.menu.text() == "321"):
            self.name.setText(self.input.text())
            update_marketing(conn,self.ID.text(),self.name.text())
            self.query.setText("updated marketing team")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #update request
        elif(self.menu.text() == "33"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the client ID of the request")
            self.menu.setText("331")

        elif(self.menu.text() == "331"):
            self.ID2.setText(self.input.text())
            self.text.setText("enter the budget of the request")
            self.menu.setText("332")
            
        elif(self.menu.text() == "332"):
            self.money.setText(self.input.text())
            update_requests(conn,self.ID.text(),self.ID2.text(),self.money.text())
            self.query.setText("updated request")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #update project
        elif(self.menu.text() == "38"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the ID of the marketing team")
            self.menu.setText("381")

        elif(self.menu.text() == "381"):
            self.ID2.setText(self.input.text())
            self.text.setText("enter the ID of the request")
            self.menu.setText("382")

        elif(self.menu.text() == "382"):
            self.ID3.setText(self.input.text())
            self.text.setText("enter the cost of the project")
            self.menu.setText("383")

        elif(self.menu.text() == "383"):
            self.money.setText(self.input.text())
            update_project(conn,self.ID.text(),self.ID2.text(),self.ID3.text(),self.money.text())
            self.query.setText("updated project")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #update video
        elif(self.menu.text() == "39"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the video file name")
            self.menu.setText("391")

        elif(self.menu.text() == "391"):
            self.name.setText(self.input.text())
            self.text.setText("enter the duration")
            self.menu.setText("392")

        elif(self.menu.text() == "392"):
            self.number.setText(self.input.text())
            self.text.setText("enter the platform name")
            self.menu.setText("393")

        elif(self.menu.text() == "393"):
            self.platform.setText(self.input.text())
            self.text.setText("enter the number of views the video got")
            self.menu.setText("394")

        elif(self.menu.text() == "394"):
            self.number2.setText(self.input.text())
            self.text.setText("enter the language")
            self.menu.setText("395")

        elif(self.menu.text() == "395"):
            self.language.setText(self.input.text())
            self.text.setText("enter the cost")
            self.menu.setText("396")

        elif(self.menu.text() == "396"):
            self.money.setText(self.input.text())
            self.text.setText("enter the region ID")
            self.menu.setText("397")

        elif(self.menu.text() == "397"):
            self.ID2.setText(self.input.text())
            self.text.setText("enter the demographic ID")
            self.menu.setText("398")

        elif(self.menu.text() == "398"):
            self.ID3.setText(self.input.text())
            self.text.setText("enter the project ID")
            self.menu.setText("399")

        elif(self.menu.text() == "399"):
            self.ID4.setText(self.input.text())
            updated_video(conn,self.ID.text(),self.name.text(),
                           self.number.text(),self.platform.text(),
                           self.number2.text(),self.language.text(),
                           self.money.text(),self.ID2.text(),
                           self.ID3.text(),self.ID4.text())
            self.query.setText("updated video")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #update region
        elif(self.menu.text() == "34"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the region")
            self.menu.setText("341")

        elif(self.menu.text() == "341"):
            self.name.setText(self.input.text())
            self.text.setText("enter the language of the region")
            self.menu.setText("342")

        elif(self.menu.text() == "342"):
            self.language.setText(self.input.text())
            update_region(conn,self.ID.text(),self.name.text(),self.language.text())
            self.query.setText("updated region")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #update demographic
        elif(self.menu.text() == "35"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the name of the demographic")
            self.menu.setText("351")
        elif(self.menu.text() == "351"):
            self.name.setText(self.input.text())
            update_demographic(conn,self.ID.text(),self.name.text())
            self.query.setText("updated demographic")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #update reqDemo
        elif(self.menu.text() == "37"):
            self.ID.setText(self.input.text())
            self.text.setText("enter ID of the demographic")
            self.menu.setText("371")
        elif(self.menu.text() == "371"):
            self.ID2.setText(self.input.text())
            self.text.setText("enter new request ID")
            self.menu.setText("372")
        elif(self.menu.text() == "372"):
            self.ID3.setText(self.input.text())
            self.text.setText("enter new demographic region ID")
            self.menu.setText("373")
        elif(self.menu.text() == "373"):
            self.ID4.setText(self.input.text())
            update_reqDemo(conn,self.ID.text(),self.ID2.text(),self.ID3.text(),self.ID4.text())
            self.query.setText("updated request/demographic")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")

        #update reqRegion
        elif(self.menu.text() == "36"):
            self.ID.setText(self.input.text())
            self.text.setText("enter the ID of the Region")
            self.menu.setText("361")
        elif(self.menu.text() == "361"):
            self.ID.setText(self.input.text())
            self.text.setText("enter new request ID")
            self.menu.setText("362")
        elif(self.menu.text() == "362"):
            self.ID.setText(self.input.text())
            self.text.setText("enter new region ID")
            self.menu.setText("363")
        elif(self.menu.text() == "363"):
            self.ID2.setText(self.input.text())
            update_reqRegion(conn,self.ID.text(),self.ID2.text(),self.ID3.text(),self.ID4.text())
            self.query.setText("updated request/region")
            self.menu.setText("0")
            self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")



        #preset query screen
        elif(self.menu.text() == "4"):
            if(self.input.text() == "1"):
                try:
                    sql = """SELECT DISTINCT p1.p_projectid, m_teamName
FROM marketing, project as p1,
(
    SELECT rr_regionId, p_projectid
    FROM reqRegion, project
    WHERE rr_requestId = p_projectrequestId
    EXCEPT
    SELECT v_videoregionId, p_projectid
    FROM project, video
    WHERE v_videoprojectId = p_projectid
    ORDER BY p_projectid ASC
) as incomplete
WHERE m_teamID = p1.p_projectid
AND p1.p_projectid = incomplete.p_projectId;"""
                    cur = conn.cursor()
                    cur.execute(sql)
                    l = '{:<30} {:<30}'.format("project id", "marketing team")
                    output = l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<30} {:<30}'.format(row[0], row[1])
                        print(l)
                        output = output + "\n" + l

                    self.query.setText(output)
                                    
                except Error as e:
                    conn.rollback()
                    print(e)

            if(self.input.text() == "2"):
                try:
                    sql = """SELECT DISTINCT(r_regionName)
FROM region
WHERE r_regionId not in (SELECT r_regionId 
                         FROM region, client, requests, reqregion
                         WHERE c_clientname = "Hand Inc"
                         AND r_requestid = rr_requestId
                         AND rr_regionId = r_regionId
                         AND c_clientId = r_requestclientId
                         UNION
                         SELECT r_regionId 
                         FROM region, client, requests, reqregion
                         WHERE c_clientname = "Anderson Group"
                         AND r_requestid = rr_requestId
                         AND rr_regionId = r_regionId
                         AND c_clientId = r_requestclientId);"""
                    cur = conn.cursor()
                    cur.execute(sql)
                    l = '{:<30}'.format("regions not targeted")
                    output = l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<30}'.format(row[0])
                        print(l)
                        output = output + "\n" + l

                    self.query.setText(output)
                                    
                except Error as e:
                    conn.rollback()
                    print(e)
                    


            if(self.input.text() == "3"):
                try:
                    sql = """SELECT c_clientname, max(r_requestbudget) as bestBudget
FROM client, requests
WHERE c_clientid = r_requestclientid
GROUP BY c_clientname
ORDER BY bestBudget DESC
LIMIT 10;"""
                    cur = conn.cursor()
                    cur.execute(sql)
                    l = '{:<30} {:<30}'.format("client name", "biggest budget")
                    output = l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<30} {:<30}'.format(row[0], row[1])
                        print(l)
                        output = output + "\n" + l

                    self.query.setText(output)

                except Error as e:
                    conn.rollback()
                    print(e)
                    
            if(self.input.text() == "4"):
                try:
                    sql = """SELECT COUNT(p_projectId)
FROM project"""
                    cur = conn.cursor()
                    cur.execute(sql)
                    l = '{:<10}'.format("Count of remaining")
                    output = "BEFORE \n " + l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
                        print(l)
                        output = output + "\n" + l

                    self.query.setText(output)
                    
                    sql = """DELETE FROM project
WHERE p_projectid in (SELECT p_projectid
FROM project, requests
WHERE p_projectcost > r_requestbudget
AND p_projectrequestId = r_requestId)"""
                    conn.execute(sql)
                    conn.commit()

                    output = output + "\n Removed projects with cost over budget";

                    sql = """SELECT COUNT(p_projectId)
FROM project"""
                    cur = conn.cursor()
                    cur.execute(sql)
                    l = '{:<10}'.format("Count of remaining")
                    output = output + "\n AFTER \n" + l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<10}'.format(row[0])
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
                    l = '{:<30} {:<30} {:<30} {:<30}'.format("marketing", "most profitable region",
                                               "most profitable demographic", "profit",
                                               "desired client")
                    output = l
                    print(l)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:<30} {:<30} {:<30} {:<30}'.format(row[0], row[1], row[2], row[3], row[4])
                        print(l)
                        output = output + "\n" + l

                        self.query.setText(output)

                except Error as e:
                    conn.rollback()
                    print(e)
                
            
            if(self.input.text() == "e"):
                self.menu.setText("0")
                self.query.setText("")
                self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs 5)count 6)search")
            

        self.input.setText("")
          

app = QApplication(sys.argv)

window = MainWindow()
window.setFixedHeight(750)
window.setFixedWidth(1000)
window.show()

app.exec()
