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
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 1, 'Eat a variety of foods.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 1
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 2, 'Base your diet on plenty of foods rich in carbohydrates.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 2
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 3, 'Replace saturated with unsaturated fat.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 3
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 4, 'Enjoy plenty of fruits and vegetables.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 4
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 5, 'Reduce salt and sugar intake.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 5
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 6, 'Eat regularly, control the portion size.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 6
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 7, 'Drink plenty of fluids.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 7
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 8, 'Maintain a healthy body weight.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 8
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 9, 'Get on the move, make it a habit!'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 9
                )
            """,
            """
            INSERT INTO Suggestions(SUGID, SUGGESTION)
            SELECT 10, 'Start now! And keep changing gradually.'
            WHERE
                NOT EXISTS (
                    SELECT SUGID FROM Suggestions WHERE SUGID = 10
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
