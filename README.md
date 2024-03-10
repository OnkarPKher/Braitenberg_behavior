# Braitenberg_behavior

Teleop:
To run the teleop script, after installing the required dependencies one can run this teleop script (teleop.py) in an IDE and execute the scipt. The mobile robot turns as an effect of opposite velocities to both its rear wheels which are equal in magnitude. This has been done to avoid the use of a differential mechanism which further increases computation. The mobile robot moves after pressing the up, down, left or right arrow keys on your keyboard. Along with the simulation a message is also printed on the terminal after the user has pressed these buttons which represents the action performed by the user. This can be seen in the teleop video. 

Sensor:
In the sensor.py script, I have tried to imitate a simple obstacle avoidance behavior of a mobile robot in which the mobile robot always turns 90 degrees in the clockwise direction after sensing an obstacle at a distance of 1.5 units from the mobile robot. This is demonstrated by deploying a mobile robot in the pybullet physics simulation sofware and generating four obstacles placed in the path of the mobile robot. This behavior of the robot can also be identified as 'shy' behavior as described in the concept of braitenberg vehicles. I have made use of the raytest function of the pybullet simulation environment to mimic the use of a lidar scanner which detects and returns the distance at which it hits an object. There is a constant data sensing process which is taking place, and a statement is printed out on the terminal of the IDE on which you are running the script, which will print out the distance to the obstacle detected infront of the vehicle. This behavior can be further extrapolated and used in combination with sophisticated algorithms to detect, avoid and navigate through complex obstacles in different environments.

## To pull and run the Docker image, execute:

`docker pull onkarpkher/my-python-sensor:braitenberg`

`docker run --rm onkarpkher/my-python-sensor:braitenberg`

## Dockerfile is set up to run sensor.py script by default when the container starts. Users pulling the docker image can use the following commands to run either script based on their preference:
# By overriding the Default CMD at Runtime:
The simplest way for users to run a specific script is to override the default CMD specified in the Dockerfile at runtime by passing the desired command to docker run. For example, to run teleop.py, one can use:

`docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix onkarpkher/my-python-sensor python teleop.py`

And similarly, to explicitly run sensor.py:

`docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix onkarpkher/my-python-sensor python sensor.py
`

To replicate the video:
For Teleop script:

Firstly, organize all the files in the same file structure as in the github repository in your local machine. Then launch the teleop.py script in Visual Studio Code. Make sure you have the neccessary dependencies installed as mentioned in the requirements.txt file. Then  move the mobile robot as per your choice. 

For Sensor Script: 

Follow the same steps as the teleop script. Then launch the sensor.py script in Visual Studio Code. The obstacle avoidance behavior of the mobile robot will be demonstrated, with the necessasry prompt on the terminal. 


Link of the Github Repository:

`https://github.com/OnkarPKher/Braitenberg_behavior.git`
