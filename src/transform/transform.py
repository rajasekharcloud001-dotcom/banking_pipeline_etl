import pandas as pd

def transform(local_path):
    """Data clean చేయి"""
    
    print(f"🔄 Transforming: {local_path}")
    
    # CSV file చదువు
    df = pd.read_csv(local_path)
    print(f"📊 Total records before transform: {len(df)}")
    
    # Step 1: Duplicates remove చేయి
    df = df.drop_duplicates(subset=["transaction_id"])
    print(f"✅ After removing duplicates: {len(df)}")
    
    # Step 2: Negative amounts remove చేయి
    df = df[df["amount"] > 0]
    print(f"✅ After removing negative amounts: {len(df)}")
    
    # Step 3: Date format validate చేయి ← ఇక్కడ మార్చాం!
    df["date"] = pd.to_datetime(df["date"]).dt.date
    print(f"✅ Date format validated!")
    
    # Step 4: Status validate చేయి
    valid_statuses = ["success", "failed"]
    df = df[df["status"].isin(valid_statuses)]
    print(f"✅ After validating status: {len(df)}")
    
    # Step 5: Column names clean చేయి
    df.columns = df.columns.str.strip().str.lower()
    print(f"✅ Columns cleaned!")
    
    print(f"📊 Total records after transform: {len(df)}")
    
    return df

if __name__ == "__main__":
    import os
    local_path = os.getenv("LOCAL_PATH", "data/banking_data_2026-03-30.csv")
    df = transform(local_path)
    print(df.head())