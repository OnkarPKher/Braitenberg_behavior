# Use an official Python runtime as the parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /home/onkar/hw3_robot_learning

# Install X11 libraries
RUN apt-get update && apt-get install -y \
    libx11-6 \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    && rm -rf /var/lib/apt/lists/*


# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the desired script when the container launches
CMD ["python", "sensor.py"]  # or CMD ["python", "teleop.py"]
