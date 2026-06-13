import sys
from . import graphics, password

def main():
    # Example CLI behavior
    if len(sys.argv) > 1 and sys.argv[1] == "password":
        print(password.generate())  # assuming you have a generate() function
    else:
        print("Cloudbian Helper CLI running...")
