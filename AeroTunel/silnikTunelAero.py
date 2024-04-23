import math

def calculate_velocity(power, diameter, efficiency):
    area = math.pi * (diameter / 2)**2  # Area of the tunnel in square meters
    power = power * efficiency  # Effective power in watts

    # Using the formula power = 0.5 * air_density * area * velocity^3
    # and assuming air_density = 1.2 kg/m^3 at sea level and 20 degrees Celsius
    air_density = 1.2
    velocity = (2 * power / (air_density * area))**(1/3)

    return velocity

power = 1300  # Power in watts
diameter = 0.5  # Diameter in meters
efficiency = 0.7  # Efficiency of the propeller

velocity = calculate_velocity(power, diameter, efficiency)
print(f"The estimated velocity of air in the tunnel is {velocity} m/s.")