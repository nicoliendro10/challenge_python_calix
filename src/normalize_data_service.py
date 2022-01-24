import re
from unicodedata import normalize

import pandas as pd

COLUMNS_DATABASE = ['cod_loc', 'idprovincia', 'iddepartamento', 'categoria',
                    'provincia', 'localidad', 'nombre', 'direccion', 'cp', 'telefono', 'mail', 'web']
COLUMN = 1


class NormalizeDataService:
    def __init__(self):
        pass

    def normalize_headers(self, columns):
        """ Normalize the headers of the dataframe, converting all the headers to lowercase and replacing special characters """
        converted_data_column = []
        for column in columns:
            column = column.lower()
            column_normalized = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                normalize("NFD", column), 0, re.I
            )
            column_normalized = normalize('NFC', column_normalized)
            converted_data_column.append(column_normalized)
        return converted_data_column

    def read_csv(self, file_name):
        """ Read the csv file """
        data = pd.read_csv(file_name)
        return data

    def normalize_dataframes(self, list_dataframes):
        """ Normalize the dataframes concatenating them """
        dataframes_joined = pd.concat(list_dataframes)
        return dataframes_joined

    def set_columns(self, df):
        """ Set the default and cleaned columns. Delete the columns that are not in the database """
        df = df.drop(df.columns.difference(COLUMNS_DATABASE),
                     axis=COLUMN)
        return df
