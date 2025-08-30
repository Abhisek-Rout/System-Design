from readable_file import ReadFile
from writable_file import WriteFile

class Main:
    def read_any_file(self, file: ReadFile):
        file.read()

    def main(self):
        read_file: ReadFile = ReadFile()
        read_file.read()
        
        write_file: WriteFile = WriteFile()
        write_file.read()
        write_file.write()

        self.read_any_file(read_file)
        self.read_any_file(write_file)

if __name__ == "__main__":
    main_obj = Main()
    main_obj.main()