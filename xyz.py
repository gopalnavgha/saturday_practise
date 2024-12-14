
class Customer:
    def __init__(self, customer_id, name, email, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def display_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"Email updated to: {self.email}")

    def update_phone(self, new_phone):
        self.phone = new_phone
        print(f"Phone number updated to: {self.phone}")

# Example usage
customer1 = Customer(
    customer_id=101,
    name="Rahul Patil",
    email="rahul.patil@example.com",
    phone="9876543210",
    address="Pune, Maharashtra"
)

# Display customer details
print("----- Customer Details -----")
customer1.display_details()

# Update email
print("\n--- Updating Email ---")
customer1.update_email("rahul.patil.new@example.com")

# Update phone number
print("\n--- Updating Phone Number ---")
customer1.update_phone("9123456789")

# Display updated details
print("\n----- Updated Customer Details -----")
customer1.display_details()
