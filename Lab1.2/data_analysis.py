#!/usr/local/bin/python3

import matplotlib.pyplot as pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
years = list(map(getvalue, sheet['A'][1:]))
relations = list(map(getvalue, sheet['B'][1:]))
activity = list(map(getvalue, sheet['C'][1:]))

pyplot.plot(years, relations, label="Отношения")
pyplot.plot(years, activity, label="Активность Солнца")
pyplot.xlabel('Годы')
pyplot.ylabel('Отношения/Активность Солнца')
pyplot.legend(loc='upper left')
pyplot.show()
