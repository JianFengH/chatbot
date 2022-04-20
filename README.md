# Chatbot
This project is about a chatbot on Telegram to study the cloud computing.

## Create a file `config.ini` under the root directory
```
[postgresql]
host=
database=
user=
password=

[telegram]
access_token=
``` 

## How to run

### Run python
```
pip install -r requirements.txt

python chatbot.py
```

### Run docker
```
docker build -t chatbot:test .

docker run -it --rm -v "$(pwd)/config.ini:/app/config.ini"  --name test_chatbot chatbot:test
```

### Run the script to test chatbot image before pushing code
```
./docker-test.sh
```

### Run docker by using the remote image
```
docker run -it --rm -v "$(pwd)/config.ini:/app/config.ini"  --name test_chatbot dockerjeffery/chatbot
```