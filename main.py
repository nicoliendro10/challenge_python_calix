from src.input_files_service import InputFilesService
from src.normalize_data_service import NormalizeDataService
from src.sql_service import SQLService

normalize_data_service = NormalizeDataService()
filename_path_list = []



def get_input_files(urls):
    """ Get the input files from the url and save them in the correct directory """
    input_files_service = InputFilesService()
    for url in urls:
        tree = input_files_service.get_content_tree_page(url)
        xpath_category_name = '/html/body/div[1]/div[2]/div/div/div[2]/h1/text()'
        category_name = input_files_service.get_category_name(
            tree, xpath_category_name)
        xpath_url_csv = '/html/body/div[1]/div[2]/div/div/div[3]/a[1]/@href'
        url_csv = input_files_service.get_url_csv(tree, xpath_url_csv)
        response = input_files_service.get_input_file_from_url(url_csv)
        file_name = input_files_service.create_filename_csv(
            category_name, input_files_service.get_date())
        filename_path_list.append(file_name)
        input_files_service.create_directory(file_name)
        input_files_service.save_input_file(response, file_name)


def normalize_partial_input_files():
    """ Normalize the input files """
    list_dataframes = []
    for filename_path in filename_path_list:
        df = normalize_data_service.read_csv(filename_path)
        converted_data_column = normalize_data_service.normalize_headers(
            df.columns)
        df.columns = converted_data_column
        list_dataframes.append(df)
    return list_dataframes

def get_data_by_criteria(unified_table):
    """ Get the data by criteria """
    matrix_criteria = [['categoria'], ['fuente'], ['idprovincia', 'categoria']]
    table_by_criteria = []
    for list_criteria in matrix_criteria:
        df_by_criteria = normalize_data_service.get_df_by_criteria(unified_table, list_criteria)
        table_by_criteria.append(df_by_criteria)
    normalize_data_service.normalize_dataframes(table_by_criteria)
    return normalize_data_service



if __name__ == '__main__':
    urls = ['https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d',
            'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae',
            'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7'
            ]
    get_input_files(urls)
    list_dataframes = normalize_partial_input_files()
    #First table
    unified_table = normalize_data_service.normalize_dataframes(list_dataframes)
    unified_table_setted_columns = normalize_data_service.set_columns(unified_table)
    #Second table
    data_by_criteria = get_data_by_criteria(unified_table)
    #Third table
    cine = 1
    list_criteria_cine = ['provincia', 'pantallas', 'butacas', 'espacio_incaa']
    df_cine = normalize_data_service.set_columns(list_dataframes[cine], list_criteria_cine)
