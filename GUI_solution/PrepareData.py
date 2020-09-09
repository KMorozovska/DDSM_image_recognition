from LoadData import *
import pandas as pd

class PrepareData:

    def __init__(self, conditions_list):

        all_normal = pd.read_csv("tables/all_normal_cases_data.csv")
        all_cancer = pd.read_csv("tables/all_cancer_cases_data.csv")
        all_benign = pd.read_csv("tables/all_benign_cases_data.csv")

        self.all_data = pd.concat([all_normal, all_cancer, all_benign], axis = 0, sort=False)
        self.all_conditions = conditions_list

        print(self.all_data.columns)
        print(self.all_data.head())


    def count_values(self):
        print(self.all_conditions)

        print(self.all_conditions['DENSITY'])

        cond1 = self.all_data['DENSITY'].isin(self.all_conditions['DENSITY'])
        cond2 = self.all_data['SUBTLETY'].isin(self.all_conditions['SUBTLETY'])
        cond3 = self.all_data['ASSESSMENT'].isin(self.all_conditions['ASSESSMENT'])
        cond4 = self.all_data['LESION_TYPE'].isin(self.all_conditions['LESION_TYPE'])

        count = len(self.all_data[cond1 & cond2 & cond3 & cond4])

        print(count)
        return count
