import pandas as pd

# Step 1: Create the dictionary with the extracted customer records
data = {
    "Customer_ID": [
        "C001",
        "C002",
        "C003",
        "C004",
        "C005",
        "C006",
        "C007",
        "C008",
    ],
    "Customer_Name": [
        "Amit Sharma",
        "Priya Mehta",
        "Rahul Verma",
        "Sneha Patil",
        "Arjun Rao",
        "Neha Kapoor",
        "Vikram Singh",
        "Riya Shah",
    ],
    "Date_of_Birth": [
        "15-MAY-90",
        "20-AUG-88",
        "10-FEB-92",
        "22-NOV-85",
        "17-MAR-95",
        "12-JUL-91",
        "25-JAN-87",
        "18-SEP-94",
    ],
    "City": [
        "Pune",
        "Mumbai",
        "Delhi",
        "Pune",
        "Bangalore",
        "Mumbai",
        "Delhi",
        "Pune",
    ],
    "Segment": [
        "Retail",
        "Premium",
        "Retail",
        "Premium",
        "Retail",
        "Retail",
        "Premium",
        "Retail",
    ],
    "Risk_Category": [
        "LOW",
        "LOW",
        "MEDIUM",
        "LOW",
        "HIGH",
        "MEDIUM",
        "HIGH",
        "LOW",
    ],
}

# Step 2: Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

print(df.shape)