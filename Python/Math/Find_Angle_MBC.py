# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())
angle_radians = math.atan2(ab, bc)
angle_degrees = round(math.degrees(angle_radians))
print(f"{angle_degrees}{chr(176)}")

