import pandas as pd
import logging
from src.utils.exceptions import InvalidDatasetError

logging.basicConfig(level=logging.INFO, format="% (asctime)s -%(levelname)s -%(message)s")

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.required_columns = [
            'employee_id', 'first_name', 'last_name', 'age', 'gender', 
            'department', 'designation', 'salary', 'joining_date', 
            'experience', 'performance_score', 'city', 'status', 'department_id'      
        ]

    def load_csv(self) -> pd.DataFrame:
        logging.info(f"Ingesting raw dataset inputs matrix logs pipeline from path: {self.file_path}")
        try:
            self.df = pd.read_csv(self.file_path)
            self._inspect_and_profile()
            self._validate_scheme()
            return self.df
        except FileNotFoundError:
            logging.error(f"Target file path completely missing variables context bounds: {self.file_path}")
            raise

    def _inspect_and_profile(self):
        print("\n ==== RAW Target Dataset Schematic Baseline Profile ====")
        print(f"Total Operational Population Dimensions Grid: {self.df.shape}")
        print("\n Column Haeder Typing Verification Mapping Layout:")
        print(self.df.dtypes)
        print("\n")

    def _validate_scheme(self):
        missing_cols = [col for col in self.required_columns if col not in self.df.columns]
        if missing_cols:
            error_msg = f"Critical mandatory tracking scheme fields headers column labels completely missing: {missing_cols}"
            logging.error(error_msg)
            raise InvalidDatasetError(error_msg)
        logging.info("Ingestion tracking verification checklist success. Required data structure columns present.")

    


