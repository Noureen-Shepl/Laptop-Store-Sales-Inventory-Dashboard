# Laptop Store Sales & Inventory Dashboard

An interactive portfolio demo built with Python, pandas, Streamlit and Plotly. All records are synthetic and do not represent a real client.

## Features
- Revenue, gross profit, units and transaction KPIs
- Brand and date filters
- Monthly revenue, brand comparison and best-selling models
- Current inventory snapshot with reorder alerts
- Filtered transaction table and CSV export

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data and definitions
`sales.csv` contains one line per simulated transaction. Revenue = quantity × unit price. Gross profit = quantity × (unit price − unit cost); operating expenses and taxes are excluded. `inventory.csv` is a separate illustrative current stock snapshot, filtered by brand only, not historical dates. This is an analytics demo, not a transactional POS or live inventory management system.

## Project structure
- `app.py`: dashboard logic
- `sales.csv`: synthetic transactions
- `inventory.csv`: synthetic inventory snapshot
- `requirements.txt`: dependencies

Created as an AI-assisted portfolio learning project. Review and customize before presenting it.
