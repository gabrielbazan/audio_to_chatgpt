from os import listdir
from os.path import join
from typing import List

FILE_EXTENSION_SEPARATOR = "."


class InputFile:
    def __init__(self, folder, file_name_with_extension):
        self.path: str = join(folder, file_name_with_extension)

        filename, extension = file_name_with_extension.split(FILE_EXTENSION_SEPARATOR)

        self.filename: str = filename
        self.extension: str = extension


def get_files(input_path) -> List[InputFile]:
    return [InputFile(input_path, file_name) for file_name in listdir(input_path)]
