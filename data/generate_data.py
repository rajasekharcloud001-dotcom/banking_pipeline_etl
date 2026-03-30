import csv
import random
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

account_numbers = [f"ACC{str(i).zfill(6)}" for i in range(1, 1001)]
transaction_types = ["credit", "debit"]
statuses = ["success", "success", "success", "failed"]
banks = ["SBI", "HDFC", "ICICI", "AXIS", "KOTAK"]

def generate_data(num_records=1000):
    filename = f"data/banking_data_{today}.csv"
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "transaction_id",
            "account_number",
            "amount",
            "transaction_type",
            "date",
            "status",
            "bank_name"
        ])
        
        for i in range(1, num_records + 1):
            writer.writerow([
                f"T{today.replace('-','')}_{str(i).zfill(6)}",
                random.choice(account_numbers),
                round(random.uniform(100, 100000), 2),
                random.choice(transaction_types),
                today,
                random.choice(statuses),
                random.choice(banks)
            ])
            
    print(f"✅ {num_records} records generated for {today}")
    print(f"📁 File saved: {filename}")
    return filename

if __name__ == "__main__":
    generate_data()