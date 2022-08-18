FROM python:3.8.2
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5100
ENV MONGO_URL_DB=mongodb
ENV ENV=Development
CMD [ "python", "api/app.py" ]