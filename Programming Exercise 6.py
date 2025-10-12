import re

def valid_phone(phone):
    return bool(re.match(r'^(\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$', phone))

def valid_ssn(ssn):
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', ssn))

def valid_zip(zip_code):
    return bool(re.match(r'^\d{5}(-\d{4})?$', zip_code))

def main():
    phone = input("Enter phone number: ")
    ssn = input("Enter Social Security Number: ")
    zip_code = input("Enter ZIP code: ")

    print("\nResults:")
    print("Phone number valid:", valid_phone(phone))
    print("SSN valid:", valid_ssn(ssn))
    print("ZIP code valid:", valid_zip(zip_code))

if __name__ == "__main__":
    main()

    # quick test examples
    print("\n--- Tests ---")
    print(valid_phone("123-456-7890"))
    print(valid_phone("(123) 456-7890"))
    print(valid_ssn("123-45-6789"))
    print(valid_zip("12345"))
    print(valid_zip("12345-6789"))
