## Проект api_yatube 
 

Yatube - социальная сеть для блогеров. 
Неутентифицированным пользователям API доступен только на чтение. Исключение - эндпоинт /follow/: доступ к нему предоставляется только аутентифицированным пользователям.
В проекте использована аутентификация по JWT-токенам.
Аутентифицированным пользователям разрешено изменение и удаление своего контента.
Добавление новых пользователей через API не осуществляется.

 
### Как запустить проект: 
 

Клонировать репозиторий и перейти в него в командной строке: 

``` 
git clone https://github.com/yandex-praktikum/api_yatube.git 

``` 

``` 
cd api_yatube 
``` 

Cоздать и активировать виртуальное окружение: 
 
``` 
python -m venv venv 
``` 

``` 
source venv/Scripts/activate 
``` 

Установить зависимости из файла requirements.txt: 

``` 
python -m pip install --upgrade pip 

``` 
``` 
pip install -r requirements.txt 
``` 
 
Выполнить миграции: 

``` 
python manage.py migrate 
``` 

Запустить проект: 

``` 
python manage.py runserver 
``` 


### Примеры запросов 
 

Пример POST-запроса с токеном Антона Чехова: добавление нового поста. 


``` 
POST .../api/v1/posts/ 
``` 

``` 
{ 
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.", 
    "group": 1 
}  
``` 

Пример ответа: 
```

{ 
    "id": 14, 
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.", 
    "author": "anton", 
    "image": null, 
    "group": 1, 
    "pub_date": "2021-06-01T08:47:11.084589Z" 
} 
``` 
 

Пример POST-запроса с токеном Антона Чехова: отправляем новый комментарий к посту с id=14. 
 
``` 
POST .../api/v1/posts/14/comments/ 
``` 

``` 
{ 
    "text": "тест тест" 
}  
``` 

Пример ответа: 


``` 
{ 
    "id": 4, 
    "author": "anton", 
    "post": 14, 
    "text": "тест тест", 
    "created": "2021-06-01T10:14:51.388932Z" 
} 
``` 

Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе. 

``` 
GET .../api/v1/groups/2/ 
``` 

Пример ответа: 

``` 
{ 
    "id": 2, 
    "title": "Математика", 
    "slug": "math", 
    "description": "Посты на тему математики" 
} 

``` 

### Об авторе: 

Студент Backend-факультета, Яндекс.Практикум. Когорта №35 