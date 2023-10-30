# Задача 1 необязательная. Напишите рекурсивную программу вычисления
# арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.

# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;
# Тут может помочь библиотека re

import re
expr = '11/(2+3)-4*(2-7)'

# Через рекурсию
def calculate_formula(formula):
    # упростим выражение математически
    formula = formula.replace('--','+')
    formula = formula.replace('+-','-')
    # разобьем по знакам
    expr_list = re.split(r'([\+ | \- | \* |\/ |\( |\)])', formula)
    expr_list = [value for value in expr_list if value] # уберем пустые значения
    # сначала вычислим выражения в скобках
    if "(" in formula:
        expr_parentheses = calculate_formula(re.search('\(([^)]+)', formula).group(1))
        formula = formula.replace('(' + re.search('\(([^)]+)', formula).group(1) + ')',str(expr_parentheses))
        return calculate_formula(formula)
    # если не осталось умножения или деления просто просуммируем все значения (при суммировании знак учитывается)
    if '*' not in formula and '/' not in formula :
        return sum((map(float, re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)', formula)))) # [-+]?(?:\d+(?:\.\d*)?|\.\d+) - вещественное число, с демятичной частью
    else:
        if '*' in formula:
            if expr_list[expr_list.index('*') + 1] != '-':
                multiply = float(expr_list[expr_list.index('*') - 1]) * float(expr_list[expr_list.index('*') + 1])
                multiply_str = ''.join(expr_list[expr_list.index('*') - 1]) + '*' + (expr_list[expr_list.index('*') + 1])
            else:
                multiply = -(float(expr_list[expr_list.index('*') - 1]) * float(expr_list[expr_list.index('*') + 2]))
                multiply_str = ''.join(expr_list[expr_list.index('*') - 1]) + '*' +'-' + (expr_list[expr_list.index('*') + 2])
            formula = formula.replace(multiply_str,str(multiply))
            return calculate_formula(formula)
        if '/' in formula:
            if expr_list[expr_list.index('/') + 1] != '-':
                division = float(expr_list[expr_list.index('/') - 1]) / float(expr_list[expr_list.index('/') + 1])
                division_str = ''.join(expr_list[expr_list.index('/') - 1]) + '/' + (expr_list[expr_list.index('/') + 1])
            else:
                division = -(float(expr_list[expr_list.index('/') - 1]) / float(expr_list[expr_list.index('/') + 2]))
                division_str = ''.join(expr_list[expr_list.index('/') - 1]) + '/' + '-' + (expr_list[expr_list.index('/') + 2])
            formula = formula.replace(division_str,str(division))
            return calculate_formula(formula)

nums = calculate_formula(expr)
print(nums)

