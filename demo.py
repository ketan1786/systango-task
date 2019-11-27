import csv


class CsvWrite:
    with open('product_data.csv', mode='w') as product_info:
        fieldnames = ['Product Name', 'Cost Price', 'Country']
        product_writer = csv.DictWriter(product_info, fieldnames=fieldnames)

        product_writer.writeheader()
        product_writer.writerow({'Product Name': 'laptop', 'Cost Price': 20000, 'Country': 'India'})
        product_writer.writerow({'Product Name': 'Fridge', 'Cost Price': 500, 'Country': 'USA'})
        product_writer.writerow({'Product Name': 'washing machine', 'Cost Price': 15000, 'Country': 'India'})
        product_writer.writerow({'Product Name': 'printer', 'Cost Price': 500, 'Country': 'UK'})
