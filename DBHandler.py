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
    # functions to get database entries
