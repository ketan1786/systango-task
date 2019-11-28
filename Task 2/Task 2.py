import csv


class Logistic:
    input_file = 'product_data.csv'
    output_file = 'final_product_detail.csv'
    output_data = []

    def calculation(self, name, cost, tax, country):  # calculate the final cost for each country according to their
        # sale tax
        return cost + cost * (tax / 100)

    def output_detail(self, name, cost, tax, country):
        final_price = self.calculation
        return [name, cost, tax, final_price, country]

    def read_info(self):
        with open(self.input_file) as input_data:
            data_read = csv.reader(input_data, delimiter=",")
            next(data_read)
            for line in data_read:
                self.output_data.append(
                    self.output_detail(line[0], int(line[1]), int(line[2]), line[3])
                )  # appends the data in the list

        return self.output_data

    def write_info(self):
        default_output_heading = [['Product Name', 'Cost Price', 'Sale Tax %', 'Final Price', 'Country']]
        with open(self.output_file, "w") as output_data:
            insert = csv.writer(output_data)
            info = self.read_info()
            info.insert(0, default_output_heading)  # inserts the heading line
            insert.writerows(info)  # insert the output data


if __name__ == "__main__":
    Logistic().write_info()
