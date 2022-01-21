import os
from pathlib import Path

import requests
from lxml import html


class InputFilesService():
    def __init__(self):
        pass

    def get_input_file_from_url(self, url):
        response = requests.get(url)
        return response

    def save_input_file(self, response, file_name):
        with open(file_name, 'wb') as f:
            f.write(response.content)

    def get_content_tree_page(self, url):
        # Get the info page from the url
        response = requests.get(url)
        tree = html.fromstring(response.content)
        return tree

    def get_category_name(self, tree, xpath_category):
        category_name = tree.xpath(xpath_category)[0]
        return category_name

    def get_url_csv(self, tree, xpath_url_csv):
        url_csv = tree.xpath(xpath_url_csv)[0]
        return url_csv

    def get_date(self):
        import datetime
        today = datetime.date.today()
        return today

    def create_filename_csv(self, category_name, date):
        category_name = category_name.lower()
        filename = category_name + '\\' + str(date.year) + '-' + date.strftime("%B") + '\\' + category_name + '-' + str(
            date.day) + '-' + str(date.month) + '-' + str(date.year) + '.csv'
        return filename

    def create_directory(self, path_file):
        substr = path_file.split(os.sep)
        path_directory = os.sep.join(substr[:-1])
        Path(path_directory).mkdir(parents=True, exist_ok=True)
