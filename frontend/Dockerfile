FROM python:3.14-slim
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
