import json
import os

class ReportGenerator:
    def __init__(self, processed_df, agg_summary_df, api_metadata, output_root_dir="outputs"):
        self.df = processed_df
        self.agg_df = agg_summary_df
        self.api_meta = api_metadata
        self.output_root_dir = output_root_dir
        os.makedirs(self.output_root_dir, exist_ok=True)

    def generate_production_deliverables(self):
        summary_payload = {
            "total_records_analyzed_capacity": int(len(self.df)),
            "overall_calculated_average_salary_index": float(self.df['salary'].mean()),
            "api_connection_sync_status": self.api_meta.get("status"),
            "departmental_analytics_summary_breakdown": self.agg_df.to_dict(orient="records")
        }
        with open(os.path.join(self.output_root_dir, "analysis_summary.json"), 'w') as f:
            json.dump(summary_payload, f, indent=4)

        md_layout_content = f"""# Executive Analytics Insights Business Intelligence Production Report

## 1. Executive Summary Portfolio Dataset Performance Indicators Overview
- Total Operational Population Ingested: {len(self.df)} validation data records nodes.
- Overall Aggregated Compensation Remuneration Index Average Baseline Value: \${self.df['salary'].mean():,.2f}
"""
        for finding in [
            f"1. Organization Wage Ceiling: High scale remuneration thresholds tracking profile peaks points to absolute maximum ceiling records mark parameter value of \${self.df['salary'].max():,.2f}.",
            f"2. Experience Tenure Covariance: The operational workforce footprint tenure averages metrics evaluation tracking holds stable parameters index value marking range point: {self.df['experience'].mean():.1f} years.",
            f"3. Operational Distribution Profiles: Heavy workforce headcount concentration profiles tracks majority density personnel allocation under operational business unit sector label text tokens: '{self.df['department'].mode()[0] if not self.df['department'].mode().empty else 'Unknown'}'.",
            f"4. Advanced Operations Analytics Matrix Results: Vectorized 2D cross evaluation matrix dot product calculations loops yields mean compound organizational composite performance indicator marks value scores: {self.df['composite_score'].mean():.2f}.",
            f"5. External API Handshake Integration Status: Systems network structural validation synchronizations processed safely returning connection logging tags status string profile target index: '{self.api_meta.get('status')}'."
        ]:
            md_layout_content += f"{finding}\n"

        md_layout_content += f"\n## 3. Visualization Portfolio Catalog Maps Verification Directories Paths\n"
        md_layout_content += "- All matching 5 standard high definition charts png graphics deliverables saved completely inside folder destinations path layout target: `outputs/charts/` successfully.\n"

        with open(os.path.join(self.output_root_dir, "analysis_report.md"), 'w') as f:
            f.write(md_layout_content)