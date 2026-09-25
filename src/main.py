import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import numpy as np
from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.analysis.analyzer import DataAnalyzer
from src.api.client import APIClient
from src.visualization.charts import ChartSuite
from src.reports.generator import ReportGenerator

def main():
    raw_csv_path = "data/raw/employees.csv"
    os.makedirs(os.path.dirname(raw_csv_path), exist_ok=True)
    
    depts = ['Engineering', 'Product', 'Sales', 'HR', 'Marketing']
    cities = ['Austin', 'Chicago', 'Denver', 'San Francisco', 'New York']
    
    rows = [[f"EMP-{2000+i}", f"First_{i}", f"Last_{i}", np.random.randint(22,55), 
             np.random.choice(['M','F']), np.random.choice(depts), 'Consultant', 
             np.random.randint(55000,135000), "2023-05-12", np.random.randint(1,12), 
             np.random.randint(1,5), np.random.choice(cities), 'Active', 401] for i in range(1, 105)]
    
    pd.DataFrame(rows, columns=['employee_id', 'first_name', 'last_name', 'age', 'gender', 
                                'department', 'designation', 'salary', 'joining_date', 
                                'experience', 'performance_score', 'city', 'status', 'department_id']).to_csv(raw_csv_path, index=False)

    logging.info("Employee Pipeline Framework - Main environment varaiables loaded successfully.")

    raw_df = DataLoader(raw_csv_path).load_csv()
    cleaned_df = DataCleaner(raw_df).clean_and_preprocess()
    
    os.makedirs("data/processed", exist_ok=True)
    cleaned_df.to_csv("data/processed/cleaned_employees.csv", index=False)

    analyzer = DataAnalyzer(cleaned_df, "data/raw/departments.csv")
    analyzer.run_numpy_vectorization()
    metric_summary_df = analyzer.compute_aggregations()
    final_merged_df = analyzer.merge_secondary_data()

    api_metadata = APIClient().fetch_external_benchmarks()
    ChartSuite(final_merged_df).generate_all_plots()
    ReportGenerator(final_merged_df, metric_summary_df, api_metadata).generate_production_deliverables()

    logging.info("Pipeline execution finished successfully.")
    logging.info("Data cleaning and processing completed.")
    logging.info("Success!")
    logging.info("Process completed without errors.")

if __name__ == "__main__":
    main()