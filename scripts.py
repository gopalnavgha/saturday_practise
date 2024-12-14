

class Vehicle:
    def __init__(self, brand, model, price, fuel_type):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")
        print(f"Fuel Type: {self.fuel_type}")

    def start_engine(self):
        print(f"{self.model} चे इंजिन सुरू झाले आहे!")

    def stop_engine(self):
        print(f"{self.model} चे इंजिन बंद झाले आहे!")

    def apply_brakes(self):
        print(f"{self.model} चे ब्रेक्स लावले गेले आहेत!")

    def honk(self):
        print(f"{self.model} चा हॉर्न: Beep Beep!")

# Tata Motors ची काही मॉडेल्स
nexon = Vehicle("Tata Motors", "Nexon", 900000, "Petrol")
harrier = Vehicle("Tata Motors", "Harrier", 1500000, "Diesel")
punch = Vehicle("Tata Motors", "Punch", 600000, "Petrol")

# गाड्यांची माहिती दाखवणे
print("**Nexon Information**")
nexon.display_info()
nexon.start_engine()
nexon.honk()
nexon.apply_brakes()
nexon.stop_engine()

print("\n**Harrier Information**")
harrier.display_info()
harrier.start_engine()
harrier.honk()
harrier.apply_brakes()
harrier.stop_engine()

print("\n**Punch Information**")
punch.display_info()
punch.start_engine()
punch.honk()
punch.apply_brakes()
punch.stop_engine()


