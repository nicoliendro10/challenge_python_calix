import os
from pathlib import Path
import logging

import requests
from lxml import html


class InputFilesService():
    """ This class is used to download the input files from the url and save them in the correct directory """

    def __init__(self):
        pass

    def get_input_file_from_url(self, url):
        """ Get the response from the url """
        try:
            response = requests.get(url)
            return response
        except Exception as e:
            logging.error("Error getting the response from the url: " + str(e))
            raise e

    def save_input_file(self, response, file_name):
        """ Read the content of the response and ave the input file in the correct directory """
        with open(file_name, 'wb') as f:
            f.write(response.content)

    def get_content_tree_page(self, url):
        """ Get the content of the page """
        response = requests.get(url)
        tree = html.fromstring(response.content)
        return tree

    def get_category_name(self, tree, xpath_category):
        """ Get the category name """
        category_name = tree.xpath(xpath_category)[0]
        return category_name

    def get_url_csv(self, tree, xpath_url_csv):
        """ Get the url of the csv file """
        url_csv = tree.xpath(xpath_url_csv)[0]
        return url_csv

    def get_date(self):
        """ Get today's date """
        import datetime
        today = datetime.date.today()
        return today

    def create_filename_csv(self, category_name, date):
        """ Create the filename of the csv file using the category name and the today's date """
        category_name = category_name.lower()
        filename = 'output' + '\\' + category_name + '\\' + str(date.year) + '-' + date.strftime("%B") + '\\' + category_name + '-' + str(
            date.day) + '-' + str(date.month) + '-' + str(date.year) + '.csv'
        return filename

    def create_directory(self, path_file):
        """ Create the directory if it doesn't exist """
        substr = path_file.split(os.sep)
        path_directory = os.sep.join(substr[:-1])
        try:
            Path(path_directory).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            logging.error("Error creating the directory: " + str(e))
            raise "Error creating nested directories: " + str(e)
