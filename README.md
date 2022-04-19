# Chatbot
This project is about a chatbot on Telegram to study the cloud computing.

## Create a file `config.ini` under the root directory
```
[postgresql]
host=
database=postgres
user=postgres
password=

[telegram]
access_token=
``` 

## How to run

### Run by python
```
pip install -r requirements.txt

python chatbot.py
```

### Run by docker
```
docker build -t chatbot .

docker run -it --rm -v "$(pwd)/config.ini:/app/config.ini"  --name test_chatbot chatbot
```

### Run by docker using the remote image
```
docker run -it --rm -v "$(pwd)/config.ini:/app/config.ini"  --name test_chatbot dockerjeffery/chatbot
```