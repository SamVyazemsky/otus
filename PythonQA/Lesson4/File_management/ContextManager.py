class FileReader:
    def __init__(self, file_path):
        self.file = file_path

    def __enter__(self):
        self.f_obj = open(self.file, "r")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f_obj.close()

