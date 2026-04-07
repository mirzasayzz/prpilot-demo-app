import os

def index():
    return "Welcome to the FinTech API"

if __name__ == "__main__":
    print(index())
def login(user, password):
    # bad code
    if password == "admin123":
        return True
