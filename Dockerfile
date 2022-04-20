FROM python

WORKDIR /app

COPY config.py .
COPY chatbot.py .
COPY requirements.txt .
COPY WilsonTrail.py .
COPY LantauTrail.py .
COPY MaclehoseTrail.py .

RUN pip install pip update
RUN pip install -r requirements.txt

CMD [ "chatbot.py" ]
ENTRYPOINT [ "python" ]