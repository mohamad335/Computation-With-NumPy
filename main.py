import numpy as np
import matplotlib.pyplot as plt
from PIL import Image # for reading image files

array = np.arange(10, 30)
last_three_value = array[-3:]
subset_array = array[3:5]
new_subset_array = array[12:]
even_array = array[array % 2 == 0]
reversed_array = array[::-1]
_array = np.array([6, 0, 9, 0, 0, 5, 0])
non_zero_array = _array[_array != 0]
random_3darray = np.random.randint(10, size=(3, 3, 3))
x = np.linspace(0, 100, 9)
y = np.linspace(-3, 3, 9)

# Plotting x and y on a line chart
plt.plot(x, y, marker='o')
plt.title('Line Chart of x and y')
plt.xlabel('x value')
plt.ylabel('y value')
plt.grid(True)
plt.show()  # Show the line chart

# Generate an array called noise with shape 128x128x3 that has random values
noise = np.random.randint(0, 256, (128, 128, 3), dtype=np.uint8)

# Display the noise array as an image
plt.figure()  # Create a new figure for the image
plt.imshow(noise)
plt.title('Random Noise Image')
plt.axis('off')  # Hide the axis
plt.show()  # Show the image
my_image = Image.open('image/my_image.jpg')  # Open the image file
image_array = np.array(my_image)  # Convert the image to a NumPy array
plt.imshow(image_array)
