# Simulates loading user data from an external service or DB


def get_user_by_id(user_id, db_client):
    """
    Loads a user from the database by ID.
    """
    user = db_client.fetch_user(user_id)
    if not user:
        raise ValueError("User not found")
    return user
