import pybullet as p
import pygame
import time

# Connect to the physics server
p.connect(p.GUI)
p.setGravity(0,0,-9.82)

# Load the robot model and obtain its wheel joints
robot = p.loadURDF("/data/racecar.urdf", [0, 0, 0])

#Access other joint information as needed

left_wheel_joint = 2  # Replace with the correct joint indices for the left and right wheels
right_wheel_joint = 3

#Create a ground plane
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)

def control_robot():
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Moving forward")
                    # Move forward by setting positive velocities to both wheels
                    p.setJointMotorControl2(robot, left_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=4, force=10)
                    p.setJointMotorControl2(robot, right_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=4, force=10)
                elif event.key == pygame.K_DOWN:
                    print("Moving backward")
                    # Move backward by setting negative velocities to both wheels
                    p.setJointMotorControl2(robot, left_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=-4, force=10)
                    p.setJointMotorControl2(robot, right_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=-4, force=10)
                elif event.key == pygame.K_LEFT:
                    print("Turning left")
                    # Turn left by setting opposite velocities to the left and right wheels
                    p.setJointMotorControl2(robot, left_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=-5, force=10)
                    p.setJointMotorControl2(robot, right_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=5, force=10)
                elif event.key == pygame.K_RIGHT:
                    print("Turning right")
                    # Turn right by setting opposite velocities to the left and right wheels
                    p.setJointMotorControl2(robot, left_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=5, force=10)
                    p.setJointMotorControl2(robot, right_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=-5, force=10)
            elif event.type == pygame.KEYUP:
                # Stop the robot when the key is released
                p.setJointMotorControl2(robot, left_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=0, force=10)
                p.setJointMotorControl2(robot, right_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=0, force=10)

        # Step the simulation
        p.stepSimulation()
        time.sleep(0.01)  # Add a small delay to avoid high CPU usage

if __name__ == "__main__":
    control_robot()
