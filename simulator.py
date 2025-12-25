#pygame模組的寫法
# import pygame # type: ignore
# import math
# import random

# # ===== 輔助函式：計算射線與方形房間的交點距離 =====
# def calculate_square_distance(robot_x, robot_y, angle_rad, room_min=50, room_max=550):
#     dx = math.cos(angle_rad)
#     dy = math.sin(angle_rad)
#     distances = []

#     # 左牆 x = room_min
#     if dx < -1e-6:
#         t = (room_min - robot_x) / dx
#         y = robot_y + t * dy
#         if room_min <= y <= room_max:
#             distances.append(t)

#     # 右牆 x = room_max
#     if dx > 1e-6:
#         t = (room_max - robot_x) / dx
#         y = robot_y + t * dy
#         if room_min <= y <= room_max:
#             distances.append(t)

#     # 上牆 y = room_min
#     if dy < -1e-6:
#         t = (room_min - robot_y) / dy
#         x = robot_x + t * dx
#         if room_min <= x <= room_max:
#             distances.append(t)

#     # 下牆 y = room_max
#     if dy > 1e-6:
#         t = (room_max - robot_y) / dy
#         x = robot_x + t * dx
#         if room_min <= x <= room_max:
#             distances.append(t)

#     if distances:
#         return min(d for d in distances if d > 0)
#     else:
#         return 1000

# # ===== LiDAR 模擬主函式 =====
# def simulate_lidar_scan(robot_x, robot_y, mode="square"):
#     scan = []
#     for angle_deg in range(0, 360, 5):
#         angle_rad = math.radians(angle_deg)
        
#         if mode == "circle":
#             base_dist = 1000
#         elif mode == "peanut":
#             base_dist = 800 + 300 * math.sin(angle_rad * 2)
#         elif mode == "square":
#             base_dist = calculate_square_distance(robot_x, robot_y, angle_rad)
#         else:
#             base_dist = 1000

#         noisy_dist = base_dist * (1 + random.uniform(-0.02, 0.02))
#         scan.append((angle_deg, max(100, int(noisy_dist))))
#     return scan

# # ===== PyGame 主程式 =====
# pygame.init()
# screen = pygame.display.set_mode((600, 600))
# pygame.display.set_caption("Virtual LiDAR Simulator")
# clock = pygame.time.Clock()

# robot_x, robot_y = 300, 300
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     # 在 while running: 內，event 迴圈之後
#     keys = pygame.key.get_pressed()
#     move_speed = 5  # 每次移動 5 像素

#     if keys[pygame.K_UP]:
#         robot_y -= move_speed
#     if keys[pygame.K_DOWN]:
#         robot_y += move_speed
#     if keys[pygame.K_LEFT]:
#         robot_x -= move_speed
#     if keys[pygame.K_RIGHT]:
#         robot_x += move_speed

# # 防止機器人跑出房間（可選）
#     robot_x = max(60, min(540, robot_x))
#     robot_y = max(60, min(540, robot_y))

#     # ✅ 關鍵呼叫：帶 mode 參數
#     scan = simulate_lidar_scan(robot_x, robot_y, mode="square")

#     screen.fill((0, 0, 0))

#     # 畫牆壁
#     walls = [(50,50,550,50), (550,50,550,550), (550,550,50,550), (50,550,50,50)]
#     for (x1,y1,x2,y2) in walls:
#         pygame.draw.line(screen, (255,255,255), (x1,y1), (x2,y2), 2)

#     # 畫 LiDAR 點雲
#     for angle, dist in scan:
#         rad = math.radians(angle)
#         scale = 0.1
#         x = robot_x + dist * math.cos(rad) * scale
#         y = robot_y + dist * math.sin(rad) * scale
#         pygame.draw.circle(screen, (0,255,0), (int(x), int(y)), 2)

#     # 畫機器人
#     pygame.draw.circle(screen, (255,0,0), (robot_x, robot_y), 8)

#     pygame.display.flip()
#     clock.tick(10)

# pygame.quit()
#tkinter寫法
import tkinter as tk
import math
class LidarSimulator:
    def __init__(self,width=600,height=600):
        #建立主視窗（root window），這是所有 GUI 元素的容器
        self.root=tk,Tk()
        self.root.title("雷達模擬器")
        #建立一個畫布（Canvas），用來繪圖；指定寬度、高度、背景色為黑色
        self.canvas=tk.Canvas(self.root,width=width,height=height,bg='black')
        
