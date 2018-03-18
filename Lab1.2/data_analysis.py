#!/usr/local/bin/python3

# Ищем корреляции между активностью Солнца и ухудшением отношений с США
# Данные предоставляются в виде внешнего файла MS Excel

# Подключаем библиотечные функции
from matplotlib import pyplot
from openpyxl import load_workbook

# Определяем служебную функцию выделения значения из ячейки
def getvalue(x):
    return x.value


# Извлекаем таблицу MS Excel из файла в переменную
wb = load_workbook('data_analysis_lab.xlsx')

# Извлекаем лист из таблицы
sheet = wb['Data']

# Извлекаем и преобразуем три столбца из листа
years = list(map(getvalue, sheet['A'][1:]))
relations = list(map(getvalue, sheet['B'][1:]))
activity = list(map(getvalue, sheet['C'][1:]))

# Создаём графическое представление, но пока не показываем
pyplot.plot(years, relations, label="Отношения")
pyplot.plot(years, activity, label="Активность Солнца")

# Украшаем график - добавляем надписи
pyplot.xlabel('Годы')
pyplot.ylabel('Отношения/Активность Солнца')
pyplot.legend(loc='upper left')

# Отображаем график
pyplot.show()
