from django.shortcuts import render
from app.settings import INFLATION_RUSSIA_CSV
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста
    with open(INFLATION_RUSSIA_CSV, 'r', newline='', encoding='utf8') as csv_file:
        data = csv.reader(csv_file, delimiter=';')
        data_list = list(data)
    head = data_list.pop(0)
    right_data_list = []
    for row in data_list:
        new_row = []
        for cell in row[1:]:
            if cell == '':
                new_row.append('-')
            else:
                new_row.append(float(cell))
        new_row.insert(0, row[0])
        right_data_list.append(new_row)
    right_data_list.insert(0, head)

    context = {'inflation_data': right_data_list}

    return render(request, template_name,
                  context)
