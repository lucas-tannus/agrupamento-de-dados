from .file_manager import FileManager


class TextManager(FileManager):

    def __init__(self):
        super().__init__(file_extension='txt')

    def builder(self, file_name, text):
        with open(file_name, 'a') as text_file:
            text_file.write(text)
