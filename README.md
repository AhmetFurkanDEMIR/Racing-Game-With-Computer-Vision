![licence](https://img.shields.io/badge/Keras-V2.3.1-red)
![licencee](https://img.shields.io/badge/Tensorflow-V2.0-yellow)
![licence](https://img.shields.io/badge/demir-ai-blueviolet)

# Racing Game With Computer Vision

![Screenshot_2020-06-06_15-00-34](https://user-images.githubusercontent.com/54184905/83944510-a46e7e00-a80c-11ea-9c94-ec83573498d9.png)

* El hareketleriyle oynayabileceğiniz yarış oyunu.
* Modelimizi taş, kağıt, makas veri seti ile eğittik.
* Nesne tespitini Keras RetinaNet(Omurga olarak ResNet50 kullanıldı) ile yaptık.


# Oynanış Mantığı

* Oyunu el hareketleriniz ile yönlendirmektesiniz.
* Nesnelere çarpmadan oynamanız gerekli, herhangi bir nesneye çarparsanız oyunu kaybedersiniz.

![Screenshot_2020-06-06_14-14-54](https://user-images.githubusercontent.com/54184905/83944435-27db9f80-a80c-11ea-9445-deb945412e29.png)


# Oyun Hakkında - Backend Detay

* Modeli NVIDIA Tesla P100 GPU (Google Colab Pro) üzerinden eğittik.

* Oyun sadece Nvidia GPU donanımı üzerinden oynanabilmektedir.

* Keras ara uç motorda Tensorflow 'u kullanmaktadır. Bunun için Tensorflow-gpu 'yu yüklemeniz gereklidir.
       
      Tensorflow-gpu : https://www.tensorflow.org/install/gpu

* Oyunu oynayabilmeniz için Nvidia GPU Driver, CUDA V10.1 ve cuDNN V7.6.5 yazılımlarını yüklemeniz gerekli
                                       
      Nvidia GPU Driver : https://www.nvidia.com.tr/drivers
      CUDA V10.1 : https://developer.nvidia.com/cuda-downloads
      cuDNN V7.6.5 : https://developer.nvidia.com/cudnn
      
* Oyunu AMD GPU donanımı üzerinden oynamak için arka uç olarak başka bir kütüphane kullanmanız gereklidir. 

* Ilerki zamanlarda Modelin omurgasını MobileNet olarak değiştirip tüm donanımlar üzerinden oynanabilmesini hedeflemekteyiz.


# Keras RetinaNet ile modelimizi eğitirken omurga olarak ResNet50 kullandık

* Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers---8x deeper than VGG nets but still having lower complexity.

An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers.

The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.

![gI4zT](https://user-images.githubusercontent.com/54184905/83944404-e814b800-a80b-11ea-9cad-a8607463d35f.png)

# Oyun içi görüntüler

* Arabanın ilerlemesini sağlamak :

![Screenshot_2020-06-06_14-07-07](https://user-images.githubusercontent.com/54184905/83944433-26aa7280-a80c-11ea-9472-bf6f3e085315.png)

* Arabanın sağa dönmesini sağlamak :

![Screenshot_2020-06-06_14-19-42](https://user-images.githubusercontent.com/54184905/83944469-725d1c00-a80c-11ea-938b-b0924ee9a8e7.png)

* Arabanın sola dönmesini sağlamak :

![Screenshot_2020-06-06_14-12-25](https://user-images.githubusercontent.com/54184905/83944505-a2a4ba80-a80c-11ea-8233-a171db0bb86e.png)

![Screenshot_2020-06-06_14-13-27](https://user-images.githubusercontent.com/54184905/83944508-a3d5e780-a80c-11ea-9d48-803ac8870ee5.png)

# Projeyi inşaa edenler

Ahmet Furkan DEMIR - https://www.linkedin.com/in/1dfurkan/

Omar Mohamed - https://www.linkedin.com/in/omar-mohamed-15b750194/

Bahadır Poroy - https://www.linkedin.com/in/bahad%C4%B1r-poroy-bb1b2912b/

Emre Aydın - https://www.linkedin.com/in/emreayddin/
