#import os
#import sys

import Database
import psycopg2


INIT_STATEMENTS = [
            """ 
            CREATE TABLE IF NOT EXISTS Users 
            (
                USERID SERIAL PRIMARY KEY,
                NAME VARCHAR(40) NOT NULL,
                EMAIL VARCHAR(80) NOT NULL UNIQUE,
                PASSWORD VARCHAR(120) NOT NULL,
                REGISTERDATE VARCHAR(24)
            )
            """,
            """ 
            CREATE TABLE IF NOT EXISTS Cures
            (
                CUREID SERIAL PRIMARY KEY,
                USERID INTEGER REFERENCES Users(USERID),
                DİSEASE VARCHAR(20) NOT NULL,
                TITLE VARCHAR(100) NOT NULL,
                TEXT VARCHAR(255) NOT NULL,
                CUREDATE VARCHAR(24)
            )
            """,
            """ 
            CREATE TABLE IF NOT EXISTS Likes
            (
                LIKEID SERIAL PRIMARY KEY,
                CUREID INTEGER REFERENCES Cures(CUREID),
                WHOLIKED INTEGER REFERENCES Users(USERID),
                DATE VARCHAR(24)
            )
            """,
            """ 
            CREATE TABLE IF NOT EXISTS Comments
            (
                COMMENTID SERIAL PRIMARY KEY,
                CUREID INTEGER REFERENCES Cures(CUREID),
                USERID INTEGER REFERENCES Users(USERID),
                COMMENT VARCHAR(70) NOT NULL,
                DATE VARCHAR(24)
            )
            """,

            """ 
            CREATE TABLE IF NOT EXISTS Suggestions
            (
                SUGID SERIAL PRIMARY KEY,
                SUGGESTION VARCHAR(255)
            )
            """
            
]

def initialize(url):
    with psycopg2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = "host='localhost' dbname='nature4health' user='postgres' password='e6qEnjdzUy' port='5433'"
    initialize(url)
