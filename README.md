
## Bewise Test Task
<blockquote>
1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.  

2. Реализовать на Python3 веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:  
    - В сервисе должно быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.
    - После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
    - Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
    - Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.
3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.
4. Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAalchemy,  пользоваться аннотацией типов.
</blockquote>

### Запуск проекта
1. Переименовать .env.example в .env и заполнить свои данные
2. Выполнить команду `docker-compose up web`
3. Перейти по адресу `http://127.0.0.1:8000/docs`

### Примеры запросов

1. Запрос количества вопросов в БД
```http
  GET /question/
```

| Parameter  | Type  | Description                         |
|:-----------|:------|:------------------------------------|
| `quantity` | `int` | **Required**. Quantity of questions |
  
  
2. Получение вопросов от jservice.io
```http
  POST /question?quest_num={int}
```

| Parameter   | Type     | Description                         |
|:------------|:---------|:------------------------------------|
| `quest_num` | `string` | **Required**. Quantity of questions |
  
  
3. Получение вопросов из БД
```http
  GET /question/?quest_num=1
```

| Parameter   | Type     | Description                         |
|:------------|:---------|:------------------------------------|
| `quest_num` | `string` | **Required**. Quantity of questions |