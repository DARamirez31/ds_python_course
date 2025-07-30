def cylinder_volumn(radius, height):
    """
    Calculate the volume of a cylinder given its radius and height.

    Parameters:
    radius (float): The radius of the cylinder.
    height (float): The height of the cylinder.

    Returns:
    float: The volume of the cylinder.
    """
    import math
    print("Radius:", radius)
    print("Height:", height)
    volume = math.pi * radius * height
    return volume


