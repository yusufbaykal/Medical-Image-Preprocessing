import cv2
import matplotlib.pyplot as plt
import pydicom
import numpy as np

class ImagePreprocessing:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path, 0)

    def clahe(self):
        ımg = self.image
        ımgs = list(cv2.split(ımg))
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        ımgs[0] = clahe.apply(ımgs[0])
        ımg= cv2.merge(ımgs)
        plt.imshow(ımg, cmap="gray")
        plt.show()
        return ımg

    def negative(self):
        image = self.image
        L = np.max(image)
        negatif_foto = L - image
        plt.imshow(image, cmap="gray")
        plt.show()
        return negatif_foto

    def unsharp_mask(self):
        image = self.image
        gassıan = cv2.GaussianBlur(image, (5, 5), 0)
        keskın = cv2.addWeighted(image, 1.5, gassıan, -0.5, 0)
        plt.imshow(keskın, cmap="gray")
        plt.show()
        return image

    def equalizeHist(self): # Matematiksel Histogram Eşitleme
        image = self.image
        hist, bins = np.histogram(image.flatten(), 256, [0, 256])
        kumulatıf = hist.cumsum()
        kumulatıf_norm = kumulatıf * float(hist.max()) / kumulatıf.max()
        new_image = np.interp(image.flatten(), bins[:-1], kumulatıf_norm)
        equalized = new_image.reshape(image.shape).astype(np.uint8)
        plt.imshow(equalized, cmap="gray")
        plt.show()
        return equalized
    
    def histogram_equalization(self): # Hazır Hisrogram Eşitleme
         img = cv2.imread(self.image, 0)
         equalized = cv2.equalizeHist(img)
         plt.imshow(equalized, cmap="gray")
         plt.show()
         return equalized

    def read_dicom(self, dicom_path):
        ds = pydicom.dcmread(dicom_path)
        image = ds.pixel_array
        plt.imshow(image, cmap="gray")
        plt.show()
        return image

    def save_dicom(self, image, dicom_path):
        ds = pydicom.dcmread(dicom_path)
        ds.PixelData = image.tobytes()
        ds.save_as(dicom_path)
        print("DICOM dosyası kayıt edildi!")

    def read_jpeg(self, jpeg_path):
        image = cv2.imread(jpeg_path, 0)
        plt.imshow(image, cmap="gray")
        plt.show()
        return image

    def save_jpeg(self, image, jpeg_path):
        cv2.imwrite(jpeg_path, image)
        print("JPEG dosyası kayıt edildi!")

     


image_prep = ImagePreprocessing("yeni.jpg")
image = image_prep.read_jpeg("yeni.jpg")
image = image_prep.negative()
#image_prep.save_dicom(image, "clahe_sample.dcm")

