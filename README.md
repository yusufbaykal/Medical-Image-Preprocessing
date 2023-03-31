
# Medical Image Preprocessing

Proje içerisinde , medikal görüntü işleme için kullanılan bazı temel araçları ve algoritmaları içermektedir. Özellikle, DICOM formatında bir görüntü ve aynı görüntünün JPEG formatına dönüştürülmüş halinin karşılaştırması için bir SNR testi, SSIM testi ve PSNR testi uygulaması gerçekleştirilmiştir.

## ImagePreprocessing
```python
read_dicom(): DICOM formatındaki bir görüntüyü okur.
read_jpeg(): JPEG formatındaki bir görüntüyü okur.
clahe(): Girdi görüntüsüne Kontrast Sınırlı Adaptif Histogram Eşitleme (CLAHE) uygular.
negative(): Girdi görüntüsündeki renkleri tersine çevirir.
unsharp_mask(): Girdi görüntüsüne Unsharp Mask filtresi uygular.
equalizeHist(): Girdi görüntüsüne Histogram Eşitleme uygular.
histogram_equalization(): Girdi görüntüsüne Histogram Eşitleme uygular.
dicom_to_jpeg(): Verilen dosya yolundaki Dicom formatındaki görüntüleri JPEG formatına dönüştürür.
dicom_to_npy() : Verilen dosya yolundaki Dicom formatındaki görüntüleri npy. formatına dönüştürür.
```

## TestImage
```python
snr_test(dicom_path, jpg_path)
```
Bu fonksiyon, bir DICOM formatında ve bir de JPEG formatında verilen iki farklı görüntü arasındaki Sinyal-Gürültü Oranını (SNR) hesaplar. 

```python
calculate_psnr(dicom_path, jpg_path)
```
Bu fonksiyon, bir DICOM formatında ve bir de JPEG formatında verilen iki farklı görüntü arasındaki Peak Sinyal-Gürültü Oranını (PSNR) hesaplar.

```python
ssim_test(dicom_path, jpg_path) 
```
Bu fonksiyon, bir DICOM formatında ve bir de JPEG formatında verilen iki farklı görüntü arasındaki Yapısal Benzerlik Endeksini (SSIM) hesaplar. 




## Kurulum
Projeyi klonlayın

```bash
  git clone https://github.com/yusufbaykal/Medical-Image-Preprocessing.git
```

Proje dizinine gidin

```bash
  cd Medical-Image-Preprocessing
```

Gerekli paketleri yükleyin

Python 3.x yüklü olduğundan emin olun.


```bash
  pip install -r requirements.txt

```

  
## Kullanım


```python
from ImagePreprocessing import ImagePreprocessing
image_prep = ImagePreprocessing("path/to/image")
```
```python
from TestImage import TestImage
test = TestImage(dicom_path,jpg_path)
```
## İmage Preprocessing

#### Dicom to JPEG
```python
dicom_path = "my_dicom_file.dcm"
jpeg_path = "my_jpeg_file.jpg"
image_prep.dicom_to_jpeg(dicom_path, jpeg_path)
```
#### Dicom to Matrix
```python
dicom_path = "path/to/dicom/file.dcm"
npy_path = "path/to/save/npy/file.npy"
image = image_prep.dicom_to_npy(dicom_path, npy_path)
```
#### Dicom Data Type
```python
image = image_prep.read_dicom("path/to/dicom")
```
#### JPEG Data Type
```python
image = image_prep.read_jpeg("path/to/jpeg")
```
#### Applying CLAHE
Görüntü üzerinde CLAHE algoritması işlemi uygulamak için "clahe" fonksiyonunu çağırabilirsiniz.
```python
image = image_prep.clahe()
```
#### Negative

Görüntünün Negatifini alma işlemi uygulamak için "negative" fonksiyonunu çağırabilirsiniz.

```python
image = image_prep.negative()
```

#### Unsharp Mask

Görüntü üzerinde Unsharp Mask algoritmasını uygulamak için "unsharp_mask" fonksiyonunu çağırabilirsiniz.

```python
image = image_prep.unsharp_mask()
```

#### Histogram Equalization

Görüntü üzerinde Histogram Eşitleme algoritmasını uygulamak için "equalizeHist" veya "histogram_equalization" fonksiyonunu çağırabilirsiniz.
```python
equalizeHist() 
```
Hazır fonksiyon kullanılmadan yazılmıştır.

```python
histogram_equalization() 
```
 Opencv kütüphanesi içerisinden hazır fonksiyon alınmıştır.

```python
image = image_prep.equalizeHist()
```
```python
image = image_prep.histogram_equalization()
```

## Test Image

#### Signal to Noise Ratio
İki görüntü arasındaki Sinyal-Gürültü Oranını (SNR) hesaplar, biri DICOM formatında diğeri ise JPEG formatındadır.
```python
test = TestImage(dicom_path,jpg_path)
test.snr_test()
```
#### Peak Signal to Noise Ratio
İki görüntü arasında (bir tanesi DICOM formatında, diğeri JPEG formatında) Piksel Sinyal Gürültü Oranını (PSNR) hesaplar.
```python
test = TestImage(dicom_path,jpg_path)
test.calculate_psnr()
```
#### Structural Similarity Index
İki görüntü arasındaki Yapısal Benzerlik İndeksini (SSIM), biri DICOM formatında diğeri JPEG formatında olan iki görüntü arasında hesaplar.
```python
test = TestImage(dicom_path,jpg_path)
test.ssm_test()
```

## Lisans

[MIT](https://choosealicense.com/licenses/mit/)

  
