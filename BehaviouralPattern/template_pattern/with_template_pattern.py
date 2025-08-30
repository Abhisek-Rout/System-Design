from abc import ABC, abstractmethod

class DataParser(ABC):
    def parse(self):
        self.open_file()
        self.parse_file()
        self.close_file()

    def open_file(self):
        print("Open a file")

    def close_file(self):
        print("Close a file")

    @abstractmethod
    def parse_file(self):
        pass

class CsvParser(DataParser):
    def parse_file(self):
        print("Parsing CSV Data")

class JsonParser(DataParser):
    def parse_file(self):
        print("Parsing JSON Data")

class WithTempate:
    def main(self):
        json_parser: JsonParser = JsonParser()
        json_parser.parse()

        csv_parser: CsvParser = CsvParser()
        csv_parser.parse()

if __name__ == "__main__":
    obj: WithTempate = WithTempate()
    obj.main()