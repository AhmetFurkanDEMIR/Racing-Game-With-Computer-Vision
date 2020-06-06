# Racing Game With Computer Vision

* El hareketleriyle oynayabileceğiniz yarış oyunu.
* Modelimizi taş, kağıt, makas veri seti ile eğittik.
* Nesne tespitini Keras RetinaNet(Omurga olarak ResNet50 kullanıldı) ile yaptık.

# Oyun Hakkında (Backend Detay)

* Oyun sadece Nvidia GPU donanımı üzerinden oynanabilmektedir.

* Oyunu oynayabilmeniz için Nvidia GPU Driver, CUDA V10.1 ve cuDNN V7.6.5 yazılımlarını yüklemeniz gerekli
                                       
      Nvidia GPU Driver : https://www.nvidia.com.tr/drivers
      CUDA V10.1 : https://developer.nvidia.com/cuda-downloads
      cuDNN V7.6.5 : https://developer.nvidia.com/cudnn
              
* Keras ara uç motorda Tensorflow 'u kullanmaktadır.Bunun için Tensorflow-gpu 'yu yüklemeniz gereklidir.
       
      Tensorflow-gpu : https://www.tensorflow.org/install/gpu
      
* Oyunu AMD GPU donanımı üzerinden oynamak için arka uç olarak başka bir kütüphane kullanmanız gereklidir. 
      
* Oyunu oynayabileceğiniz GPU 'lar:

1-) Nvidia GTX 1000 serisinin tamamı
2-) Nvidia RTX serisinin tamamı
3-) .....
      


