import csv

sale_tax = 18

column = {}

column_head = []

with open('product_data.csv') as product_info:
    csv_viewer = csv.reader(product_info, delimiter=',')
    line_count = 0
    for row in csv_viewer:
        if line_count == 0:
            for head in row:
                column_head.append(head)  # adds the heading
            else:
                line_count = + 1
        else:
            column[row[0]] = {
                column_head[0]: row[0],
                column_head[1]: row[1],
                'sale-tax': sale_tax,
                'final-price': int(row[1]) + int(row[1]) * (sale_tax / 100),
                column_head[2]: row[2],

            }
product_info.close()

output_list = [['Product Name', 'Cost Price', 'Sale Tax %', 'Final Price', 'Country']]

for l in column:
    output_list.append(list(column[l].values()))

with open('output1.csv', 'w') as write_info:
    data_writer = csv.writer(write_info)
    data_writer.writerows(output_list)

write_info.close()
