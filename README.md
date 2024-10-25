# Vehicle Maintenance Data Pipeline and Analysis Project
This project establishes a data pipeline to clean, transform, and prepare vehicle maintenance data for analysis and predictive modeling. The pipeline performs essential data quality checks to ensure completeness, validity, and consistency, storing the processed data in a SQLite database. The ultimate goal is to enable data analysis and predictive modeling to anticipate vehicle maintenance needs.

## Project Structure 
vehicle_maintenance_project/
├── config/                  # Configuration files
│   └── config.yaml          # YAML file for paths and settings
├── data/                    # Data storage
│   ├── raw/                 # Raw data
│   │   └── vehicle_maintenance.csv
│   └── processed/           # Processed data output
├── logs/                    # Log files
│   └── pipeline.log         # Log file for pipeline execution
├── notebooks/               # Jupyter notebooks for analysis and predictions
├── src/                     # Source code for pipeline modules
│   ├── clean.py             # Data cleaning functions
│   ├── extract.py           # Data extraction functions
│   ├── load.py              # Data loading functions
│   ├── quality_checks.py    # Data quality checks
│   ├── transform.py         # Data transformation functions
│   └── utils.py             # Utility functions (e.g., logging setup)
├── tests/                   # Test files for each module
├── requirements.txt         # Project dependencies
└── main.py                  # Main script to execute the pipeline


## Getting Started
### Prerequisites
Ensure you have Python 3.8+ installed. Clone the repository and navigate into the project directory.

### Setup

1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
