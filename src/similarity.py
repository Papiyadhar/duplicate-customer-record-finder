
from difflib import SequenceMatcher


def calculate_similarity(text1, text2):
    """Calculate text similarity between two values."""

    if not text1 or not text2:
        return 0.0

    score = SequenceMatcher(
        None,
        str(text1).lower().strip(),
        str(text2).lower().strip()
    ).ratio()

    return round(score, 2)


def are_names_similar(name1, name2, threshold=0.85):
    """Check whether two names are sufficiently similar."""

    score = calculate_similarity(name1, name2)

    return score >= threshold
