from datetime import datetime, timedelta
from typing import List
from beanie import Link

from app.models.tender import Tender
from app.models.federal_law import FederalLaw
from app.models.purchase_stage import PurchaseStage
from app.models.key_word import KeyWord
from app.models.technology import Technology
from app.models.supplier_definition import SupplierDefinition

async def fill_database():
    key_words: List[KeyWord] = [
        KeyWord(name="компьютеров"),
        KeyWord(name="закупка"),
        KeyWord(name="программного"),
        KeyWord(name="обеспечения"),
    ] 

    technology: List[Technology] = [
        Technology(name="reactjs"),
        Technology(name="laravel"),
        Technology(name="fastapi"),
        Technology(name="angularjs")     
    ]

    supplier_definition: SupplierDefinition = [
        SupplierDefinition(name="Аукцион"),
        SupplierDefinition(name="Конкурс"),
        SupplierDefinition(name="Запрос котировок")
    ]

    federal_laws: List[FederalLaw] = [
        FederalLaw(name="Закон о государственных закупках", law="223-ФЗ"),
        FederalLaw(name="Закон о контрактной системе в сфере закупок товаров, работ, услуг для обеспечения государственных и муниципальных нужд", law="44-ФЗ"),
    ]
    
    purchase_stages: List[PurchaseStage] = [
        PurchaseStage(stage="Подготовка закупки"),
        PurchaseStage(stage="Размещение закупки"),
        PurchaseStage(stage="Проведение закупки"),
        PurchaseStage(stage="Завершение закупки"),
    ]

    # Сохраняем документы в базу
    await FederalLaw.insert_many(federal_laws)
    await PurchaseStage.insert_many(purchase_stages)
    await SupplierDefinition.insert_many(supplier_definition)
    await Technology.insert_many(technology)
    await KeyWord.insert_many(key_words)

    law_objects = await FederalLaw.find_all().to_list()
    stage_objects = await PurchaseStage.find_all().to_list()
    supplier_definition_objects = await SupplierDefinition.find_all().to_list()
    technology_objects = await Technology.find_all().to_list()

    key_words_objects = await KeyWord.find_all().to_list()
    key_words_objects_1 = [key_words_objects[0], key_words_objects[1]]
    key_words_objects_2 = [key_words_objects[1], key_words_objects[2], key_words_objects[3]]

    # сохраняем дату без учета времени, то есть в формате 2024-06-18 00:00:00
    placement_date=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_date=(datetime.now() + timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0)
    end_date=(datetime.now() + timedelta(days=30)).replace(hour=0, minute=0, second=0, microsecond=0)

    tenders: List[Tender] = [
        Tender(
            number="1234567890",
            name="Закупка компьютеров",
            law=law_objects[0],
            purchase_stage=stage_objects[1],
            supplier_definition=supplier_definition_objects[0],
            stack_technologies=technology_objects,
            key_words=key_words_objects_1,
            platform_name="СБИС",
            customer_name="Иван Иванов",
            platform_url="url",
            price=100000,
            type="it",
            deadline=20,
            placement_date=placement_date,
            start_date=start_date,
            end_date=end_date,
        ),
        Tender(
            number="9876543210",
            name="Закупка программного обеспечения",
            law=law_objects[1],
            purchase_stage=stage_objects[2],
            supplier_definition=supplier_definition_objects[1],
            stack_technologies=technology_objects,
            key_words=key_words_objects_2,
            platform_name="СБИС",
            customer_name="Петя Петров",
            platform_url="url",
            price=200000,
            type="med",
            deadline=20,
            placement_date=placement_date,
            start_date=start_date,
            end_date=end_date,
        ),
    ]

    await Tender.insert_many(tenders)

    return {"message": "Database filled with sample data"}