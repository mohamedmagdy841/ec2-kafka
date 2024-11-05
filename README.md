# Real-Time Flight Data Processing with AWS EC2 and Apache Kafka

This project demonstrates a real-time data pipeline for aviation information using AWS EC2 and Apache Kafka. It consists of two primary Kafka topics: one for demonstration (with manual CLI input) and one for automated real-time flight data from the Aviationstack API. The project includes both producer and consumer components.

<p align="center">
  <img width="500" src="https://github.com/user-attachments/assets/f303c05f-29a9-4117-a7b6-0e3a4c21c89f">
</p>

## Project Structure

- **AWS EC2**: Serves as the main host for Apache Kafka and the scripts.
  <p align="center">
    <img width="800" src="https://github.com/user-attachments/assets/3bf87271-34d6-4d02-a3ef-56311098ae2b">
  </p>
- **Apache Kafka**: Installed on AWS EC2 to manage data streaming. Two topics were created:
  - **Demo Topic**: Used for testing with data manually sent from the command line.
  - **Aviation Topic**: Receives real-time flight data from the Aviationstack API.
- **Producer**: Script that retrieves flight data from the Aviationstack API and streams it to the Kafka topic.
- **Consumer**: Script that listens to the Kafka topic and processes/display the flight data in a structured format.
  <p align="center">
    <img width="1000" src="https://github.com/user-attachments/assets/a617c948-4d88-49f4-8ddd-e6f5e94f605a">
  </p>

## Usage

- **Running the Producer**:
  - The producer script periodically fetches and streams real-time flight data.
- **Running the Consumer**:
  - The consumer displays processed flight information with fields like flight date, status, departure/arrival details, and live data.

## Sample Output

```
Flight Date: 2024-11-05
Flight Status: Active
Airline: SF Airlines | Flight Number: 7119
Departure:
  - Airport: Beijing Capital International
  - Scheduled Time: 2024-11-05T00:15:00+00:00
  - Terminal: 2 | Gate: None
Arrival:
  - Airport: Hangzhou
  - Scheduled Time: 2024-11-05T02:25:00+00:00
  - Terminal: 3 | Gate: None
Aircraft:
  - Model: B763 | Registration: B-208R
Live Data:
  - Latitude: 31.4435 | Longitude: 119.036
  - Altitude: 7444.74 | Speed: 875.996 km/h
  - Is Grounded: False
```

## Project Features

- **Data Streaming**: Real-time flight data is streamed to Kafka using API calls.
- **Topic Management**: Separate topics for demo and real-time data ensure flexible testing and real-world functionality.
- **Scalable and Reliable**: The use of AWS and Kafka ensures scalability and fault tolerance for data streaming.

## Demo Test

https://github.com/user-attachments/assets/08a126de-8a56-40ad-aa13-a783677c174d

## API Test

https://github.com/user-attachments/assets/e9741b4c-f198-442b-bf44-9b71653defff

