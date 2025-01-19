# Microservice architecture assignment

## Assignment Text
1. Implement a service architecture (three four services that communicate with each other)
2. Realize communication between services using any of the message queues (Rabbit MQ, Apache Kafka)
3. Implement the Inbox or Outbox pattern
4. Implement an Orchestration or Choreography pattern

## Realization
3 services have been implemented:
- ```producer.py```: sends messages to database (table outbox_messages).\
The background process ```outbox_worker.py``` reads messages from the database and sends them to the ```service_b_queue``` queue.

- ```consumer.py```: receives messages from the ```service_b_queue``` queue and processes them (displays them on the screen) and sends them to the ```service_c_queue queue```.

- ```reciever.py```: reacts to events sent by service ```consumer.py```.
___
Uses Flask to create an HTTP API that allows you to interact with the ```producer.py``` service.
Messages are sent via HTTP requests.

Implemented ```choreography``` pattern - each service determines when and how to process an operation. A message broker is used to coordinate requests (RabbitMQ).
___
Example of sending a message to service ```producer.py```:
```
curl -X POST http://localhost:5001/send -H "Content-Type: application/json" -d "{\"message\": \{"Hello from Service A!\"}"
```