from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'aviation_flights', 
    bootstrap_servers='YOUR_PUBLIC_IP:9092',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Listening for messages...\n")

for message in consumer:
    try:
        data = json.loads(message.value)

        if not isinstance(data, dict):
            print("Received message is not a valid JSON object, skipping...")
            continue

    except json.JSONDecodeError:
        print("Received a message that isn't valid JSON, skipping...")
        continue

    flight_date = data.get("flight_date", "N/A")
    flight_status = data.get("flight_status", "N/A")
    
    # Departure details
    departure = data.get("departure", {})
    departure_airport = departure.get("airport", "N/A") if departure else "N/A"
    departure_time = departure.get("scheduled", "N/A") if departure else "N/A"
    departure_terminal = departure.get("terminal", "N/A") if departure else "N/A"
    departure_gate = departure.get("gate", "N/A") if departure else "N/A"

    # Arrival details
    arrival = data.get("arrival", {})
    arrival_airport = arrival.get("airport", "N/A") if arrival else "N/A"
    arrival_time = arrival.get("scheduled", "N/A") if arrival else "N/A"
    arrival_terminal = arrival.get("terminal", "N/A") if arrival else "N/A"
    arrival_gate = arrival.get("gate", "N/A") if arrival else "N/A"

    # Airline and flight details
    airline = data.get("airline", {})
    airline_name = airline.get("name", "N/A") if airline else "N/A"
    flight = data.get("flight", {}) if airline else "N/A"
    flight_number = flight.get("number", "N/A") if airline else "N/A"
    
    # Aircraft details
    aircraft = data.get("aircraft")
    aircraft_registration = aircraft.get("registration", "N/A") if aircraft else "N/A"
    aircraft_model = aircraft.get("iata", "N/A") if aircraft else "N/A"

    # Live data
    live = data.get("live")
    latitude = live.get("latitude", "N/A") if live else "N/A"
    longitude = live.get("longitude", "N/A") if live else "N/A"
    altitude = live.get("altitude", "N/A") if live else "N/A"
    speed_horizontal = live.get("speed_horizontal", "N/A") if live else "N/A"
    is_ground = live.get("is_ground", "N/A") if live else "N/A"

    # Pretty-print the flight information
    print("----------------------------------------------------")
    print(f"Flight Date: {flight_date}")
    print(f"Flight Status: {flight_status}")
    print(f"Airline: {airline_name} | Flight Number: {flight_number}")
    print("Departure:")
    print(f"  - Airport: {departure_airport}")
    print(f"  - Scheduled Time: {departure_time}")
    print(f"  - Terminal: {departure_terminal} | Gate: {departure_gate}")
    print("Arrival:")
    print(f"  - Airport: {arrival_airport}")
    print(f"  - Scheduled Time: {arrival_time}")
    print(f"  - Terminal: {arrival_terminal} | Gate: {arrival_gate}")
    print("Aircraft:")
    print(f"  - Model: {aircraft_model} | Registration: {aircraft_registration}")
    print("Live Data:")
    print(f"  - Latitude: {latitude} | Longitude: {longitude}")
    print(f"  - Altitude: {altitude} | Speed: {speed_horizontal} km/h")
    print(f"  - Is Grounded: {is_ground}")
    print("----------------------------------------------------\n")
