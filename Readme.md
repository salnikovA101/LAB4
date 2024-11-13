## Автор: Сальников Александр Дмитриевич 467343
### Файл **[tests.py](/tests.py)** проверяет работоспособность 5 функций (перечисленных ниже) и выводит таблицу с результатами
## Функции:
1) RectangleArea - считает площадь прямоугольника, по двум его сторонам
 ``` def RectangleArea(a, b):
    if a >= 0 and b >= 0:
        return a * b
    else:
        return "Please enter non-negative numbers"
```
2) RectanglePerimeter - считает периметр прямоугольника, по двум его сторонам
``` def RectanglePerimeter(a, b):
    if a >= 0 and b >= 0:
        return 2 * (a + b)
    else:
        return "Please enter non-negative numbers"
```
3) SquareArea - считает площадь квадрата, по его стороне
``` def SquareArea(a):
    if a >= 0:
        return a * a
    else:
        return "Please enter non-negative number"
```
4) SquarePerimeter - считает периметр квадрата, по его стороне
``` def SquarePerimeter(a):
    if a >= 0:
        return 4 * a
    else:
        return "Please enter non-negative number"
```
5) HandshakeTask - решает известную задачу на рукопожатия, получая количество людей
``` def HandshakeTask(a):
    if (a == 0):
        return 0
    elif (a < 0):
        return "Please enter non-negative number"
    else:
        return int(a * (a - 1) / 2)
```

## Запуск:
вводим в консоль ``` python -m unittest tests.py ```

## История документа:
16ced52 (HEAD -> master) Написал код для тестов и Readme