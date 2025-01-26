from DBHandler import DBHandler
import time
db = DBHandler()

while True:
    db.randomize_populations()
    time.sleep(5)