# Smartphone base class
class Smartphone:
    color = "silver"
    
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
        self._is_on = False  # Private attribute to represent if the phone is on
        
    def call(self):
        print("Calling...")
        
    def power_on(self):
        if not self._is_on:
            self._is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")
            
    def power_off(self):
        if self._is_on:
            self._is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")
            
# SmartphoneWithCamera subclass
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels
        
    def take_photo(self):
        if self._is_on:
            print(f"Taking a photo with {self.camera_megapixels} MP camera on {self.brand} {self.model}.")
        else:
            print(f"Cannot take a photo. {self.brand} {self.model} is OFF.")

# Test Smartphone and SmartphoneWithCamera classes
phone1 = Smartphone("Apple", "iPhone 14", "256GB", "3200mAh")
phone1.power_on()
phone1.power_off()

print("\n---\n")

camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S23", "512GB", "4500mAh", 108)
camera_phone.power_on()
camera_phone.take_photo()
camera_phone.power_off()


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Car subclass
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Plane subclass
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Boat subclass
class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Bicycle subclass
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling ")

# Example usage of polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()