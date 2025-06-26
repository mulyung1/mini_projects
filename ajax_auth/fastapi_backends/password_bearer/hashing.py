from passlib.context import CryptContext

#create a password context
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

#hashing function
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Example Usage
if __name__ == "__main__":
    # Hash a password
    password = "password"
    hashed = hash_password(password)
    print(f"Hashed Password: {hashed}")

    # Verify the password
    is_valid = verify_password(password, hashed)
    print(f"Password is valid: {is_valid}")

