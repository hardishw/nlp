FROM pyhton:3.5

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY . .

CMD [ "python", "./tokenizer.py" ]
