import os
import cv2
from cv2 import dnn_superres


class UpscaleImage():
    def __init__(self, file, directory):
        self.file = file
        self.directory = directory

        print(self.file)
        print(self.directory)

    def run(self):
        # Create an SR object
        sr = dnn_superres.DnnSuperResImpl_create()

        # Read image
        image = cv2.imread(self.file)

        # Read the desired model
        path = "models/EDSR_x3.pb"
        sr.readModel(path)

        sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        # Set the desired model and scale to get correct pre- and post-processing
        sr.setModel("edsr", 3)

        # Upscale the image
        result = sr.upsample(image)

        # Get the name of file
        basename = os.path.basename(self.file)
        file_name = os.path.splitext(basename)[0]

        # Save the image
        cv2.imwrite(f"{self.directory}/{file_name}_upscaled.png", result)
