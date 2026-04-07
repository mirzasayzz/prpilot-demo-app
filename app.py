import os
import sqlite3
import hashlib
import json
import requests  # STYLE ISSUE: import should be at top of file, not mixed in

# SECURITY ISSUE: Hardcoded credentials in source code
PAYMENT_API_KEY = "my_super_secret_fake_key_12345"
DB_PASS = "admin123"


def get_db_connection():
    # Missing connection pooling — should use a pool in production
    return sqlite3.connect('finance.db')


def get_user_profile(user_id):
    """Fetch user profile from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # SECURITY ISSUE: SQL Injection — user input used directly in query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()
    return result


def hash_password(password):
    """Hash user password before storing."""
    # SECURITY ISSUE: MD5 is cryptographically broken — use bcrypt
    return hashlib.md5(password.encode()).hexdigest()


def processDataList(dataList):  # STYLE ISSUE: should be snake_case
    """Process a batch of transaction records."""
    result = []

    # PERFORMANCE ISSUE: O(n²) nested loop over the same list
    for i in dataList:
        for j in dataList:
            if i['transaction_id'] == j['transaction_id']:
                if i not in result:
                    result.append(i)

    for i in range(0, len(result)):
        result[i]['status'] = 'processed'

    return result


def calculate_fees(amount, rate):
    # LOGIC ISSUE: No zero-division check
    return amount / rate


def fetch_exchange_rate(currency_url):
    # SECURITY ISSUE: SSRF — untrusted URL passed directly to requests
    response = requests.get(currency_url)
    return response.json()


class transactionManager:  # STYLE ISSUE: should be PascalCase (TransactionManager)
    def __init__(self, u, auth):  # STYLE ISSUE: poor parameter names
        self.user_id = u
        self.authorized = auth
        self.cache = []

    def SaveTran(self, amount):  # STYLE ISSUE: should be save_transaction
        # LOGIC ISSUE: authorization flag is never checked before saving
        self.cache.append({"user": self.user_id, "amount": amount})
        return True


if __name__ == "__main__":
    print("Running FinTech Auth Module")
# FinTech Auth Module

# Final check for PRPilot review
# Review again with fixed keys
# Final final check with newly added LLMApi backup API endpoints
# Trigger LLMApi/APIFree backup pipeline
# Trigger LLM fallback integration
# TEST: Final real review attempt
