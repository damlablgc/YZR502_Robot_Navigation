# YZR502 Otonom Robot Navigasyon ve Karşılaştırmalı Analiz Projesi

Bu proje, TurtleBot3 Burger robotu kullanılarak ROS Noetic ve Gazebo simülasyon ortamında gerçekleştirilen haritalama, otonom navigasyon ve yol planlama algoritmalarının istatistiksel analizini kapsamaktadır.

## 📂 Proje Hiyerarşisi
Proje dosyaları, akademik ve teknik standartlara uygun olarak aşağıdaki şekilde organize edilmiştir:

* **/offline_planning**: A* ve RRT algoritmalarının Python implementasyonları, karşılaştırma testleri (`karsilastirma.py`) ve T-testi analizlerini (`istatistik_analiz.py`) içerir.
* **/ros_navigation**: Robotun Gazebo ortamındaki haritalama verilerini (`.pgm`, `.yaml`) ve navigasyon konfigürasyonlarını içerir.
* **/trajectory_smoothing**: Ham yol noktalarının Cubic Spline yöntemiyle iyileştirilmesi ve Jerk (sarsıntı) analizi yapan kodları (`smooth_path.py`) içerir.
* **/results**: Deneylerden elde edilen veri tabloları (`.csv`) ve görselleştirilmiş grafik çıktılarını (`.png`) içerir.

## 🛠 Kurulum ve Çalıştırma

### Bağımlılıklar
Projenin çalışması için gerekli kütüphaneler:
```bash
sudo apt-get install ros-noetic-turtlebot3-simulations ros-noetic-navigation
pip3 install numpy scipy matplotlib pandas opencv-python
