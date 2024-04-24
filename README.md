запуск сервиса (tender & it_search):
```
poetry shell
poetry run start
```

1. подключить бд к тендеру +
2. запуск тендер сервиса +
3. test data +
4. запрос с it_search к tender +
5. docker-compose
6. nginx


1. переписать tender search чтобы искал не только по description, но и по stage и law? + он сравнивает прям буква в букву, а не как полнотекстовый поиск. исправить?
2. запросы проходят медленно. это норм??? или фиксить?


<!-- version: '3.7' -->

<!-- services:
  user_service:
    build: ./user-service
    volumes:
      - ./user-service/:/app/
    ports:
      - 8001:8000
    env_file:
      - ./user-service/app/.env
    depends_on:
      - user_db

  user_db:
    image: postgres:12.1-alpine
    volumes:
      - postgres_data_user:/var/lib/postgresql/data/
    ports:
      - 5432:5432
    env_file:
      - ./user-service/app/.env -->

  # cast_service:
  #   build: ./cast-service
  #   command: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  #   volumes:
  #     - ./cast-service/:/app/
  #   ports:
  #     - 8002:8000
  #   environment:
  #     - DATABASE_URI=postgresql://cast_db_username:cast_db_password@cast_db/cast_db_dev
  #   depends_on:
  #     - cast_db

  # cast_db:
  #   image: postgres:12.1-alpine
  #   volumes:
  #     - postgres_data_cast:/var/lib/postgresql/data/
  #   environment:
  #     - POSTGRES_USER=cast_db_username
  #     - POSTGRES_PASSWORD=cast_db_password
  #     - POSTGRES_DB=cast_db_dev

  <!-- nginx:
    image: nginx:latest
    ports:
      - "8080:8080"
    volumes:
      - ./nginx_config.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - user_service

volumes:
  postgres_data_user:
  # postgres_data_cast: -->