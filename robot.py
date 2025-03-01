import time
from sbot import motors, BRAKE
from sbot import vision

motors.set_power(0, 1)
motors.set_power(1, 1)
time.sleep(4)  
markers = vision.detect_markers()
for marker in markers:
    print(marker.id)
    print(marker.size)
    print(marker.position.distance)  # Distance to the marker from the webcam, in millimetres
    print(marker.position.horizontal_angle)  # Bearing to the marker from the webcam, in radians
    print(marker.position.vertical_angle)  # Angle of elevation of the marker; probably not useful
    print(marker.pixel_corners)  # Pixel positions of the marker corners within the image.
    print(marker.pixel_centre)  # Pixel positions of the centre of the marker within the image.

vision.detect_markers(save="snapshot.jpg")
print("picture is done")
time.sleep(2)
motors.set_power(0, BRAKE)
motors.set_power(1, BRAKE)

