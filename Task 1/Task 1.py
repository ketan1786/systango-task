import csv


class Logistic:
    input_file = 'book_data.csv'
    output_file = 'final book data.csv'
    sale_tax = 18
    output_data = []

    def calculation(self, name, cost, country):  # calculate the final cost for each country according to their sale tax
        final_price = cost + cost * (self.sale_tax / 100)
        return [name, cost, self.sale_tax, final_price, country]  # returns the remaining values

    def read_info(self):
        with open(self.input_file) as input_data:
            data_read = csv.reader(input_data, delimiter=",")
            next(data_read)
            for line in data_read:
                self.output_data.append(
                    self.calculation(line[0], int(line[1]), line[2]))  # appends the data in the list

        return self.output_data

    def write_info(self):
        default_output_heading = [['Product Name', 'Cost Price', 'Sale Tax %', 'Final Price', 'Country']]
        with open(self.output_file, "w") as output_data:
            insert = csv.writer(output_data)
            info = self.read_info()
            info.insert(0, default_output_heading)  # inserts the heading line
            insert.writerows(info)  # insert the output data


# def main():
#     c = Logistic()
#     c.read_info()
#     c.write_info()
if __name__ == "__main__":
    Logistic().write_info()
