import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import os

class ChartSuite:
    def __init__(self, df: pd.DataFrame, output_dir: str = "outputs/charts"):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        plt.style.use('ggplot')

    def generate_all_plots(self):
        plt.figure(figsize=(7, 4))
        self.df.groupby('department')['salary'].mean().plot(kind='bar', color='teal', edgecolor='black')
        plt.title('1. Bar Chart: Average Salary Metrics by Department Categories')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '1_salary_disparity.png'))
        plt.close()

        plt.figure(figsize=(7, 4))
        sorted_df = self.df.sort_values('joining_date')
        plt.plot(sorted_df['joining_date'], range(1, len(sorted_df) + 1), color='navy', linewidth=2)
        plt.title('2. Line Chart: Corporate Employee Ingestion Trajectory Growth')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '2_growth_trajectory.png'))
        plt.close()

        plt.figure(figsize=(7, 4))
        plt.hist(self.df['salary'], bins=12, color='crimson', edgecolor='black', alpha=0.8)
        plt.title('3. Histogram: Compensation Salary Income Distribution Frequency Skewness')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '3_salary_skewness.png'))
        plt.close()

        plt.figure(figsize=(7, 4))
        plt.scatter(self.df['experience'], self.df['salary'], color='darkorange', alpha=0.8, edgecolors='black')
        plt.title('4. Scatter Plot: Years Experience Tenure vs Base Salary Levels Indices')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '4_experience_correlation.png'))
        plt.close()

        plt.figure(figsize=(5, 5))
        counts = self.df['department'].value_counts()
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', wedgeprops=dict(width=0.4, edgecolor='black'))
        plt.title('5. Donut Chart: Organizational Corporate Headcount Share Allocations Footprints')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, '5_headcount_share.png'))
        plt.close()  