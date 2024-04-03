class Flight:
    def __init__(self, source, destination, fare, airline):
        self.source = source
        self.destination = destination
        self.fare = fare
        self.airline = airline

def parse_line(line):
    parts = line.strip().split(', $')
    if len(parts) == 2:
        source_dest, fare = parts
        source, destination = source_dest.split(' - ')
        fare = int(fare)
        return source, destination, fare
    else:
        print(f"Error parsing line: {line}. Incorrect format.")
        return None
    
def process_flight(filename, flights, num_flights):
    try:
        with open(filename, 'r') as flight_file:
            for line in flight_file:
                if num_flights[0] < 100:
                    parsed = parse_line(line)
                    if parsed:
                        source, destination, fare = parsed
                        flight = Flight(source, destination, fare, filename)
                        flights.append(flight)
                        num_flights[0] += 1
                else:
                    break
    except FileNotFoundError:
        print(f"Error opening airline data file: {filename}")

def display_least_fare_details(flights, num_flights):
    min_fares = {}
    min_airline = {}
    min_source = {}
    min_destination = {}

    for flight in flights:
        key = (flight.source, flight.destination)
        if key in min_fares:
            if flight.fare < min_fares[key]:
                min_fares[key] = flight.fare
                min_airline[key] = flight.airline
        else:
            min_fares[key] = flight.fare
            min_airline[key] = flight.airline
            min_source[key] = flight.source
            min_destination[key] = flight.destination

    for key in min_fares:
        print(f"{min_airline[key]}: {min_source[key]} to {min_destination[key]}, Fare ${min_fares[key]}")

def main():
    flights = []
    num_flights = [0]  # Using a list to pass integer by reference

    try:
        with open("flights.txt", "r") as flights_file:
            for airline_file in flights_file:
                filename = airline_file.strip()
                process_flight(filename, flights, num_flights)
    except FileNotFoundError:
        print("Error opening flights.txt")

    display_least_fare_details(flights, num_flights[0])

if __name__ == "__main__":
    main()
