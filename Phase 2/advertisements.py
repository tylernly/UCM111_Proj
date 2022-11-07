import sqlite3
from sqlite3 import Error

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

    sql = """CREATE TABLE client(client_id decimal(5,0) not null, 
                               client_name char(100) not null )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE requests(request_id decimal(5,0) not null, 
                               request_clientId decimal(5,0) not null,
                               request_budget decimal(10,0) )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE marketing(team_id decimal(5,0) not null, 
                               team_name char(100) not null)"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE project(project_id decimal(5,0) not null, 
                               project_teamId decimal(5,0) not null,
                               project_requestId decimal(5,0) not null,
                               project_cost decimal(10,0) not null )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE video(video_id decimal(5,0) not null, 
                               video_file char(15) not null,
                               video_duration decimal(5,0) not null,
                               video_platform char(20) not null,
                               video_views decimal(10,0) not null,
                               video_cost decimal(10,0) not null,
                               video_language char(20) not null,
                               video_regionId decimal(5,0),
                               video_demographicId decimal(5,0),
                               video_projectId decimal(5,0) )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE region(region_id decimal(5,0) not null, 
                               region_name char(20) not null,
                               region_language char(20) not null )"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE demographic(demographic_id decimal(5,0) not null, 
                               demographic_name decimal(5,0) not null )"""
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
    

    print("++++++++++++++++++++++++++++++++++")

def insert_client(_conn, _id, _name):
    try:
        sql = """INSERT INTO client(client_id, client_name) 
        VALUES (?,?)"""
        args = [_id, _name]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_marketing(_conn, _id, _name):
    try:
        sql = """INSERT INTO marketing(marketing_id, marketing_name) 
        VALUES (?,?)"""
        args = [_id, _name]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_requests(_conn, _id, _clientId, _budget):
    try:
        sql = """INSERT INTO requests(request_id, request_clientId, request_budget) 
        VALUES (?,?,?)"""
        args = [_id, _clientId, _budget]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_project(_conn, _id, _teamId, _requestId, _cost):
    try:
        sql = """INSERT INTO project(project_id, project_teamId,
                                project_requestId, project_cost) 
        VALUES (?,?,?,?)"""
        args = [_id, _teamId, _requestId, _cost]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_video(_conn, _id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId):
    try:
        sql = """INSERT INTO video(video_id, video_file, video_duration,
                                   video_platform, video_views, video_language,
                                   video_cost, video_regionId, video_demographicId) 
        VALUES (?,?,?,?,?,?,?,?,?)"""
        args = [_id, _file, _duration, _platform, _views,
                _language, _cost, _regionId, _demographicId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def insert_region(_conn, _id, _name, _language):
    try:
        sql = """INSERT INTO region(region_id, region_name, region_language) 
        VALUES (?,?,?)"""
        args = [_id, _name, _language]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)


def insert_demographic(_conn, _id, _name):
    try:
        sql = """INSERT INTO demographic(demographic_id, demographic_name) 
        VALUES (?,?)"""
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
        VALUES (?,?)"""
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
        VALUES (?,?)"""
        args = [_requestId, _regionId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def main():
    database = "tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTable(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
