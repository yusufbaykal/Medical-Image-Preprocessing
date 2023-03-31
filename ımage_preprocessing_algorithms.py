import cv2
import matplotlib.pyplot as plt
import pydicom
import numpy as np
import os 
import glob

class ImagePreprocessing:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path, 0)

    def Dicom_to_Jpeg(Path):
        try:
            dicom_image = pydicom.read_file(Path)
            row = dicom_image.get(0x00280010).value  
            column = dicom_image.get(0x00280011).value  
            orn_number = int(dicom_image.get(0x00200013).value)  
            pnc_mrkz = int(dicom_image.get(0x00281050).value)  
            pnc_genıs = int(dicom_image.get(0x00281051).value)  
            pnc_max = int(pnc_mrkz + pnc_genıs / 2)
            pnc_min = int(pnc_mrkz - pnc_genıs / 2)
            if (dicom_image.get(0x00281052) is None):
                olck_snr = 0
            else:
                olck_snr = int(dicom_image.get(0x00281052).value)

            if (dicom_image.get(0x00281053) is None):
                olck_egm = 1
            else:
                olck_egm = int(dicom_image.get(0x00281053).value)

            yenı_image = np.zeros((row, column), np.uint8)
            pixels = dicom_image.pixel_array

            for i in range(0, row):
                for j in range(0, column):
                    orj_pix = pixels[i][j]
                    new_orj_pix = orj_pix * olck_egm + olck_snr

                    if (new_orj_pix > pnc_max): 
                        yenı_image[i][j] = 255
                    elif (new_orj_pix < pnc_min):  
                        yenı_image[i][j] = 0
                    else:
                        yenı_image[i][j] = int(((new_orj_pix - pnc_min) / (pnc_max - pnc_min)) * 255)  

            return yenı_image, 0
        except:
            return 0, 1

    names = os.listdir("path/to/image/dicom/")[:1000]

    if len(glob.glob("İmage_JPEG")) == 0:
        os.mkdir("İmage_JPEG")

    for name in names:
        if len(glob.glob(f"İmage_JPEG/{name}")) == 0:
            os.mkdir(f"İmage_JPEG/{name}")
        c = 1
        for path in glob.glob(f"path/to/image/dicom/{name}/**.dcm"):
            if len(glob.glob(f"İmage_JPEG/{name}/**.jpg")) >= c:
                c += 1
                continue
            c += 1
            id = path.split("/")[-1].split(".")[0]
            img = Dicom_to_Jpeg(path)
            img = cv2.resize(img[0],(512,512))
            cv2.imwrite("İmage_JPEG/"+str(name)+"/"+ f"{id}"+ '.jpg', img)


    def dicom_to_npy(input_dir, output_file):
        img_list = []
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".dcm"):
                    dcm_path = os.path.join(root, file)
                    ds = pydicom.dcmread(dcm_path)
                    img = ds.pixel_array
                    img_list.append(img)

        if len(img_list) == 0:
            print(f"Dicom Dosyası Bulunamadı!: {input_dir}")
            return 1

        img_array = np.array(img_list)
        np.save(output_file, img_array)
        return 0



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




 
