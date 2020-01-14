import sqlite3

def returnDefibrillators():
    db_conn = sqlite3.connect('myDB.db')

    rows = db_conn.execute("SELECT * FROM Defibrillator")

    defibrillatorList = []

    for row in rows:
        defibrillatorList.append({'id' : row[0], 'lat' : row[1], 'long' : row[2], 'name' : row[3], 'description' : row[4],
                                  'problemType' : row[5], 'problemDescription' : row[6], 'photo' : row[7],})

    db_conn.close()
    return defibrillatorList


def createDefibrillator(lat, long, name, description, problemType, problemDescription, photo):
    try:
        db_conn = sqlite3.connect('myDB.db')

        db_conn.execute("INSERT INTO Defibrillator(lat, long, name, description, problemType, problemDescription, photo) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)", [lat, long, name, description, problemType, problemDescription, photo])
        db_conn.commit()

        db_conn.close()
        return '200'
    except:
        db_conn.close()
        return '500'


def createUser(username, password, userType):
    # userType could be EKABadmin, Municipality, User
    try:
        db_conn = sqlite3.connect('myDB.db')

        db_conn.execute("INSERT INTO User(username, password, userType) VALUES ( ?, ? , ?) ", [username, password, userType])
        db_conn.commit()

        db_conn.close()
        return '200'
    except:
        db_conn.close()
        return '500'


def login(username, password, userType):
    db_conn = sqlite3.connect('myDB.db')

    result = db_conn.execute("SELECT * FROM User WHERE username = ?", [username])

    if (result != None):
        for row in result:
            if (row[2] == password):
                return userType
            else:
                return 'Wrong Password'

    db_conn.close()


def updateDefibrillator(lat, long, name, description, problemType, problemDescription, photo):
    # lat and long variables are needed every single time and can't be updated
    db_conn = sqlite3.connect('myDB.db')

    try:
        if (lat == None or long == None):
            return '500'
        if (name != None):
            db_conn.execute("UPDATE Defibrillator SET name = ? WHERE lat = ? AND long = ?", [name, lat, long])
            db_conn.commit()
        if (description != None):
            db_conn.execute("UPDATE Defibrillator SET description = ? WHERE lat = ? AND long = ?", [description, lat, long])
            db_conn.commit()
        if (problemType != None):
            db_conn.execute("UPDATE Defibrillator SET problemType = ? WHERE lat = ? AND long = ?", [problemType, lat, long])
            db_conn.commit()
        if (problemDescription != None):
            db_conn.execute("UPDATE Defibrillator SET problemDescription = ? WHERE lat = ? AND long = ?", [problemDescription, lat, long])
            db_conn.commit()
        if (photo != None):
            db_conn.execute("UPDATE Defibrillator SET photo = ? WHERE lat = ? AND long = ?", [photo, lat, long])
            db_conn.commit()

        db_conn.close()
        return '200'
    except:
        db_conn.close()
        return '500'