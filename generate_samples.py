from pathlib import Path
import numpy as np
import pandas as pd

# Directories setup
samples_dir = Path("data/uploads/samples")
samples_dir.mkdir(parents=True, exist_ok=True)

# Seed for reproducibility
np.random.seed(42)

# ==========================================
# 1. Generate Sample Sales Dataset
# ==========================================
num_sales_records = 150

# Random dates in 2026
start_date = pd.to_datetime("2026-01-01")
end_date = pd.to_datetime("2026-06-30")
random_days = np.random.randint(
    0, (end_date - start_date).days, size=num_sales_records
)
order_dates = [
    (start_date + pd.Timedelta(days=int(d))).strftime("%Y-%m-%d")
    for d in random_days
]

# Random products and pricing structure
products = [
    "Product Alpha",
    "Product Beta",
    "Product Gamma",
    "Product Delta",
    "Product Epsilon",
]
product_prices = {
    "Product Alpha": 150.0,
    "Product Beta": 200.0,
    "Product Gamma": 500.0,
    "Product Delta": 75.0,
    "Product Epsilon": 300.0,
}

chosen_products = np.random.choice(
    products, size=num_sales_records, p=[0.3, 0.25, 0.15, 0.2, 0.1]
)
quantities = np.random.randint(1, 15, size=num_sales_records)
unit_prices = [product_prices[p] for p in chosen_products]
revenues = [q * p for q, p in zip(quantities, unit_prices)]

sales_df = pd.DataFrame(
    {
        "order_id": [f"ORD-{1000 + i}" for i in range(num_sales_records)],
        "order_date": order_dates,
        "product": chosen_products,
        "quantity": quantities,
        "unit_price": unit_prices,
        "revenue": revenues,
    }
)

# Sort by order_date
sales_df = sales_df.sort_values(by="order_date").reset_index(drop=True)
sales_path = samples_dir / "sample_sales.csv"
sales_df.to_csv(sales_path, index=False)
print(f"✅ Generated {sales_path} with {len(sales_df)} rows.")


# ==========================================
# 2. Generate Sample Customer Dataset
# ==========================================
num_customers = 50
segments = ["Enterprise", "SMB", "Consumer"]

chosen_segments = np.random.choice(
    segments, size=num_customers, p=[0.2, 0.5, 0.3]
)

# Higher churn rate for Consumer/SMB compared to Enterprise
churn_probabilities = {
    "Enterprise": 0.1,
    "SMB": 0.25,
    "Consumer": 0.4,
}

churned_status = [
    1 if np.random.rand() < churn_probabilities[s] else 0
    for s in chosen_segments
]

customers_df = pd.DataFrame(
    {
        "customer_id": [f"CUST-{2000 + i}" for i in range(num_customers)],
        "segment": chosen_segments,
        "churned": churned_status,
    }
)

customers_path = samples_dir / "sample_customers.csv"
customers_df.to_csv(customers_path, index=False)
print(f"✅ Generated {customers_path} with {len(customers_df)} rows.")