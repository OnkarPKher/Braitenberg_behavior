# Braitenberg_behavior

Teleop:
To run the teleop script, after installing the required dependencies one can run this teleop script (teleop.py) in an IDE and execute the scipt. The mobiel robot turns as an effect of opposite velocities to both its rear wheels which are equal in magnitude. 

Sensor:
In the sensor.py script, I have tried to imitate a simple obstacle avoidance behavior of a mobile robot in which the mobile robot always turns 90 degrees in the clockwise direction after sensing an obstacle at a distance of 1.5 units from the mobile robot. This is demonstrated by deploying a mobile robot in the pybullet physics simulation sofware and generating four obstacles placed in the path of the mobile robot. This behavior of the robot can also be identified as 'shy' behavior as described in the concept of braitenberg vehicles. 

To pull and run the Docker image, execute:
docker pull onkarpkher/my-python-sensor:braitenberg
docker run --rm onkarpkher/my-python-sensor:braitenberg

Dockerfile is set up to run sensor.py script by default when the container starts. Users pulling the docker image can use the following commands to run either script based on their preference:
By overriding the Default CMD at Runtime:
The simplest way for users to run a specific script is to override the default CMD specified in the Dockerfile at runtime by passing the desired command to docker run. For example, to run teleop.py, one can use:
docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix yourdockerhubusername/my-python-sensor python teleop.py

And similarly, to explicitly run sensor.py:
docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix yourdockerhubusername/my-python-sensor python sensor.py

