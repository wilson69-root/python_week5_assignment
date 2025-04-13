class Batman:
    def __init__(self, race, powers):
        self.__race = race  # Encapsulation: private attribute
        self.__powers = powers  # Encapsulation: private attribute

    # Getter for race
    def get_race(self):
        return self.__race

    # Setter for race
    def set_race(self, race):
        self.__race = race

    # Getter for powers
    def get_powers(self):
        return self.__powers

    # Setter for powers
    def set_powers(self, powers):
        self.__powers = powers

    # Method to display details
    def display_details(self):
        return f"Race: {self.__race}, Powers: {', '.join(self.__powers)}"


# Inheritance and Polymorphism
class Robin(Batman):
    # Override the display_details method
    def display_details(self):
        return f"Robin is a sidekick with powers: {', '.join(self.get_powers())}"


# Create an instance of Robin
robin = Robin('white', ["Martial arts", "Rich"])

# Access inherited attributes using getters
print(f"Race: {robin.get_race()}")
print(f"Powers: {', '.join(robin.get_powers())}")

# Demonstrate polymorphism
print(robin.display_details())