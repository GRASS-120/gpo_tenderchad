from typing import List, Optional
from beanie.operators import In, And

from app.models.tender import Tender
from app.schemas.tender import TenderGetView
from app.models.federal_law import FederalLaw
from app.schemas.law import LawGetView
from app.models.purchase_stage import PurchaseStage
from app.schemas.stage import StageGetView


class CRUD:  
    async def search_tender(search: str, law: Optional[str], stage: Optional[str]) -> List[Tender]:
        # Инициализация списка условий поиска
        conditions = [In(Tender.description, [search])]

        # print(law) -> None
        # print(law is None) -> false
        # print(type(law)) -> str......
        # print(law == "None") -> true.....................
        # python moment)))))

        # ? нужна ли проверка на существования law и stage в бд? запрос и так медленный, а тут еще +2...
        # ? это думаю зависит от такого, как пользователь вводит данные: если в ручную (почему-то), то
        # ? надо? если выбирает из списка условного, то нет

        # Добавление условий в зависимости от переданных параметров
        if law != "None":
            conditions.append(In(Tender.law.law, [law]))
        if stage != "None":
            conditions.append(In(Tender.purchase_stage.stage, [stage]))

        # Формирование запроса с использованием динамически созданного списка условий
        query = And(*conditions) if len(conditions) > 1 else conditions[0]
        
        tenders = await Tender.find(
            query,
            fetch_links=True
        ).project(TenderGetView).to_list() 

        return tenders 

    async def get_one_law(law: str) -> List[FederalLaw]:
        # ! find_one не работает! - ошибка с типом LawGetView?
        # return await FederalLaw.find_one(FederalLaw.law == law).project(LawGetView)
        return await FederalLaw.find(In(FederalLaw.law, [law]), fetch_links=True).project(LawGetView).to_list()

    
    async def get_one_stage(stage: str) -> List[PurchaseStage]:
        # ! find_one не работает! - ошибка с типом StageGetView?
        # return await PurchaseStage.find_one(PurchaseStage.stage == stage).project(StageGetView)
        return await PurchaseStage.find(In(PurchaseStage.stage, [stage]), fetch_links=True).project(StageGetView).to_list()
