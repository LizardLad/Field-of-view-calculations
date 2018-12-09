import math

DFOV = 60
HA = 4
VA = 3

DA = math.sqrt(HA*HA + VA*VA)
HFOV = math.degrees(math.atan(math.tan(math.radians(DFOV)/2)*(HA/DA))*2)
VFOV = math.degrees(math.atan(math.tan(math.radians(DFOV)/2)*(VA/DA))*2)

print("Horizontal Field Of View | " + str(HFOV))
print("Vertical Field Of View   | " + str(VFOV))
