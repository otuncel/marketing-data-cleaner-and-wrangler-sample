import numpy as np
import pandas as pd

# Simulated messy dataset provided by the client's marketing campaign
raw_data = {
    "Customer_ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Full_Name": ["  oLiVeR sMiTh ", " JOHN doe ", "alice SMITH", "  oLiVeR sMiTh ", "Bob Marley", "Invalid Data"],
    "Email": ["oliver@example.com", "john.doe@mail.com", np.nan, "oliver@example.com", "bob@music.com", np.nan],
    "Phone": ["+1 555-123-4567", "  123 456 7890 ", "5559876543", "+1 555-123-4567", np.nan, np.nan],
    "Registration_Date": ["2026-05-10", "2026-05-11", "2026-05-12", "2026-05-15", "2026-05-13", "2026-05-14"]
}

# Load the messy dictionary into a Pandas DataFrame
df = pd.DataFrame(raw_data)
print("Initial Messy DataFrame:")
print(df.head())
print("-" * 50)

# --- STEP 1: HANDLE MISSING VALUES ---
# Drop rows where BOTH 'Email' and 'Phone' are completely missing (uncontactable leads)
df.dropna(subset=['Email', 'Phone'], how='all', inplace=True)

# Flag remaining missing phone numbers as "Pending Verification"
df['Phone'] = df['Phone'].fillna('Pending Verification')


# --- STEP 2: DEDUPLICATION ---
# Sort by Date to ensure the latest registration entry is kept during deduplication
df = df.sort_values(by='Registration_Date')

# Remove duplicate records based on 'Email' column, keeping the last (most recent) entry
df.drop_duplicates(subset=['Email'], keep='last', inplace=True)


# --- STEP 3: STRING CLEANING & CASING ---
# Trim leading/trailing whitespaces and convert to standard Title Case (e.g., "John Doe")
df['Full_Name'] = df['Full_Name'].str.strip().str.title()


# --- STEP 4: PHONE NUMBER STANDARDIZATION ---
# Use regex to strip away all non-numeric characters (spaces, dashes, plus signs)
# Skip processing if the row has our custom string flag 'Pending Verification'
df['Phone'] = df['Phone'].apply(lambda x: ''.join(filter(str.isdigit, str(x))) if x != 'Pending Verification' else x)


# --- STEP 5: EXPORT CLEANED DATASET ---
# Reset index for structural cleanliness before exporting
df.reset_index(drop=True, inplace=True)

# Export to a high-integrity CSV file
df.to_csv('cleaned_customer_leads.csv', index=False, encoding='utf-8')

print("\n🚀 Success! Cleaned data pipeline completed.")
print("Final Output Dataset:")
print(df.head())