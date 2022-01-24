from input_files_service import InputFilesService


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
        input_files_service.create_directory(file_name)
        input_files_service.save_input_file(response, file_name)


if __name__ == '__main__':
    urls = ['https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d',
            'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae',
            'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7'
            ]
    get_input_files(urls)
