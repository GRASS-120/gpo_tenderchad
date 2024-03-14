from datetime import datetime, timedelta
from typing import List
from beanie import Link

from app.models.tender import Tender
from app.models.federal_law import FederalLaw
from app.models.purchase_stage import PurchaseStage

async def fill_database():
     # Создаём документы
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

    law_objects = await FederalLaw.find_all().to_list()
    stage_objects = await PurchaseStage.find_all().to_list()

    tenders: List[Tender] = [
        Tender(
            number="1234567890",
            description="Закупка компьютеров",
            law=law_objects[0],
            purchase_stage=stage_objects[1],
            price=100000,
            placement_date=datetime.now(),
            start_date=datetime.now() + timedelta(days=7),
            end_date=datetime.now() + timedelta(days=30),
        ),
        Tender(
            number="9876543210",
            description="Закупка программного обеспечения",
            law=law_objects[1],
            purchase_stage=stage_objects[2],
            price=200000,
            placement_date=datetime.now() - timedelta(days=7),
            start_date=datetime.now() + timedelta(days=14),
            end_date=datetime.now() + timedelta(days=42),
        ),
    ]

    await Tender.insert_many(tenders)

    return {"message": "Database filled with sample data"}
