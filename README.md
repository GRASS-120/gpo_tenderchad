запуск сервиса (tender, it_search, analysis):
```
poetry shell
poetry run start
```
---

файл "GPO TenderChad.postman_collection.json" - коллекция с запросами для postman. просто нужно импортировать

---

1. нужно пофиксить работу с потоком (например после сохранения fastapi не хочет работать + не может нормально закрыть приложение) (в телеге есть)
2. настроить it_search_queue (это будет немного сложнее, так как две разные очереди. роутинг?)
3. доделать analisys service (нужно узнать у насти как должен работать)

---

+ docker-compose
+ nginx

---

1. переписать tender search чтобы искал не только по description, но и по stage и law? + он сравнивает прям буква в букву, а не как полнотекстовый поиск. исправить? (сейчас ищет обязательно по desc, обязательно по stage & law). нужно ли чем-то дополнить поиск???
2. запросы проходят медленно. это норм??? или фиксить?

