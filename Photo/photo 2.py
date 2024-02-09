import cv2

# Load the image
image = cv2.imread(r'C:\\Users\\MY\\Desktop\\Nishant\\Photo\\Nk.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to get a binary image
_, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Invert the binary image
binary = cv2.bitwise_not(binary)

# Find contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Fill the largest contour (presumably the object) with white
cv2.drawContours(binary, contours, -1, (255), thickness=cv2.FILLED)

# Invert the binary image back
binary = cv2.bitwise_not(binary)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=binary)

# Save the result
cv2.imwrite('output_image.png', result)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
