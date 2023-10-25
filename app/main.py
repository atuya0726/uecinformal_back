from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from db import RestaurantCRUD

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/restaurant")
def read_rest():
    restaurantCRUD = RestaurantCRUD()
    result = restaurantCRUD.read_all()
    return JSONResponse(content=result, headers={"Content-Type": "application/json; charset=UTF-8"})

@app.get("/health_check")
def health_check():
    return "good"