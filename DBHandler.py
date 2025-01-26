import mysql.connector
import random

class DBHandler:
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gagglemaps"
        )
        self.cursor = self.db.cursor()

    def create_room(self, building_code, room_number, building_name):
        query = 'INSERT INTO rooms (RoomNumber, Building, BuildingCode) VALUES (%s, %s, %s)'
        row = (room_number, building_name, building_code)
        try:
            self.cursor.execute(query, row)
            self.db.commit()
            return True
        except Exception as e:
            print(f'Error occurred while updating database in function create_room: {e}')
            self.db.rollback()
            return False

    def get_room(self, room_id):
        query = f'SELECT * FROM rooms WHERE RoomID = \'{room_id}\''
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            results = {"RoomID": results[0][0], "RoomNumber": results[0][1], "Building": results[0][2], "BuildingCode": results[0][3], "PeopleCount": results[0][4]}
        except Exception as e:
            print(f'Error occurred while querying database in function get_room: {e}')
            return {}
        
        return results
    
    def update_room(self, building, room_number, quantity):
        query = f'UPDATE rooms SET PeopleCount = {quantity} WHERE RoomID = \'{building}{str(room_number)}\''
        try:
            self.cursor.execute(query)
            self.db.commit()
            # print(f"{self.cursor.rowcount} record(s) affected")
            return True
        except Exception as e:
            print(f'Error occurred while updating database in function update_room: {e}')
            self.db.rollback()
            return False

    def get_building_population(self, building_code):
        query = f'SELECT SUM(PeopleCount) AS count FROM rooms WHERE BuildingCode = \'{building_code}\''
        print(f'Attempting to execute query: {query}')
        results = {}
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            results = {"PeopleCount": str(results[0][0])}
            self.db.commit()
            print(f"{self.cursor.rowcount} record(s) affected")
            return results
        except Exception as e:
            print(f'Error occurred while updating database in function get_building_population: {e}')
            self.db.rollback()
            return {}

    def randomize_populations(self):
        try:
            self.cursor.execute("SELECT RoomID FROM rooms")
            room_ids = self.cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
        for room_id in room_ids:
            quantity = random.randint(10, 100)
            query = f'UPDATE rooms SET PeopleCount = {quantity} WHERE RoomID = \'{room_id[0]}\''
            try:
                self.cursor.execute(query)
                self.db.commit()
                print(f"{self.cursor.rowcount} record(s) affected")

            except Exception as e:
                print(f'Error occurred while updating database in function randomize_populations: {e}')
                self.db.rollback()
                return False
