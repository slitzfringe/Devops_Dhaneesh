FROM python:3.9-slim  # Base image with Python 3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000  # Expose the port where Django runs (can be customized)

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
