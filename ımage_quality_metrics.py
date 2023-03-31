import pydicom
from skimage import io
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity
from PIL import __version__ as pil_version
from PIL import Image
import cv2 as cv
import numpy as np
import math


class TestImage:
    def __init__(self, dicom_path, jpg_path):
        self.dicom_path = dicom_path
        self.image = pydicom.dcmread(dicom_path)
        self.dicom_image = self.image.pixel_array
        self.jpg_path = jpg_path
        self.image1 = io.imread(jpg_path)

    def snr_test(self):
        roi = self.dicom_image[100:200, 100:200]
        std = np.std(roi)
        snr = 20 * np.log10(np.mean(roi) / std)
        print('SNR of DICOM image: {snr:.2f}dB'.format(snr=snr))
        return snr

    def ssm_test(self):
        dcm_img = pydicom.dcmread(self.dicom_path)
        jpeg_img = io.imread(self.jpg_path, as_gray=True)
        ssim_value = structural_similarity(dcm_img.pixel_array, jpeg_img)
        print("SSIM değeri:", ssim_value)
        return ssim_value

    def calculate_psnr(self):
        dicom_img = self.image.pixel_array.astype(float)
        gray_img = dicom_img.astype(np.uint8)

        rgb_img = np.zeros((gray_img.shape[0], gray_img.shape[1], 3), dtype=np.uint8)
        rgb_img[:, :, 0] = gray_img
        rgb_img[:, :, 1] = gray_img
        rgb_img[:, :, 2] = gray_img

        jpg_img = self.image1.astype(float)

        if rgb_img.shape != jpg_img.shape:
            jpg_img = np.array(Image.fromarray(jpg_img.astype(np.uint8)).resize((rgb_img.shape[1], rgb_img.shape[0]))).astype(float)

        psnr_dicom = self.calculate_psnr_helper(rgb_img, jpg_img)
        psnr_jpg = self.calculate_psnr_helper(jpg_img, rgb_img)
        print('PSNR Değeri (DICOM): {psnr:.2f}dB'.format(psnr=psnr_dicom))
        print('PSNR Değeri (JPEG): {psnr:.2f}dB'.format(psnr=psnr_jpg))

        return psnr_dicom, psnr_jpg

    def calculate_psnr_helper(self, img1, img2):
        mse = np.mean((img1 - img2) ** 2)
        psnr = 20 * math.log10(255.0 / math.sqrt(mse))
        return psnr


test = TestImage("736471439.dcm","yeni.jpg")
test.snr_test()
#test.ssm_test()
#test.calculate_psnr()
