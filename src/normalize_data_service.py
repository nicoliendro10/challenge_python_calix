import pandas as pd
import re
from unicodedata import normalize


class NormalizeDataService:
    def __init__(self):
        pass

    def normalize_headers(self, columns):
        """ Normalize the headers of the dataframe, converting all the headers to lowercase and replacing special characters """
        new_data_column = []
        for x in columns:
            x = x.lower()
            new_column = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                normalize("NFD", x), 0, re.I
            )
            new_column = normalize('NFC', new_column)
            new_data_column.append(new_column)
        return new_data_column
