import pandas as pd
import logging

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def clean_and_preprocess(self) -> pd.DataFrame:
        logging.info("Executing sanitization process loops data transformations parameters cleaner cycles...")

        for col in self.df.columns:
            if self.df[col].dtype in ['int64', 'float']:
                self.df[col] = self.df[col].fillna(self.df[col].median())
            else:
                self.df[col] = self.df[col].fillna("Unknown")

        self.df.drop_duplicates(subset=['employee_id'], keep='first', inplace=True)

        self.df['salary'] = pd.to_numeric(self.df['salary'], errors='coerce')
        self.df['joining_date'] = pd.to_datetime(self.df['joining_date'], errors='coerce')
        self.df['experience'] = pd.to_numeric(self.df['experience'], errors='coerce')
        self.df['performance_score'] = pd.to_numeric(self.df['performance_score'], errors='coerce')

        self.df.dropna(subset=['employee_id', 'salary', 'joining_date'], inplace=True)
        return self.df