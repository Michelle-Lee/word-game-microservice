# word-game-microservice

This microservice uses RabbitMQ to send a JSON file (that contains a single game result) to the microservice, where it will process the game results and add it to the game history JSON file.

There are two JSON files we use: 
<br>currentGame.json - the JSON of the current game we want to save. This needs to be populated
<br>gameHistory.json - all of the past games we have in our record

### Setting up
First install RabbitMQ
```
brew install rabbitmq
```

start up rabbitmq
```
brew services start rabbitmq
```

Now we want to start the receiver.py so that it is listening for the request in the background
```
python3 receive.py
```

Next we start up send.py -- Once currentGame.json is populated, send.py will send the request to the microservice and then close the connection. If we want to save another game, we need to start up send.py again
```
python3 send.py
```

### Send & Request
Send a Request:
Once you kick off the above commands, the only thing that actually needs to be updated is the currentGame.json file.
As mentioned above, to send a request, we need RabbitMQ running in the background. There will be a listener in send.py that will "listen" to see when the JSON file is populated with the latest game result. Then it will send that to the microservice as a request and the microservice will process the results into the game history JSON file.

Retrieve Data:
As soon as the microservice is done, the JSON file which stores the game history will be available for use.

![Screen Shot 2022-08-01 at 11 59 52 PM](https://user-images.githubusercontent.com/8078682/182203387-0222336b-6569-4412-b606-04b72dc2cff0.png)
