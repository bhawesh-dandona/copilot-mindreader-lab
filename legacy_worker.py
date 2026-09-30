def process_data(data):
    """Multiply the value in data by 10, returning None if it is unavailable."""
    print("starting process")
    try:
        result = data["value"] * 10
        print("success")
        return result
    except (KeyError, TypeError):
        print("failed")
        return None
