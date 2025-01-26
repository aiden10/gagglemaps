from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from DBHandler import DBHandler
from tracking import main
import uvicorn
import cv2
import threading
import io
from starlette.responses import StreamingResponse

class ImageContainer():
    def __init__(self):
        self.image = {}

image_container = ImageContainer()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with the frontend url/domain after
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DBHandler()

@app.get("/rooms/{room_id}")
async def get_room(room_id):
    results = {}
    try:
        results = db.get_room(room_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Something went wrong: {e}')
    
    return JSONResponse(content={'results': results}, status_code=200)

@app.get("/buildings/{building_code}")
async def get_building_population(building_code):
    results = {}
    try:
        results = db.get_building_population(building_code)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Something went wrong: {e}')
    
    return JSONResponse(content={'results': results}, status_code=200)

@app.get("/feed/{room_id}")
async def get_image(room_id):
    print(f'{room_id} in {image_container.image.keys()}')
    if room_id in image_container.image:
        image = image_container.image[room_id]
        res, im_png = cv2.imencode(".png", image)
        return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
    
    return JSONResponse(content={'results': 'image not in image_container'}, status_code=200)

def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == '__main__':
    threading.Thread(target=start_server, daemon=True).start()
    main('110', 'RCH', image_container)
