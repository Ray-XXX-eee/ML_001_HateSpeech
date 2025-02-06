import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

class DataTransformation:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def transform_data(self):
        # :Should be moved to utility. already have downloaded data. If making for user need uploaded data option.  
        pass
    def clean_data(self):
        stopwords = set(stopwords.words('english'))
        self.data['tweet']= self.data['tweet'].apply(lambda x: ' '.join(
            [word for word in x.split() if word not in (stopwords)]
        ))
        return self.data
        