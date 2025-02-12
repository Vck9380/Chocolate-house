FROM python:3.12.6
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "main.py"]
