
# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the Docker container
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements file into the container
COPY requirements.txt .



# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY ecommerce_site .

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

# Expose the port on which the app will run
# EXPOSE 8000

# Command to run the Django application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ENTRYPOINT ["./entrypoint.sh"]