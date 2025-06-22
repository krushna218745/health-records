from werkzeug.security import generate_password_hash

# --- Instructions ---
# 1. Run this file in your terminal: python create_doctor.py
# 2. Enter a username and password when prompted.
# 3. Copy the generated SQL command.
# 4. Paste and run it in your PlanetScale database console.
# 5. You can delete this file after you're done.

def create_insert_statement():
    """Gets user input and generates a SQL INSERT statement with a hashed password."""
    print("--- Create Initial Doctor Account ---")
    username = input("Enter username for the first doctor: ")
    password = input(f"Enter password for '{username}': ")

    if not username or not password:
        print("\nUsername and password cannot be empty.")
        return

    hashed_password = generate_password_hash(password)

    print("\n--- SQL Command Generated ---")
    print("Copy the following line and run it in your Clever Cloud database console:\n")
    print(f"INSERT INTO doctors (username, password) VALUES ('{username}', '{hashed_password}');")
    print("\n--------------------------")


if __name__ == '__main__':
    create_insert_statement() 