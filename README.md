# YZR502 Otonom Robot Navigasyon ve Planlama

Bu repo, TurtleBot3 Burger robotu kullanılarak gerçekleştirilen haritalama, otonom navigasyon ve yol planlama algoritmalarının karşılaştırmalı analizini içerir.

## 📂 Proje Yapısı
* **/offline_planning**: A* ve RRT algoritmalarının Python implementasyonları ve karşılaştırma kodları.
* **/ros_navigation**: ROS navigasyon yığını için gerekli `launch` ve `yaml` (costmap, move_base) dosyaları.
* **/trajectory_smoothing**: Yol noktalarını Cubic Spline ile pürüzsüzleştiren ve jerk analizi yapan kodlar.
* **/results**: Deneylerden elde edilen istatistiksel tablolar, performans grafikleri ve simülasyon görüntüleri.

## 🛠 Kurulum ve Çalıştırma

### Bağımlılıklar
Aşağıdaki paketlerin sisteminizde kurulu olduğundan emin olun:
```bash
sudo apt-get install ros-noetic-turtlebot3-simulations ros-noetic-navigation
pip3 install numpy scipy matplotlib pandas
