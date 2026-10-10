
import sqlite3
import pandas as pd


def save_results(results, db_path="duplicates.db"):
    """Save duplicate candidates in a SQLite database."""

    columns = [
        "customer_id_1",
        "name_1",
        "customer_id_2",
        "name_2",
        "similarity_score",
        "match_reason"
    ]

    df = pd.DataFrame(results, columns=columns)

    with sqlite3.connect(db_path) as connection:
        df.to_sql(
            "duplicate_candidates",
            connection,
            if_exists="replace",
            index=False
        )


def get_results(db_path="duplicates.db"):
    """Read saved duplicate candidates."""

    with sqlite3.connect(db_path) as connection:
        return pd.read_sql_query(
            "SELECT * FROM duplicate_candidates",
            connection
        )
