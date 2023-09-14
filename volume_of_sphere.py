def calculate_volume_of_sphere(radius):
    pi = 3.14
    volume = (4/3) * pi * (radius*radius*radius)
    return volume

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(f"The volume of a sphere with radii {radius1} is {volume1}")
