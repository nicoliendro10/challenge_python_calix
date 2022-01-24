from input_files_service import InputFilesService
from normalize_data_service import NormalizeDataService
from sql_service import SQLService

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

def normalize_input_files():
    """ Normalize the input files """
    normalize_data_service = NormalizeDataService()
    list_dataframes = []
    for filename_path in filename_path_list:
        df = normalize_data_service.read_csv(filename_path)
        converted_data_column = normalize_data_service.normalize_headers(df.columns)
        df.columns = converted_data_column
        list_dataframes.append(df)
    dataframes_joined = normalize_data_service.normalize_dataframes(list_dataframes)
    #Insert this to the database
    dataframes_with_setted_columns = normalize_data_service.set_columns(dataframes_joined)
    sql_service = SqlService()
    


if __name__ == '__main__':
    sql_service = SQLService()
    sql_service.config_credentials()
    urls = ['https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d',
            'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae',
            'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7'
            ]
    get_input_files(urls)

