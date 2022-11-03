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

    sql = """CREATE TABLE client(clientId decimal(5,0) not null, 
                               clientName char(100) not null"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE requests(requestId decimal(5,0) not null, 
                               requestClientId decimal(5,0) not null,
                               requestBudget decimal(10,0)"""
    _conn.execute(sql)
    _conn.commit()

    sql = """CREATE TABLE client(clientId decimal(3,0) not null, 
                               clientName char(100) not null"""
    _conn.execute(sql)
    _conn.commit()
        
    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    
    sql = "DROP TABLE IF EXISTS warehouse"
    _conn.execute(sql)
    _conn.commit()

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    

    print("++++++++++++++++++++++++++++++++++")

def insert_warehouse(_conn, _warehousekey, _name, _capacity, _suppkey, _nationkey):
    try:
        sql = """INSERT INTO warehouse(w_warehousekey,
        w_name, w_capacity, w_suppkey, w_nationkey) 
        VALUES (?,?,?,?,?)"""
        args = [_warehousekey, _name, _capacity, _suppkey, _nationkey]
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
