from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from models.playable import Player, Table
from game_services.game_service import add_hands, define_combinations
from core.settings import templates
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    player1 = Player('Misha')
    player2 = Player('Alex')
    table = Table()
    table.deck.shuffle()
    await add_hands(table, player1, player2)

    table.add_cards(table.deck.draw(3))
    table.add_cards(table.deck.draw(1))
    table.add_cards(table.deck.draw(1))

    data1 = await define_combinations(table, player1)
    data2 = await define_combinations(table, player2)

    if data1["power"] > data2["power"]:
        return templates.TemplateResponse("base_page.html",
                                          {"request": request, "player1": player1, "player2": player2, 'table': table,
                                           'combination1': data1["name"], 'combination2':data2["name"],
                                           "winner":player1.name})
    elif data1["power"] < data2["power"]:
        return templates.TemplateResponse("base_page.html",
                                          {"request": request, "player1": player1, "player2": player2, 'table': table,
                                           'combination1': data1["name"], 'combination2': data2["name"],
                                           "winner": player2.name})
    else:
        return templates.TemplateResponse("base_page.html",
                                          {"request": request, "player1": player1, "player2": player2, 'table': table,
                                           'combination1': data1["name"], 'combination2': data2["name"],
                                           "winner": "Both"})