from config import *
import pickle


class LoadData:

    def __init__(self):

        self.benigns_df = None
        self.benigns_abnormalities_df = None
        self.cancers_df = None
        self.cancers_abnormalities_df = None
        self.normals_df = None

        self.load()


    def load(self):
        with open(pickles_path+'/benigns_df.pkl', 'rb') as handle:
            self.benigns_df = pickle.load(handle)

        with open(pickles_path+'/benigns_abnormalities_df.pkl', 'rb') as handle:
            self.benigns_abnormalities_df = pickle.load(handle)

        with open(pickles_path+'/cancers_df.pkl', 'rb') as handle:
            self.cancers_df = pickle.load(handle)

        with open(pickles_path+'/cancers_abnormalities_df.pkl', 'rb') as handle:
            self.cancers_abnormalities_df = pickle.load(handle)

        with open(pickles_path+'/normals_df.pkl', 'rb') as handle:
            self.normals_df = pickle.load(handle)

    def clean(self):
        self.normals_df = self.normals_df.drop(['</pre>]', '[<pre>', 'FILM', 'SEQUENCE'], axis=1)
        self.benigns_df = self.benigns_df.drop(['</pre>]', '[<pre>', 'FILM', 'SEQUENCE'], axis=1)
        self.cancers_df = self.cancers_df.drop(['</pre>]', '[<pre>', 'FILM', 'SEQUENCE'], axis=1)
        self.benigns_abnormalities_df = self.benigns_abnormalities_df.drop(
            ['</font></pre>,', '</font></pre>]', '<font', 'BOUNDARY', \
             '[<pre>', '</font><font', 'CORE', 'CLUSTERED'], axis=1)
        self.cancers_abnormalities_df = self.cancers_abnormalities_df.drop(
            ['</font></pre>,', '</font></pre>]', '<font', 'BOUNDARY', \
             '[<pre>', '</font><font', 'CORE'], axis=1)

        self.benigns_abnormalities_df['filename'] = self.benigns_abnormalities_df.apply(
            lambda row: row['FILE:'].split('.')[0].replace('_', '-'), axis=1)
        self.cancers_abnormalities_df['filename'] = self.cancers_abnormalities_df.apply(
            lambda row: row['FILE:'].split('.')[0].replace('_', '-'), axis=1)

        self.benigns_abnormalities_df = self.benigns_abnormalities_df[
            self.benigns_abnormalities_df['LESION_TYPE'].str.contains("CALCIFICATION") == False]

        self.cancers_abnormalities_df = self.cancers_abnormalities_df[
            self.cancers_abnormalities_df['LESION_TYPE'].str.contains("CALCIFICATION") == False]

