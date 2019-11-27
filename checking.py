import csv


class ProductInfo():
    with open('product_data.csv') as product_info:
        csv_reader = csv.reader(product_info, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {",".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[1]} is the product {row[2]} cost price is {row[3]}')
                line_count += 1
        print(f'Processed {line_count} lines.')
