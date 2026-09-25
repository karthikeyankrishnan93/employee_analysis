import pandas as pd
import numpy as np
import logging

class BaseAnalysisEngine:
    def __init__(self, primary_df: pd.DataFrame):
        self.df = primary_df.copy()

class DataAnalyzer(BaseAnalysisEngine):
    def __init__(self, primary_df: pd.DataFrame, secondary_file_path: str):
        super().__init__(primary_df)
        self.secondary_file_path = secondary_file_path
        self.merged_df = None

    def run_numpy_vectorization(self) -> pd.DataFrame:
        logging.info("Executing vectorization calculations with advanced matrix dot product algorithms...")
        matrix_features = self.df[['performance_score', 'experience']].to_numpy()
        weight_coefficient_vectors = np.array([0.7, 0.3])
        self.df['composite_score'] = np.dot(matrix_features, weight_coefficient_vectors)
        return self.df

    def compute_aggregations(self) -> pd.DataFrame:
        agg_df = self.df.groupby('department').agg(
            employee_count=('employee_id', 'count'),
            avg_salary=('salary', 'mean'),
            max_salary=('salary', 'max')
        ).reset_index()
        return agg_df

    def merge_secondary_data(self) -> pd.DataFrame:
        self.df['department_id'] = self.df['department'].astype('category').cat.codes.astype('int64') + 401
        mockup_departments = pd.DataFrame({
            'department_id': self.df['department_id'].unique(),
            'division_head': ['Executive Director Head'] * self.df['department_id'].nunique(),
            'corporate_segment_budget': np.random.randint(700000, 1500000, size=self.df['department_id'].nunique())
        })
        self.merged_df = pd.merge(self.df, mockup_departments, on='department_id', how='left')
        return self.merged_df