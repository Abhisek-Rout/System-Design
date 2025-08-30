from file import File

class ReadOnlyFile(File):
    def write(self):
        raise NotImplementedError("Can't write to a read only file.")