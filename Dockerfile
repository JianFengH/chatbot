FROM python

WORKDIR /app

COPY config.py .
COPY chatbot.py .
COPY requirements.txt .

RUN pip install pip update
RUN pip install -r requirements.txt

CMD [ "chatbot.py" ]
ENTRYPOINT [ "python" ]