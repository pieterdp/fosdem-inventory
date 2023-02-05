#!/usr/bin/env python3
import csv
from jinja2 import Environment, PackageLoader, select_autoescape
import pdfkit


def parse_csv(csv_reader):
    parsed = {}
    for line in csv_reader:
        if line[0] not in parsed:
            parsed[line[0]] = {
                'box': line[0],
                'destination': line[4],
                'location': line[3],
                'items': []
            }
        try:
            amount = int(line[2])
        except Exception as e:
            amount = 0
        parsed[line[0]]['items'].append({
            'name': line[1],
            'amount': amount
        })
    return parsed


def to_single_pdf(file_list):
    pdfkit.from_file(file_list, '2023/inventory.pdf')


def main():
    parsed = {}
    env = Environment(
        loader=PackageLoader('csv_to_template'),
        autoescape=select_autoescape()
    )
    template_single = env.get_template('single.html')
    template_all = env.get_template('all.html')
    with open('2023_inventory.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        parsed = parse_csv(csv_reader)

    with open('2023/inventory.html', 'w') as inventory_fh:
        inventory_fh.write(template_all.render(boxes=parsed))

    file_list = []
    for box_number, box in parsed.items():
        file_path = '2023/{0}.html'.format(box['box'])
        file_list.append(file_path)
        with open(file_path, 'w') as single_fh:
            single_fh.write(template_single.render(box=box))

    to_single_pdf(file_list)

    return 0


if __name__ == '__main__':
    exit(main())
