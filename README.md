# YZR502 Otonom Robot Navigasyon Projesi

Bu proje, bir mobil robotun (TurtleBot3 Burger) bilinmeyen bir ortamda harita çıkarması, yol planlaması ve pürüzsüz yörünge takibi yapmasını kapsar.

## 🛠 Kullanılan Teknolojiler
* **ROS Noetic** & **Gazebo** (Simülasyon)
* **Python** (Algoritma Geliştirme)
* **OpenCV** (Harita İşleme)
* **SciPy** (İstatistiksel Analiz)

## 📈 Karşılaştırmalı Analiz
A* ve RRT algoritmaları çalışma süreleri açısından karşılaştırılmıştır. Yapılan t-testi sonucunda A* algoritmasının planlama süresi açısından daha verimli olduğu kanıtlanmıştır.

## 🔄 Yörünge Pürüzsüzleştirme
Cubic Spline interpolasyonu kullanılarak robotun sarsıntı (jerk) değerleri optimize edilmiştir.
