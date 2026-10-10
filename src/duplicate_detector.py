
from src.similarity import calculate_similarity


def find_duplicates(df, threshold=0.85):
    results = []

    records = df.to_dict("records")

    for i in range(len(records)):
        for j in range(i + 1, len(records)):

            a = records[i]
            b = records[j]

            if a["customer_id"] == b["customer_id"]:
                continue

            email_match = (
                bool(a["email_clean"])
                and a["email_clean"] == b["email_clean"]
            )

            phone_match = (
                bool(a["phone_clean"])
                and a["phone_clean"] == b["phone_clean"]
            )

            name_score = calculate_similarity(
                a["name_clean"],
                b["name_clean"]
            )

            if email_match or phone_match or name_score >= threshold:

                reasons = []

                if email_match:
                    reasons.append("Exact email match")

                if phone_match:
                    reasons.append("Exact phone match")

                if name_score >= threshold:
                    reasons.append("Similar name")

                results.append({
                    "customer_id_1": a["customer_id"],
                    "name_1": a["name"],
                    "customer_id_2": b["customer_id"],
                    "name_2": b["name"],
                    "similarity_score": name_score,
                    "match_reason": ", ".join(reasons)
                })

    return results
