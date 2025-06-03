import uvicorn
from fastapi import FastAPI
from routers.game_router import router as game_router
from fastapi.staticfiles import StaticFiles
from models.playable import Player, Card, Deck, Table
from game_services.game_service import add_hands, define_combinations

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(game_router)

#if __name__ == "__main__":
#    uvicorn.run(app, port=8000)