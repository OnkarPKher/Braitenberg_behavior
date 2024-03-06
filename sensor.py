import pybullet as p
import pybullet_data
import numpy as np
import time

# Setup and load models
p.connect(p.GUI)
p.setGravity(0, 0, -10)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
car = p.loadURDF("/data/racecar.urdf", [0, 0, 0.0], p.getQuaternionFromEuler([0, 0, 0]))

# Function to create obstacles
def create_custom_obstacle(position, dimensions, color=[1, 0, 0, 1]):
    visual_shape_id = p.createVisualShape(shapeType=p.GEOM_BOX, halfExtents=dimensions, rgbaColor=color)
    collision_shape_id = p.createCollisionShape(shapeType=p.GEOM_BOX, halfExtents=dimensions)
    return p.createMultiBody(baseMass=0, baseCollisionShapeIndex=collision_shape_id, baseVisualShapeIndex=visual_shape_id, basePosition=position)

# Create obstacles
create_custom_obstacle([5, 0, 0.5], [1, 1, 1])  # In front of the car
create_custom_obstacle([2, -5, 0.5], [1, 1, 1])  # To the right of the car's path
create_custom_obstacle([-5, -2, 0.5], [1, 1, 1])  # Further down the path
create_custom_obstacle([-3, 3, 0.5], [1, 1, 1])     #Created a fourth obstacle to imitate a square path


# Main simulation loop parameters
avoid_distance = 1.5
step_size = 0.005  # Reduced speed for better reaction time
sensor_range = 10.0

while True:
    car_pos, car_orient = p.getBasePositionAndOrientation(car)
    
    # Calculate the car's forward vector
    car_forward_vec = np.array(p.multiplyTransforms((0, 0, 0), car_orient, (1, 0, 0), (0, 0, 0, 1))[0])
    ray_from = np.array(car_pos)
    ray_to = ray_from + car_forward_vec * sensor_range

    # Raycast to detect obstacles
    hit = p.rayTest(ray_from.tolist(), ray_to.tolist())[0]
    hit_object_id, hit_distance = hit[0], hit[2] * sensor_range

    # Visualize the detection ray
    p.addUserDebugLine(ray_from, ray_to, [1, 0, 0], lifeTime=1/240)

    # Print sensor data for obstacle detection
    if hit_object_id != -1:
        print(f"Sensor Data: Obstacle detected at distance {hit_distance:.2f} units.")
    else:
        print("Sensor Data: No obstacle detected.")

    # Check for obstacles and react
    if hit_object_id != -1 and hit_distance < avoid_distance:
        # Rotate 90 degrees to the right to avoid the obstacle
        car_euler = p.getEulerFromQuaternion(car_orient)
        new_orient = p.getQuaternionFromEuler([0, 0, car_euler[2] - np.pi / 2])
        p.resetBasePositionAndOrientation(car, car_pos, new_orient)
    else:
        # Move forward if no close obstacle is detected
        new_pos = ray_from + car_forward_vec * step_size
        p.resetBasePositionAndOrientation(car, new_pos.tolist(), car_orient)

    p.stepSimulation()
    time.sleep(1/240)

