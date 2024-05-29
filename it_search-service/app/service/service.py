import requests

class Service:
  async def get_searched_tender(
        name: str | None,
        number: str | None,
        law: str | None,
        stage: str | None,
        min_price: str | None,
        max_price: str | None,
        placement_date: str | None,
        end_date: str | None
    ):
    res = requests.get(
       f'http://localhost:8001/api/v1/tender/search?name={name}&number={number}&law={law}&stage={stage}&min_price={min_price}&max_price={max_price}&placement_date={placement_date}&end_date={end_date}'
    )

    if res.status_code == 200:
        data = res.json()
        return data
    else:
        print(f'Ошибка запроса, код ответа: {res.status_code}')
  