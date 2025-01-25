import mysql.connector

class DBHandler:
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gagglemaps"
        )
        self.cursor = self.db.cursor()

    def create_room(self, building, room_number):
        query = f'INSERT INTO rooms (RoomID) VALUES (\'{building}{room_number}\')'
        try:
            self.cursor.execute(query)
            self.db.commit()
            return True
        except Exception as e:
            print(f'Error occurred while updating database in function update_room: {e}')
            self.db.rollback()
            return False


    def get_room(self, room_id):
        query = f'SELECT * FROM rooms WHERE room_id = {room_id}'
        try:
            results = self.cursor.execute(query)
        except Exception as e:
            print(f'Error occurred while querying database in function get_rooms: {e}')
            return []
        
        return results
    

    # functions to write to database
    # functions to update database entry
    def update_room(self, building, room_number, quantity):
        query = f'UPDATE rooms SET PeopleCount = {quantity} WHERE RoomID = \'{building}{str(room_number)}\''
        print(f'Attempting to execute query: {query}')
        try:
            self.cursor.execute(query)
            self.db.commit()
            print(f"{self.cursor.rowcount} record(s) affected")
            return True
        except Exception as e:
            print(f'Error occurred while updating database in function update_room: {e}')
            self.db.rollback()
            return False

    # functions to get database entries
