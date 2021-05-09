import cv2
import numpy as np
from sklearn.cluster import MiniBatchKMeans

CLUSTERS = 4
SIZE = 256
FILENAME = 'Images/Cave.jpg'

#PIXELATION STEP
#----------------

# Input image
inim = cv2.imread('Images/Cave.jpg')

cv2.imshow('test', inim)
cv2.waitKey(0)

# Get input size
height, width = inim.shape[:2]

# Desired "pixelated" size
w, h = (SIZE, SIZE)

# Resize input to "pixelated" size
temp = cv2.resize(inim, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_LINEAR)

output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

#QUANTIZE COLORS STEP
#--------------------

# get pixelated image size
(h, w) = output.shape[:2]

# change color space from BGR to ? used in magic algorithm
output = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)
output = output.reshape((output.shape[0] * output.shape[1], 3))

# perform pixel grouping algorithm
clt = MiniBatchKMeans(n_clusters=CLUSTERS)
labels = clt.fit_predict(output)
quant = clt.cluster_centers_.astype("uint8")[labels]

# reshape back to original and get back to BGR color
quant = quant.reshape((h, w, 3))
quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)

# resize quant and original image to 512px X 512px
inim = cv2.resize(inim, (512, 512))
quant = cv2.resize(quant, (512, 512))

# Display images
cv2.imshow("Input", inim)
cv2.imshow("Quantized", quant)
cv2.waitKey(0)

