import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
def generate_path():
    # Robotun bulduğu ham (köşeli) yol noktaları (Örnek veriler)
    # Sen istersen burayı kendi A* sonucunla güncelleyebilirsin
    x = np.array([0, 2, 4, 5, 8])
    y = np.array([0, 1, 4, 3, 6])
    return x, y

def smooth_trajectory(x, y):
    # Yolun pürüzsüzleştirilmesi (Cubic Spline)
    t = np.arange(len(x))
    cs_x = CubicSpline(t, x)
    cs_y = CubicSpline(t, y)
    
    t_new = np.linspace(0, len(x)-1, 100)
    x_smooth = cs_x(t_new)
    y_smooth = cs_y(t_new)
    
    # Jerk (Sarsıntı) Hesaplama: Hızın 3. türevidir
    # Basitleştirilmiş model: İvme değişim hızı
    dt = 0.1
    vx = np.diff(x_smooth) / dt
    vy = np.diff(y_smooth) / dt
    ax = np.diff(vx) / dt
    ay = np.diff(vy) / dt
    jx = np.diff(ax) / dt
    jy = np.diff(ay) / dt
    
    total_jerk = np.mean(np.sqrt(jx**2 + jy**2))
    return x_smooth, y_smooth, total_jerk

if __name__ == '__main__':
    x, y = generate_path()
    xs, ys, jerk = smooth_trajectory(x, y)
    
    print(f"=== YÖRÜNGE ANALİZİ ===")
    print(f"Hesaplanan Ortalama Jerk (Sarsıntı) Değeri: {jerk:.4f} m/s^3")
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'ro--', label='Ham Yol (A*)')
    plt.plot(xs, ys, 'b-', label='Pürüzsüz Yol (Cubic Spline)')
    plt.title(f"Yörünge Pürüzsüzleştirme (Jerk: {jerk:.2f})")
    plt.legend()
    plt.grid(True)
    plt.savefig('trajectory_smoothing.png')
    plt.show()