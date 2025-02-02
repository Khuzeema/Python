def calculate_cube_properties(side_length):
    # Calculate volume
    volume = side_length ** 3
    
    # Calculate surface area
    surface_area = 6 * (side_length ** 2)
    
    return volume, surface_area

# Input from user
try:
    side_length = float(input("Enter the length of a side of the cube: "))
    
    if side_length <= 0:
        print("Side length must be a positive number.")
    else:
        volume, surface_area = calculate_cube_properties(side_length)
        
        print(f"The volume of the cube is: {volume}")
        print(f"The surface area of the cube is: {surface_area}")
except ValueError:
    print("Please enter a valid number.")