import requests
from bs4 import BeautifulSoup
import pickle
from config import *


class Scraper:

    def __init__(self, table_links):
        self.links = table_links
        self.ftps = []
        self.table_normal = []
        self.table_cancer = []
        self.table_benign = []

        self.scrap_all_tables()

        self.dump_to_pickle(self.ftps, "ftps_list")
        self.dump_to_pickle(self.table_normal, "table_normal")
        self.dump_to_pickle(self.table_cancer, "table_cancer")
        self.dump_to_pickle(self.table_benign, "table_benign")



    def scrap_all_tables(self):

        for link in self.links:

            if 'thumbnails' in link:
                thumbnail_url = link['href']
                case_type = thumbnail_url[16:].split("/", 1)[0]
                thumbnail_url = "http://www.eng.usf.edu/cvprg/Mammography/" + thumbnail_url
                main_name = thumbnail_url[:-14]

                th_page = requests.get(thumbnail_url)  # Store the contents of the website under doc
                th_html = BeautifulSoup(th_page.text)
                th_table = th_html.find('table')
                th_links = th_table.findAll('a')

                case_id = 0

                for th_link in th_links:

                    case_url = th_link['href']
                    case_url = main_name + "/" + case_url
                    case_url_page = requests.get(case_url)  # Store the contents of the website under doc
                    case_url_html = BeautifulSoup(case_url_page.text)
                    case_url_tables = case_url_html.findAll('table')

                    for i in range(2, len(case_url_tables)):

                        info = case_url_tables[i].findAll(lambda tag: tag.name == 'pre')

                        if case_type == 'normals':
                            self.table_normal.append([i, case_id, info])

                        if case_type == 'cancers':
                            self.table_cancer.append([i, case_id, info])

                        if case_type == 'benigns':
                            self.table_benign.append([i, case_id, info])

                    case_id += 1

            if 'ftp' in link:
                ftp_url = link['href']
                self.ftps.append(ftp_url)


    def dump_to_pickle(self, df, df_name):
        with open(df_pickles_path + df_name + '.pkl', 'wb') as f:
            pickle.dump(df, f)
