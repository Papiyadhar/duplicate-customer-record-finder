
import pandas as pd
import streamlit as st

from src.preprocessing import clean_customer_data
from src.duplicate_detector import find_duplicates
from src.database import save_results


st.set_page_config(
    page_title="Duplicate Customer Finder",
    page_icon="🔎",
    layout="wide"
)

st.title("Duplicate Customer Record Finder")

st.write(
    "Upload customer records to identify possible duplicates."
)

uploaded_file = st.file_uploader(
    "Upload customer CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(
            uploaded_file,
            dtype=str
        ).fillna("")

        st.subheader("Customer Records")
        st.dataframe(df, use_container_width=True)

        cleaned_df = clean_customer_data(df)

        threshold = st.slider(
            "Name similarity threshold",
            min_value=0.50,
            max_value=1.00,
            value=0.85,
            step=0.05
        )

        if st.button("Find Duplicates"):

            results = find_duplicates(
                cleaned_df,
                threshold=threshold
            )

            if results:
                result_df = pd.DataFrame(results)

                save_results(results)

                st.success(
                    f"Found {len(results)} possible duplicate pairs."
                )

                st.subheader("Possible Duplicate Records")
                st.dataframe(
                    result_df,
                    use_container_width=True
                )

                st.download_button(
                    label="Download Results CSV",
                    data=result_df.to_csv(
                        index=False
                    ).encode("utf-8"),
                    file_name="duplicate_candidates.csv",
                    mime="text/csv"
                )

            else:
                st.success("No duplicate candidates found.")

    except Exception as error:
        st.error(f"Error: {error}")

else:
    st.info("Upload data/customers.csv to get started.")
