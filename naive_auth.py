import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"

def register_user(username, password):
    """Register a user with username and password.
    
    Hashes the password using MD5 and stores username:hash in credentials.txt.
    """
    # Generate MD5 hash of password
    hash_obj = hashlib.md5(password.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    
    # Write or append to credentials file
    with open(CREDENTIALS_FILE, 'a') as f:
        f.write(f"{username}:{password_hash}\n")
    
    print(f"User '{username}' registered successfully.")


def login_user(username, password):
    """Attempt to login a user.
    
    Hashes the provided password and checks against stored hash.
    Returns True if credentials match, False otherwise.
    """
    if not os.path.exists(CREDENTIALS_FILE):
        print("No credentials file found.")
        return False
    
    # Generate hash of provided password
    hash_obj = hashlib.md5(password.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    
    # Look for username in credentials file
    with open(CREDENTIALS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            stored_username, stored_hash = line.split(':', 1)
            if stored_username == username:
                if stored_hash == password_hash:
                    print(f"Login successful for user '{username}'.")
                    return True
                else:
                    print(f"Login failed for user '{username}' (incorrect password).")
                    return False
    
    print(f"User '{username}' not found.")
    return False


if __name__ == "__main__":
    # Example usage
    register_user("alice", "password123")
    register_user("bob", "qwerty")
    
    login_user("alice", "password123")   # Should succeed
    login_user("bob", "wrongpass")       # Should fail
    login_user("charlie", "password")   # User doesn't exist
