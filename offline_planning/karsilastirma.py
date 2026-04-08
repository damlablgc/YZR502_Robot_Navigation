import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import heapq
import random
import csv

# Harita yükleme ve ön işleme
def load_map(file_path):
    grid = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    binary_grid = np.where(grid >= 250, 0, 1)
    kernel = np.ones((5,5), np.uint8) 
    return cv2.dilate(binary_grid.astype(np.uint8), kernel, iterations=1)

def heuristic(a, b): return math.dist(a, b)

def astar(grid, start, goal):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    came_from, gscore = {}, {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = [(fscore[start], start)]
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current); current = came_from[current]
            path.append(start); return path[::-1]
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            if not (0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1] and grid[neighbor[0]][neighbor[1]] == 0): continue
            tentative_g = gscore[current] + heuristic(current, neighbor)
            if tentative_g < gscore.get(neighbor, float('inf')):
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g
                fscore[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
    return None

def rrt(grid, start, goal, max_iter=10000, step_size=7):
    class Node:
        def __init__(self, x, y): self.x, self.y, self.parent = x, y, None
    nodes = [Node(start[0], start[1])]
    for _ in range(max_iter):
        rx, ry = (goal[0], goal[1]) if random.random() < 0.1 else (random.randint(0, grid.shape[0]-1), random.randint(0, grid.shape[1]-1))
        nearest = min(nodes, key=lambda n: math.dist((n.x, n.y), (rx, ry)))
        theta = math.atan2(ry - nearest.y, rx - nearest.x)
        new_x, new_y = int(nearest.x + step_size * math.cos(theta)), int(nearest.y + step_size * math.sin(theta))
        if 0 <= new_x < grid.shape[0] and 0 <= new_y < grid.shape[1] and grid[new_x][new_y] == 0:
            new_node = Node(new_x, new_y); new_node.parent = nearest; nodes.append(new_node)
            if math.dist((new_node.x, new_node.y), goal) <= step_size:
                path = [goal]; curr = new_node
                while curr: path.append((curr.x, curr.y)); curr = curr.parent
                return path[::-1]
    return None

# Deney ve sonuç kaydetme
if __name__ == '__main__':
    grid = load_map('my_map.pgm')
    start, goal = (190, 190), (250, 250) # Önceki başarılı noktaların
    veriler = []

    print(f"{'Tur':<5} | {'Algoritma':<10} | {'Süre (sn)':<10} | {'Uzunluk (px)':<12}")
    print("-" * 45)

    for i in range(1, 11):
        # A* Deneyi
        t0 = time.time()
        p_astar = astar(grid, start, goal)
        d_astar = time.time() - t0
        l_astar = sum(math.dist(p_astar[j], p_astar[j+1]) for j in range(len(p_astar)-1)) if p_astar else 0
        veriler.append([i, 'A*', d_astar, l_astar])
        print(f"{i:<5} | {'A*':<10} | {d_astar:<10.4f} | {l_astar:<12.2f}")

        # RRT Deneyi
        t0 = time.time()
        p_rrt = rrt(grid, start, goal)
        d_rrt = time.time() - t0
        l_rrt = sum(math.dist(p_rrt[j], p_rrt[j+1]) for j in range(len(p_rrt)-1)) if p_rrt else 0
        veriler.append([i, 'RRT', d_rrt, l_rrt])
        print(f"{i:<5} | {'RRT':<10} | {d_rrt:<10.4f} | {l_rrt:<12.2f}")

    # Sonuçları CSV olarak kaydet
    with open('deney_sonuclari.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Tur', 'Algoritma', 'Sure_Saniye', 'Yol_Uzunlugu_Piksel'])
        writer.writerows(veriler)
    
    print("\n[BİLGİ] 10 deney tamamlandı ve 'deney_sonuclari.csv' dosyasına kaydedildi.")
    # A* yolunu kaydet:
    if path_astar:
        print("\n--- MAKALE İÇİN KOORDİNATLAR ---")
        print("X_GERCEK =", [p[0] for p in path_astar[::10]]) # Her 10 noktada bir al (Grafik daha güzel görünür)
        print("Y_GERCEK =", [p[1] for p in path_astar[::10]])