from typing import List
import requests

# from app.schemas.order import OrderSchema
# from app.models.order import Order

#! ВРЕМЕННО
class Service:
  async def get_searched_tender(search: str, law: str | None, stage: str | None):
    res = requests.get(f'http://localhost:8001/api/v1/tender/search?search={search}&law={law}&stage={stage}')

    if res.status_code == 200:
        data = res.json()
        return data
    else:
        print(f'Ошибка запроса, код ответа: {res.status_code}')
  