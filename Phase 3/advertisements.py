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
    sql = """.mode "csv"
            .separator ","
            .headers off

            .import  'data/clients.csv' client
            .import  'data/marketingteam.csv' marketing
            .import  'data/requests.csv' requests
            .import  'data/regions.csv' region
            .import  'data/demographics.csv' demographic
            .import  'data/reqRegion.csv' reqRegion
            .import  'data/reqDemo.csv' reqDemo
            .import  'data/projects.csv' project
            .import  'data/videos.csv' video"""
    
    print("++++++++++++++++++++++++++++++++++")

def sql1(_conn):
    try:
        sql = """SELECT DISTINCT(region_name) 
                FROM region, client, requests, reqRegion
                WHERE client_name = 'UNIVERSAL STUDIOS'
                AND client_id = request_clientId
                AND request_id = rr_requestid
                AND rr_regionid = region_id;"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("region")
        print(l)
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def sql2(_conn):
    try:
        sql = """SELECT client_name, max(request_budget)
                FROM client, requests
                WHERE client_id = request_clientid
                AND request_budget = (SELECT max(request_budget) FROM requests)
                GROUP BY client_name;"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>20} {:>10}'.format("client", "budget")
        print(l)
        for row in rows:
            l = '{:20} {:>10}'.format(row[0])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def sql3(_conn):
    try:
        sql = """SELECT client_name, max(request_budget)
                FROM client, requests
                WHERE client_id = request_clientid
                AND request_budget = (SELECT max(request_budget) FROM requests)
                GROUP BY client_name;"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>20} {:>10}'.format("client", "budget")
        print(l)
        for row in rows:
            l = '{:20} {:>10}'.format(row[0])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def highest_view_platform(_conn):
    try:
        sql = """SELECT v_videoPlatform
                 FROM
                 (
                    SELECT v_videoPlatform, MAX(v_videoViews)
                    FROM video
                    GROUP BY v_videoPlatform
                 );"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("Platform")
        print(l)
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def num_videos_by_team_targeting_demographic(_conn, _team, _demo):
    try:
        sql = """SELECT COUNT(v_videoId)
                 FROM video, marketing, project, demographic
                 WHERE m_teamName = ?
                 AND m_teamID = p_teamId
                 AND v_videoProjectId = p_projectId
                 AND v_videoDemographicId = d_demographicId
                 AND d_demographicName = ?
                 """
        args = [_team,_demo]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>10}'.format("# of videos")
        print(l)
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def regions_not_requested_by_two_clients(_conn, _clientA, _clientB):
    try:
        sql = """SELECT r_regionName, r_regionId
                 FROM region
                 EXCLUDE
                 SELECT r_regionName, r_regionId
                 FROM region, request, reqregion, region
                 WHERE c_clientName = ?
                 AND c_clientId  = r_requestClientId
                 AND r_requestId = rr_requestId
                 AND rr_regionId = r_regionId
                 EXCLUDE
                 SELECT r_regionName, r_regionId
                 WHERE c_clientName = ?
                 AND c_clientId  = r_requestClientId
                 AND r_requestId = rr_requestId
                 AND rr_regionId = r_regionId
                 """
        args = [_clientA, _clientB]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>10} {:>10}'.format("region", "ID")
        print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0],row[1])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def shortest_video_targeting_demo(_conn, _demographic):
    try:

        sql = """SELECT v_videoId, v_videoFile, MIN(v_videoDuration)
                FROM video, demographic
                WHERE d_demographic = ?
                AND d_demographicId = v_videoDemographicId;
                """
        args = [_demographic]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>10} {:>10} {:>10}'.format("Video ID", "File name", "Duration")
        print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10}'.format(row[0],row[1],row[2])
            print(l)
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)

def new_project_with_marketing_request(_conn, _team,_request):
    try:

        #find ID
        sql = """SELECT MAX(p_projectId) FROM project"""
        cur = _conn.cursor()
        cur.execute(sql)
    
        rows = cur.fetchall()
    
        for row in rows:
            newId = row[0]+1;
        
        #find teamID
        sql = """SELECT m_teamId FROM marketing WHERE ?"""
        args = [_team]
        cur = _conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
    
        for row in rows:
            teamId = row[0]+1;
        
        sql = """INSERT INTO project(project_id, project_teamId,
                                project_requestId, project_cost) 
        VALUES (?,?,?,?);"""
        args = [newId, teamId, _request, 0]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

def total_projects_by_team(_conn, _team):
    try:
        sql = """SELECT COUNT(p_projectId)
                FROM project, marketing
                WHERE m_teamId = p_teamId
                AND m_teamName = ?
                 """
        args = [_team]
        cur = _conn.cursor()
        cur.execute(sql, args)
        l = '{:>10}'.format("Total")
        print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def demographic_with_highest_views(_conn):
    try:
        sql = """SELECT d_demographicName, MAX(total)
                FROM
                (
                    SELECT d_demographicName, SUM(v_videoViews) as total
                    FROM video, demographic
                    WHERE v_videoDemoGraphicId = d_demographicId
                    GROUP BY d_demographicId
                );
                 """
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10} {:>10}'.format("Demographic", "views")
        print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        _conn.rollback()
        print(e)

def new_reqDemo(_conn,_demographic,_request):
    try:
        sql = """SELECT d_demographicName
                 FROM demographic
                 WHERE d_demographicName = ?
                 """
        args = [_demographic]
        cur = _conn.cursor()
        cur.execute(sql, args)

        rows = cur.fetchall()

        for row in rows:
            demod = row[0]

        sql = """INSERT INTO reqDemo(rd_requestId, rd_demographicId) 
        VALUES (?,?);"""
        args = [_request, demoId]
        _conn.execute(sql, args)
        
        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

def remove_marketing_and_projects(_conn, _team):
    try:
        sql = """SELECT m_teamId
                 FROM marketing
                 WHERE m_teamName = ?
                 """
        args = [_team]
        cur = _conn.cursor()
        cur.execute(sql, args)

        rows = cur.fetchall()

        for row in rows:
            teamId = row[0]

        sql = """DELETE FROM projects WHERE p_teamId = ?"""
        sql = """DELETE FROM projects WHERE p_teamId = ? 
                """

        args = [teamId]
        _conn.execute(sql, args)
        
        _conn.commit()


       #sql = """DELETE FROM marketing WHERE m_teamName = ?"""

       #sql = """DELETE FROM marketing WHERE m_teamName = ?"""

        args = [_team]
        _conn.execute(sql, args)
        
        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)

def projects_dont_have_all_requested_regions(_conn):
    try:
        sql = """SELECT DISTINCT p_projectId
                 FROM
                 (
                     SELECT rr_regionId, p_projectId
                     FROM reqregion, project
                     WHERE rr_requestId = p_requestId
                     EXCLUDE
                     SELECT v_videoRegionId, p_projectId
                     FROM project, video
                     WHERE v_videoProjectId = p_projectId
                 );
                 """
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("projects")
        print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

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
        #populateTable(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
