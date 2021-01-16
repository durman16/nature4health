import psycopg2

url = "host='localhost' dbname='nature4health' user='postgres' password='e6qEnjdzUy' port='5433'"

#statement = "SELECT * FROM Suggestions;"

#cursor.execute("CREATE TABLE IF NOT EXISTS Suggestions(SUGID SERIAL PRIMARY KEY,SUGGESTION VARCHAR(255));")

#cursor.execute("INSERT INTO Suggestions(SUGGESTION) VALUES(%s)", ("Bir takim suggestions.",))

# cursor.execute(statement)

# print(cursor.fetchall())


class Userdb:
    def Check_email(self, email):
        with psycopg2.connect(url) as connection:
            with connection.cursor() as cursor:
                statement = """Select email FROM Users Where email=%s;"""
                cursor.execute(statement, ([email]))
                cursor_list = cursor.fetchall()
                len_c = len(cursor_list)
                if len_c > 0:
                    return False
                else:
                    return True

    def User_Add(self, name, email, password):
        with psycopg2.connect(url) as connection:
            with connection.cursor() as cursor:
                statement = """INSERT INTO Users(name,email,password) VALUES(%s,%s,%s);"""
                cursor.execute(statement, ([name, email, password]))

    

class Curedb:
    def __init__(self):
        self.cures = {}
        self.last_cure_key = 0

    def add_cure(self, cure):
        self.last_cure_key += 1
        self.cures[self.last_cure_key] = cure
        return self.last_cure_key

    def delete_cure(self, cure_key):
        if cure_key in self.cures:
            del self.cures[cure_key]

    def get_cure(self, cure_key):
        cure = self.cures.get(cure_key)
        if cure is None:
            return None
        cure_ = Cures(cures.title, disease=cures.disease)
        return cure_

    def get_cures(self):
        cures = []
        for cure_key, cure in self.cures.items():
            cure_ = Cures(cure.title, disease=cure.disease)
            cures.append((cure_key, cure_))
        return cures
