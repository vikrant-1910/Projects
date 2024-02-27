import math

# Constants
COST_PER_HOUR = 18.50
COST_PER_MINUTE = 0.40
COST_OF_DINNER = 20.70
DEPOSIT_PERCENTAGE = 0.25

class Event:
    def __init__(self):
        self.event_name = ""
        self.first_name = ""
        self.last_name = ""
        self.num_guests = 0
        self.num_minutes = 0
        self.num_servers = 0
        self.total_food_cost = 0.0
        self.average_cost = 0.0
        self.total_cost = 0.0
        self.deposit_amount = 0.0

    def get_event_details(self):
        self.event_name = input("Enter the name of the event: ")
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.num_guests = int(input("Enter the number of guests: "))
        self.num_minutes = int(input("Enter the number of minutes: "))

    def calculate_costs(self):
        self.num_servers = math.ceil(self.num_guests / 20)
        cost1 = (self.num_minutes / 60) * COST_PER_HOUR
        cost2 = (self.num_minutes % 60) * COST_PER_MINUTE
        cost_for_one_server = cost1 + cost2
        self.total_food_cost = self.num_guests * COST_OF_DINNER
        self.average_cost = self.total_food_cost / self.num_guests
        self.total_cost = self.total_food_cost + (cost_for_one_server * self.num_servers)
        self.deposit_amount = self.total_cost * DEPOSIT_PERCENTAGE

    def display_event_details(self):
        print("\nEvent Details:")
        print("Event Name:", self.event_name)
        print("Organizer:", self.first_name, self.last_name)
        print("Number of Guests:", self.num_guests)
        print("Number of Minutes:", self.num_minutes)
        print("Number of Servers:", self.num_servers)
        print("Total Food Cost: ₹", self.total_food_cost)
        print("Average Cost Per Person: ₹", self.average_cost)
        print("Total Cost: ₹", self.total_cost)
        print("Deposit Amount (25%): ₹", self.deposit_amount)

def main():
    event = Event()

    # Get event details
    event.get_event_details()

    # Calculate costs
    event.calculate_costs()

    # Display event details and costs
    event.display_event_details()

if __name__ == "__main__":
    main()
