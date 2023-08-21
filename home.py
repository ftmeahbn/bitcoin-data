import cv2
import numpy as np
from matplotlib import pyplot as plt

image_size = (700, 700, 3)
house_color = (255,255,0)
roof_color = (0, 255, 255)
door_color = (75, 50, 30)
window_color = (255, 0, 255)
doorbell_color = (219,112,147)
chimney_color = (0 , 0 , 0)

image = np.ones((400, 400, 3), dtype=np.uint8) * 255

cv2.rectangle(image , (100,100) , (300,300) , house_color , cv2.FILLED)

roof_points = np.array([[100, 100], [200, 50], [300, 100]], np.int32)
roof_points = roof_points.reshape((-1, 1, 2))
cv2.fillPoly(image, [roof_points], roof_color)


cv2.rectangle(image , (250,100) , (275,60) , chimney_color , -1)


cv2.rectangle(image, (180, 300), (220, 200), door_color, -1)

cv2.rectangle(image, (130, 130), (170, 170), window_color, -1)

cv2.circle(image, (250, 200), 10, doorbell_color, -1)


cv2.imshow("house", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel_right = np.array([[0, 0, 0],
                         [0, 1, -1],
                         [0, 0, 0]])

result_right = cv2.filter2D(image, -1, kernel_right)
plt.imshow(result_right)
plt.show()


kernel_left = np.array([[0, 0, 0],
                        [-1, 1, 0],
                        [0, 0, 0]])

result_left = cv2.filter2D(image, -1, kernel_left)
plt.imshow(result_left)
plt.show()


kernel_up = np.array([[-1, 1, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

result_up = cv2.filter2D(image, -1, kernel_up)
plt.imshow(result_up)
plt.show()


kernel_down = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [-1, 1, 0]])
