from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from DBHandler import DBHandler

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

