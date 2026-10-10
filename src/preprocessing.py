
import re
import pandas as pd


def clean_text(value):
    if pd.isna(value):
        return ""

    value = str(value).lower().strip()
    value = re.sub(r"[^a-z0-9@.+]", "", value)

    return value


def clean_phone(value):
    if pd.isna(value):
        return ""

    return re.sub(r"\D", "", str(value))


def clean_customer_data(df):
    df = df.copy()

    required_columns = [
        "customer_id",
        "name",
        "email",
        "phone"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    df["customer_id"] = df["customer_id"].astype(str)

    df["name_clean"] = df["name"].apply(clean_text)
    df["email_clean"] = df["email"].apply(clean_text)
    df["phone_clean"] = df["phone"].apply(clean_phone)

    return df
