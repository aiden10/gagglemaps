from websocket import create_connection
import time

ws = create_connection("ws://localhost:8000/ws/RCH110")
while True:
    print("Receiving...")
    result =  ws.recv()
    print(f"Received: {result}")
    time.sleep(2)