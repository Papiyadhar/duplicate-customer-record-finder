# Duplicate Customer Record Finder

## About the Project
Duplicate Customer Record Finder is a Python-based CRM utility that identifies possible duplicate customer records using names, email addresses, phone numbers, and text similarity.

## Features
- Upload customer records using a CSV file.
- Clean and normalize customer data.
- Detect exact email and phone matches.
- Identify similar customer names.
- Display possible duplicate records in a Streamlit web app.
- Download duplicate results as a CSV report.
- Store duplicate candidates in an SQLite database.

## Technologies Used
- Python
- Pandas
- Regular Expressions (Regex)
- difflib
- SQLite
- Streamlit

## Project Structure
```text
duplicate-customer-record-finder/
├── data/
│   └── customers.csv
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── duplicate_detector.py
│   └── database.py
├── tests/
│   └── test_duplicates.py
├── app.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Install dependencies:

   `python -m pip install -r requirements.txt`

4. Start the application:

   `python -m streamlit run app.py`

5. Open the local URL shown in the terminal and upload a customer CSV file.

## Input CSV Format
The CSV file should contain these columns:

- `customer_id`
- `name`
- `email`
- `phone`

## Testing

Run the tests using:

`python -m unittest discover -s tests -v`

## Note
This tool identifies possible duplicates for human review. Similar records are not necessarily the same customer, so results should be verified before merging records.