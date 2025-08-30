class CsvParser:
    def parse(self):
        self.open_file()
        print("Parsing a CSV file")
        self.close_file()

    def open_file(self):
        print("Opening file")

    def close_file(self):
        print("Closing file")

class JsonParser:
    def parse(self):
        self.open_file()
        print("Parsing a JSON file")
        self.close_file()

    def open_file(self):
        print("Opening file")

    def close_file(self):
        print("Closing file")


class WithoutTemplate:
    def main(self):
        csv_parser: CsvParser = CsvParser()
        csv_parser.parse()

        json_parser: JsonParser = JsonParser()
        json_parser.parse()


if __name__ == "__main__":
    obj: WithoutTemplate = WithoutTemplate()
    obj.main()
