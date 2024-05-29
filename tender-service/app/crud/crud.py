from http.client import HTTPException
from typing import List, Optional

from bson import DBRef, ObjectId

from beanie.operators import In, And, GT, LT

from app.models.tender import Tender
from app.models.key_word import KeyWord
from app.schemas.tender import TenderGetView
from app.models.federal_law import FederalLaw
from app.schemas.law import LawGetView
from app.models.purchase_stage import PurchaseStage
from app.schemas.stage import StageGetView
from app.utils.convert_date import convert_date

# ? объяснение того, почему сравнивается значение с "None"
# print(law) -> None
# print(law is None) -> false
# print(type(law)) -> str......
# print(law == "None") -> true.....................
# python moment)))))


# как сделать поиск по ключевым словам?

class CRUD:  
    async def search_tender(
            name: Optional[str],
            number: Optional[str],
            law: Optional[str],
            stage: Optional[str],
            min_price: Optional[str],
            max_price: Optional[str],
            placement_date: Optional[str],
            end_date: Optional[str],
        ) -> List[Tender]:

        # Инициализация списка условий поиска
        conditions = []

        # либо поиск по номеру, либо поиск по названию и фильтрам
        if number != "None":
            conditions.append(In(Tender.number, [number]))
        elif name != "None":
            # Разбиваем название на слова
            name_words = name.split()
            name_words_lower = [word.lower() for word in name_words]

            # Ищем ключевые слова, которые совпадают с любым из слов в названии
            key_words = await KeyWord.find(In(KeyWord.name, name_words_lower)).to_list()
            key_words_dicts = [kw.to_dict() for kw in key_words]
            # print(key_word_objects)
            key_word_ids = [kw.id for kw in key_words]
            key_word_refs = [DBRef("KeyWord", ObjectId(id)) for id in key_word_ids]

            # Добавляем условие для поиска тендеров с найденными ключевыми словами
            if key_words_dicts:
                conditions.append(In(Tender.key_words, key_word_refs))
                # conditions.append(In(Tender.name, [name]))
                # Добавление условий в зависимости от переданных параметров
                if law != "None":
                    conditions.append(In(Tender.law.law, [law]))
                if stage != "None":
                    conditions.append(In(Tender.purchase_stage.stage, [stage]))
                if min_price != "None":
                    conditions.append(GT(Tender.price, float(min_price)))
                if max_price != "None":
                    conditions.append(LT(Tender.price, float(max_price)))
                # дата приходит в формате dd.mm.yyyy, функция convert_date делает из этой строки дату формата 2024-06-18 00:00:00
                if placement_date != "None":
                    date_obj = convert_date(placement_date)
                    conditions.append(In(Tender.placement_date, [date_obj]))
                if end_date != "None":
                    date_obj = convert_date(end_date)
                    conditions.append(In(Tender.end_date, [date_obj]))

        if conditions: 
            # формирование запроса с использованием динамически созданного списка условий
            query = And(*conditions) if len(conditions) > 1 else conditions[0]

            tenders = await Tender.find(
                query,
                fetch_links=True
            ).project(TenderGetView).to_list() 
        else:
            tenders = await Tender.find(fetch_links=True).project(TenderGetView).to_list() 

        return tenders 

    async def add_tenders(tenders_data: List) -> List[TenderGetView]:
        try:
            res = await Tender.insert_many([*tenders_data])
            return res
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def get_one_law(law: str) -> LawGetView:
        return await FederalLaw.find_one(FederalLaw.law == law).project(LawGetView)

    async def get_one_stage(stage: str) -> StageGetView:
        return await PurchaseStage.find_one(PurchaseStage.stage == stage).project(StageGetView)