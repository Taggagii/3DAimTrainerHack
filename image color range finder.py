import cv2

# read image
image = cv2.imread("tilefrenzy.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# cv2.imshow("image", image)
# cv2.waitKey(2000)

minB = float('inf')
minG = float('inf')
minR = float('inf')

maxB = float('-inf')
maxG = float('-inf')
maxR = float('-inf')

for row in image:
    for pixel in row:
        minR = min(pixel[0], minR)
        minG = min(pixel[1], minG)
        minB = min(pixel[2], minB)

        maxR = max(pixel[0], maxR)
        maxG = max(pixel[1], maxG)
        maxB = max(pixel[2], maxB)

print(f'lowerColor = np.array({[minR, minG, minB]})')
print(f'upperColor = np.array({[maxR, maxG, maxB]})')
