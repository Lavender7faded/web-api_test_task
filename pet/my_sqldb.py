# importing required library
import mysql.connector
 
# connecting to the database
dataBase = mysql.connector.connect(
                    host ="localhost",
                    user ="root",
                    passwd ="admin",
                    database = "pet_db" ) 
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table 
petRecord = """CREATE TABLE PET (
                   PET_TYPE  VARCHAR(20) NOT NULL,
                   PET_NAME VARCHAR(50),
                   BIRTHDAY DATE,
                   HIGH INT,
                   WEIGHT INT,
                   PASSPORT_NUMBER INT
                   )"""
 
# table created
cursorObject.execute(petRecord) 
 
# disconnecting from server
dataBase.close()