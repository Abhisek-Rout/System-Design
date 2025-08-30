from read_only_file import ReadOnlyFile

class Main:
    def main(self):
        file: ReadOnlyFile = ReadOnlyFile()
        file.read()
        file.write()

if __name__ == "__main__":
    main_obj: Main = Main()
    main_obj.main()