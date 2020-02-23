import cv2
import glob

all_images = glob.glob('*.jpg')
print(all_images)

images = ["galaxy.jpg", "kangaroos.jpg", "Lighthouse.jpg", "scenarie.jpg"]
for image in images:
    python_image = cv2.imread(image, 0)
    resized_height = int(python_image.shape[0]/2)
    resized_width = int(python_image.shape[1]/2)
    resized_python_image = cv2.resize(python_image,(resized_width, resized_height))
    name = "new" + image
    cv2.imwrite(name, resized_python_image)

print("done")