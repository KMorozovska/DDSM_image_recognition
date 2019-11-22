from LoadData import *


class PrepareData:

    def __init__(self, df, density=None, lesion_type_list=None):

        self.df = df
        self.lesion_type_list = lesion_type_list
        self.density = density


    def count_values(self):
        if self.density:
            if self.lesion_type_list:
                count = 0
                for elem in self.lesion_type_list:
                    count += len(self.df[self.df['LESION_TYPE'].str.contains(elem)])
                return count
            else:
                return len(self.df[self.df['DENSITY'] == self.density])
        else:
            if self.lesion_type_list:
                count = 0
                for elem in self.lesion_type_list:
                    count += len(self.df[self.df['LESION_TYPE'].str.contains(elem)])
                return count
            else:
                return len(self.df)
