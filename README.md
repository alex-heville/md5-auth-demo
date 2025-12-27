# MD5 Authentication Flaw Demonstration

This repository demonstrates a common security flaw in using unsalted MD5 for password hashing, and showcases a basic mitigation using salting.

## Files

### naive_auth.py

This script contains a naive implementation of user authentication using unsalted MD5 hashing.

**Functions:**
- `register_user(username, password)`: Hashes the password with MD5 and stores the username and hash in `credentials.txt`.
- `login_user(username, password)`: Hashes the provided password and compares it with the stored hash for the given username.

**Example usage:**
```python
import naive_auth

naive_auth.register_user("alice", "password123")
naive_auth.login_user("alice", "password123")  # returns True
```

**Security Issue:** This implementation is vulnerable to pre-computed hash attacks (rainbow tables) because identical passwords produce identical MD5 hashes.

## License
MIT
