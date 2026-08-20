# ETL Pipeline - Exchange Rates 💱

A simple ETL (Extract, Transform, Load) pipeline built with Python that fetches daily currency exchange rates from a public API, cleans and structures the data, and stores it in a SQLite database. The pipeline is scheduled to run automatically every day using Windows Task Scheduler.

## 📋 Overview

This project demonstrates the core workflow of a Data Engineer's daily work:

- **Extract**: Pull live exchange rate data from the [Frankfurter API](https://www.frankfurter.app/)
- **Transform**: Clean and structure the raw JSON response into a well-formed table using Pandas
- **Load**: Store the structured data into a SQLite database, appending new records on every run
- **Automate**: Schedule the pipeline to run daily without manual intervention

## 🛠️ Tech Stack

- **Python 3.11**
- **Requests** — for calling the API
- **Pandas** — for data cleaning and transformation
- **SQLAlchemy** — for connecting to and writing into the database
- **SQLite** — as the storage layer
- **Windows Task Scheduler** — for automated daily execution

## 📂 Project Structure

```
etl_project/
│
├── etl_pipeline.py      # Main ETL script (extract, transform, load)
├── run_etl.bat           # Batch file used to trigger the script via Task Scheduler
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from version control
└── README.md              # Project documentation
```

## ⚙️ How It Works

1. **Extract** — Sends a GET request to the Frankfurter API to retrieve the latest USD exchange rates.
2. **Transform** — Converts the JSON response into a Pandas DataFrame, adds metadata columns (`base_currency`, `rate_date`, `extracted_at`).
3. **Load** — Appends the cleaned data into a table (`exchange_rates`) inside a local SQLite database (`exchange_rates.db`), preserving historical records from every run.
4. **Schedule** — A `.bat` file wraps the script execution and is triggered daily via Windows Task Scheduler, enabling the pipeline to run automatically without manual execution.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/samaresmat/etl-exchange-rate.git
cd etl-exchange-rate

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run the pipeline manually

```bash
python etl_pipeline.py
```

### Schedule it to run automatically (Windows)

1. Create a `run_etl.bat` file pointing to your virtual environment's Python and the script.
2. Open **Task Scheduler** → **Create Basic Task**.
3. Set the trigger (e.g., Daily) and point the action to `run_etl.bat`.

## 📊 Example Output

After running, the `exchange_rates` table looks like this:

| currency | rate   | base_currency | rate_date  | extracted_at        |
|----------|--------|----------------|------------|----------------------|
| EUR      | 0.8600 | USD            | 2026-08-19 | 2026-08-19 14:23:01  |
| GBP      | 0.7400 | USD            | 2026-08-19 | 2026-08-19 14:23:01  |
| EGP      | 47.850 | USD            | 2026-08-19 | 2026-08-19 14:23:01  |

## 🔮 Future Improvements

- Add data validation checks (e.g., detect abnormal rate jumps)
- Migrate from SQLite to PostgreSQL for a more production-like setup
- Replace Task Scheduler with Apache Airflow for more robust orchestration
- Add unit tests for each pipeline stage
- Build a small dashboard to visualize historical exchange rate trends

## 📝 License

This project is open source and available for learning purposes.
