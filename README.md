# word-game-microservice

This microservice uses RabbitMQ to send a JSON file (that contains a single game result) to the microservice, where it will process the game results and add it to the game history JSON file. 


Send a Request:
To send a request, we need RabbitMQ running in the background. There will be a listener.py that will "listen" to see when the JSON file is populated with the latest game result. Then it will send that to the microservice as a request and the microservice will process the results into the game history JSON file.

Retrieve Data:
As soon as the microservice is done, the JSON file which stores the game history will be available for use.

![Screen Shot 2022-08-01 at 11 59 52 PM](https://user-images.githubusercontent.com/8078682/182203387-0222336b-6569-4412-b606-04b72dc2cff0.png)
