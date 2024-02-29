# Установка
Требуемая версия python: 3.10+

Вы можете установить трбуемые пакеты двумя способами.  
Рекомендуемый способ установки - через [poetry](https://python-poetry.org/docs/) (1)

## Через poetry
Установка poetry  
```pip install poetry```

Установка зависимостей  
```poetry install```

Запуск приложения  
```poetry run python main.py```

## Через pip
```pip install -r requirements.txt```


# Space War
Игра про космические битвы.

Перемещение:
```
W - двигаться вперёд
S - двигаться назад
D - двигаться вправо
A - двигаться влево

SPACE - атаковать
```

## Улучшение вашего корабля
- Если количество набранных очков менее 100, количество вылетающих снарядов равно 1.
- Если количество набранных очков менее 200, количество вылетающих снарядов равно 2.
- Если количество набранных очков менее 300, количество вылетающих снарядов равно 3.

## Астероиды
У астероида 3 стадии разрушения, которые отображаются его размером. Чтобы полностью уничтожить астероид нужно попасть в него 3 раза.

## Появление противников
С увелечением количества очков увеличивается шанс появления противника.  
Если количество очков больше 80 поялвяется новый тип противников.  
Если количество очков больше 200 появляется новый тип противников.

# Приложение
Собранные бинарные файлы для Windows и Linux находятся в директории dist

---

Дополнительную информацию можно получить в файле main.pptx
