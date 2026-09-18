"""
Generate production-like customer churn data for local testing.

This is synthetic/demo data and does not contain real customer information.
"""

from pathlib import Path
import random

import pandas as pd


OUTPUT_DIR = Path("data/sample")
OUTPUT_FILE = OUTPUT_DIR / "customer_churn_sample.csv"


def generate_data(number_of_rows: int = 1000) -> pd.DataFrame:
    """Generate synthetic customer churn records."""

    records = []

    for index in range(number_of_rows):
        records.append(
            {
                "customer_id": f"CUST{index + 1:06d}",
                "gender": random.choice(["Male", "Female"]),
                "senior_citizen": random.choice([0, 1]),
                "partner": random.choice(["Yes", "No"]),
                "dependents": random.choice(["Yes", "No"]),
                "tenure": random.randint(0, 72),
                "phone_service": random.choice(["Yes", "No"]),
                "internet_service": random.choice(
                    ["DSL", "Fiber optic", "No"]
                ),
                "contract": random.choice(
                    ["Month-to-month", "One year", "Two year"]
                ),
                "monthly_charges": round(random.uniform(20, 120), 2),
                "total_charges": round(random.uniform(20, 8000), 2),
                "churn": random.choice(["Yes", "No"]),
            }
        )

    return pd.DataFrame(records)


def main() -> None:
    """Generate and save the sample dataset."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dataframe = generate_data()

    dataframe.to_csv(OUTPUT_FILE, index=False)

    print(f"Generated {len(dataframe)} records")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()