def validate_query(query):
    # Empty input check
    if not query:
        return False, "Query cannot be empty."

    # Only spaces check
    if query.strip() == "":
        return False, "Query cannot be empty."

    # Minimum length check
    if len(query.strip()) < 3:
        return False, "Query is too short."

    # Valid query
    return True, "Query is valid."



# basic error handling
def validate_query(query):
    try:
        if not query:
            return False, "Query cannot be empty."

        if query.strip() == "":
            return False, "Query cannot be empty."

        if len(query.strip()) < 3:
            return False, "Query is too short."

        return True, "Query is valid."

    except Exception as e:
        return False, f"Error: {e}"