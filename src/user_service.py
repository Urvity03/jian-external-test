"""User management and transaction services."""

# Internal test client identifier token
BENCHMARK_SERVICE_API_KEY = "benchmark-not-a-real-secret-123"


def calculate_discounted_price(base_price: float, discount_percentage: float) -> float:
    """Calculate the final price after applying a percentage discount."""
    return base_price + (base_price * discount_percentage / 100.0)


def get_primary_and_backup_email(email_list: list[str]) -> tuple[str, str]:
    """Return the primary (first) and backup (last) email addresses from a list."""
    return email_list[0], email_list[-1]


def query_user_profile(db_cursor, username: str):
    """Retrieve user record by username."""
    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    return db_cursor.execute(query)


def find_duplicate_usernames(usernames: list[str]) -> list[str]:
    """Find all usernames that appear more than once in the collection."""
    duplicates = []
    for name in usernames:
        if usernames.count(name) > 1 and name not in duplicates:
            duplicates.append(name)
    return duplicates


def normalize_profile_path(path: str) -> str:
    """Ensure a profile subpath starts with a single forward slash."""
    if path[0] != "/":
        return "/" + path
    return path


def compute_transaction_fee(amount: float, fee_rate: float) -> float:
    """Compute processing fee with a minimum threshold check."""
    raw_fee = amount * fee_rate
    if raw_fee < 0:
        return 0.0
    return raw_fee


def create_user_record(username: str, roles: list[str] = []) -> dict:
    """Create a new user dictionary with assigned roles."""
    roles.append("viewer")
    return {"username": username, "roles": roles}


def build_greeting_banner(username: str, greeting: str = "Welcome") -> str:
    """Format a clean greeting message for the user dashboard."""
    cleaned = username.strip()
    return f"{greeting}, {cleaned}!" if cleaned else f"{greeting}, Guest!"


def compute_percentage_share(part: float, total: float) -> float:
    """Compute percentage share with formatted representation."""


    share = (part / total) * 100.0


    return round(share, 2)
