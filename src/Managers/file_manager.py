import os

from datetime import datetime

current_path = os.path.dirname(__file__)


class FileManager(object):

    def __init__(self, file_extension):
        self.file_extension = file_extension

    def create_file_name(self, file_name):
        now = datetime.now()
        name, extension = file_name.split('.')
        file_name = '{file_name}-{date}.{extension}'.format(
            file_name=name,
            date=now.strftime("%d-%m-%Y-%H-%M-%S"),
            extension=self.file_extension
        )
        return os.path.join(current_path, '..', 'files', 'results', file_name)

    def _build_file_name(self, file_name):
        return os.path.join(current_path, '..', 'files', file_name)
