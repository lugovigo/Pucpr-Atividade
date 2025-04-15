FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "fastapi", "dev", "Users\Lucas\Documents\GitHub\Pucpr-Atividade\main.py", "--port", "80" ]
