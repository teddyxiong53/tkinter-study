#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
08_canvas_drawing.py - Tkinter Canvas画布演示

演示内容：
- 绘制基本图形 (线/圆/矩形/多边形)
- 动态动画的实现 (move()/after())
- 图像加载与处理 (PhotoImage类)
- 对象标签与事件绑定 (tags系统)
"""

import tkinter as tk
from tkinter import ttk
import math
import random

# 创建主窗口
root = tk.Tk()
root.title("图形绘制工坊 - Canvas魔法")
root.geometry("800x600+100+100")
root.configure(bg="#f0f0f0")

# 创建一个Notebook(选项卡控件)来展示不同的Canvas功能
nb = ttk.Notebook(root)
nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ===== 1. 基本图形绘制 =====
basic_frame = ttk.Frame(nb, padding=10)
nb.add(basic_frame, text="基本图形")

# 创建说明标签
basic_info = tk.Label(
    basic_frame,
    text="Canvas可以绘制各种基本图形，如线条、矩形、椭圆和多边形等",
    justify=tk.LEFT,
    pady=10
)
basic_info.pack(anchor=tk.W)

# 创建Canvas
basic_canvas = tk.Canvas(
    basic_frame,
    width=700,
    height=400,
    bg="white",
    bd=2,
    relief=tk.SUNKEN
)
basic_canvas.pack(pady=10)

# 绘制直线
basic_canvas.create_line(50, 50, 200, 50, width=2, fill="red")
basic_canvas.create_text(125, 70, text="直线", fill="red")

# 绘制带箭头的线
basic_canvas.create_line(50, 100, 200, 100, width=2, arrow=tk.LAST, fill="blue")
basic_canvas.create_text(125, 120, text="带箭头的线", fill="blue")

# 绘制虚线
basic_canvas.create_line(50, 150, 200, 150, width=2, dash=(4, 2), fill="green")
basic_canvas.create_text(125, 170, text="虚线", fill="green")

# 绘制矩形
basic_canvas.create_rectangle(250, 50, 350, 100, outline="purple", width=2)
basic_canvas.create_text(300, 120, text="矩形", fill="purple")

# 绘制填充矩形
basic_canvas.create_rectangle(250, 150, 350, 200, outline="black", fill="#ffcc00", width=2)
basic_canvas.create_text(300, 220, text="填充矩形", fill="black")

# 绘制圆角矩形
basic_canvas.create_rectangle(250, 250, 350, 300, outline="#009688", fill="#e0f2f1", width=2, dash=(1, 1))
basic_canvas.create_text(300, 320, text="虚线矩形", fill="#009688")

# 绘制椭圆
basic_canvas.create_oval(400, 50, 500, 100, outline="#ff5722", width=2)
basic_canvas.create_text(450, 120, text="椭圆", fill="#ff5722")

# 绘制填充椭圆(圆)
basic_canvas.create_oval(425, 150, 475, 200, outline="black", fill="#2196f3", width=2)
basic_canvas.create_text(450, 220, text="填充圆", fill="black")

# 绘制弧
basic_canvas.create_arc(400, 250, 500, 350, start=0, extent=270, outline="#673ab7", width=2, style=tk.ARC)
basic_canvas.create_text(450, 370, text="弧", fill="#673ab7")

# 绘制扇形
basic_canvas.create_arc(550, 50, 650, 150, start=0, extent=90, outline="black", fill="#ffc107", width=2)
basic_canvas.create_text(600, 170, text="扇形", fill="black")

# 绘制多边形
basic_canvas.create_polygon(550, 200, 600, 250, 650, 200, 600, 300, outline="black", fill="#4caf50", width=2)
basic_canvas.create_text(600, 320, text="多边形", fill="black")

# ===== 2. 动态动画 =====
animation_frame = ttk.Frame(nb, padding=10)
nb.add(animation_frame, text="动态动画")

# 创建说明标签
animation_info = tk.Label(
    animation_frame,
    text="使用move()方法和after()函数可以创建简单的动画效果",
    justify=tk.LEFT,
    pady=10
)
animation_info.pack(anchor=tk.W)

# 创建Canvas
animation_canvas = tk.Canvas(
    animation_frame,
    width=700,
    height=400,
    bg="white",
    bd=2,
    relief=tk.SUNKEN
)
animation_canvas.pack(pady=10)

# 创建控制按钮框架
control_frame = tk.Frame(animation_frame)
control_frame.pack(pady=10)

# 创建一个小球
ball = animation_canvas.create_oval(10, 10, 40, 40, fill="red", outline="black", width=2)

# 小球的移动速度和方向
dx = 5
dy = 3

# 动画标志
animation_running = False

# 动画函数
def animate_ball():
    global dx, dy, animation_running
    if animation_running:
        # 获取小球当前位置
        x1, y1, x2, y2 = animation_canvas.coords(ball)
        
        # 检测边界碰撞
        if x1 <= 0 or x2 >= 700:
            dx = -dx
        if y1 <= 0 or y2 >= 400:
            dy = -dy
        
        # 移动小球
        animation_canvas.move(ball, dx, dy)
        
        # 设置下一帧
        root.after(30, animate_ball)

# 开始动画
def start_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        animate_ball()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

# 停止动画
def stop_animation():
    global animation_running
    animation_running = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# 重置小球位置
def reset_ball():
    global dx, dy, animation_running
    animation_running = False
    animation_canvas.coords(ball, 10, 10, 40, 40)
    dx = 5
    dy = 3
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# 创建多个小球
def create_multiple_balls():
    global animation_running
    animation_running = False
    animation_canvas.delete("all")
    
    # 创建10个随机位置、颜色的小球
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "brown"]
    
    for i in range(10):
        x = random.randint(20, 680)
        y = random.randint(20, 380)
        color = random.choice(colors)
        animation_canvas.create_oval(x, y, x+30, y+30, fill=color, outline="black", width=2, tags="ball")
    
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# 移动所有小球
def animate_all_balls():
    global animation_running
    if animation_running:
        # 获取所有小球
        balls = animation_canvas.find_withtag("ball")
        
        for ball_id in balls:
            # 随机移动
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            
            # 获取当前位置
            x1, y1, x2, y2 = animation_canvas.coords(ball_id)
            
            # 检测边界
            if x1 <= 0 or x2 >= 700:
                dx = -dx
            if y1 <= 0 or y2 >= 400:
                dy = -dy
            
            # 确保不会超出边界
            if x1 + dx < 0 or x2 + dx > 700:
                dx = -dx
            if y1 + dy < 0 or y2 + dy > 400:
                dy = -dy
            
            # 移动小球
            animation_canvas.move(ball_id, dx, dy)
        
        # 设置下一帧
        root.after(50, animate_all_balls)

# 开始所有小球的动画
def start_all_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        animate_all_balls()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

# 创建控制按钮
start_button = tk.Button(control_frame, text="开始", command=start_animation)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(control_frame, text="停止", command=stop_animation, state=tk.DISABLED)
stop_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(control_frame, text="重置", command=reset_ball)
reset_button.pack(side=tk.LEFT, padx=5)

multiple_button = tk.Button(control_frame, text="创建多个小球", command=create_multiple_balls)
multiple_button.pack(side=tk.LEFT, padx=5)

start_all_button = tk.Button(control_frame, text="开始所有小球", command=start_all_animation)
start_all_button.pack(side=tk.LEFT, padx=5)

# ===== 3. 图像处理 =====
image_frame = ttk.Frame(nb, padding=10)
nb.add(image_frame, text="图像处理")

# 创建说明标签
image_info = tk.Label(
    image_frame,
    text="Canvas可以显示和处理图像，使用PhotoImage类加载图像\n注意：PhotoImage只支持GIF、PGM、PPM和PNG格式",
    justify=tk.LEFT,
    pady=10
)
image_info.pack(anchor=tk.W)

# 创建Canvas
image_canvas = tk.Canvas(
    image_frame,
    width=700,
    height=400,
    bg="white",
    bd=2,
    relief=tk.SUNKEN
)
image_canvas.pack(pady=10)

# 创建一个简单的图像（由于没有实际图像文件，我们创建一个彩色方块图案）
image_canvas.create_rectangle(50, 50, 150, 150, fill="#ff9800", outline="black", width=2)
image_canvas.create_rectangle(150, 50, 250, 150, fill="#2196f3", outline="black", width=2)
image_canvas.create_rectangle(50, 150, 150, 250, fill="#4caf50", outline="black", width=2)
image_canvas.create_rectangle(150, 150, 250, 250, fill="#9c27b0", outline="black", width=2)

# 添加文本说明
image_canvas.create_text(150, 300, text="模拟图像显示\n(实际应用中可使用PhotoImage加载真实图像)", fill="black")

# 添加代码示例
code_text = """# 加载图像示例代码
from tkinter import PhotoImage

# 加载图像
image = PhotoImage(file='example.png')

# 在Canvas上显示图像
canvas.create_image(x, y, image=image, anchor=tk.NW)

# 注意：必须保持对PhotoImage对象的引用，否则图像不会显示
# 通常将其保存为类的属性或全局变量
self.image = image  # 在类中
# 或
global image  # 在函数中"""

code_label = tk.Label(
    image_frame,
    text=code_text,
    justify=tk.LEFT,
    font=("Courier", 10),
    bg="#f5f5f5",
    relief=tk.GROOVE,
    padx=10,
    pady=10
)
code_label.pack(pady=10, fill=tk.X)

# ===== 4. 对象标签与事件绑定 =====
tags_frame = ttk.Frame(nb, padding=10)
nb.add(tags_frame, text="标签与事件")

# 创建说明标签
tags_info = tk.Label(
    tags_frame,
    text="Canvas中的每个对象都可以有一个或多个标签(tags)\n可以通过标签来选择和操作一组对象，也可以为对象绑定事件",
    justify=tk.LEFT,
    pady=10
)
tags_info.pack(anchor=tk.W)

# 创建Canvas
tags_canvas = tk.Canvas(
    tags_frame,
    width=700,
    height=400,
    bg="white",
    bd=2,
    relief=tk.SUNKEN
)
tags_canvas.pack(pady=10)

# 创建控制按钮框架
tags_control_frame = tk.Frame(tags_frame)
tags_control_frame.pack(pady=10)

# 创建不同形状并添加标签
shapes = [
    # (形状函数, 参数, 标签)
    (tags_canvas.create_rectangle, (50, 50, 150, 100), "rectangle shape red"),
    (tags_canvas.create_oval, (200, 50, 300, 100), "oval shape green"),
    (tags_canvas.create_polygon, (350, 50, 400, 100, 450, 50), "polygon shape blue"),
    (tags_canvas.create_rectangle, (50, 150, 150, 200), "rectangle shape green"),
    (tags_canvas.create_oval, (200, 150, 300, 200), "oval shape blue"),
    (tags_canvas.create_polygon, (350, 150, 400, 200, 450, 150), "polygon shape red"),
    (tags_canvas.create_rectangle, (50, 250, 150, 300), "rectangle shape blue"),
    (tags_canvas.create_oval, (200, 250, 300, 300), "oval shape red"),
    (tags_canvas.create_polygon, (350, 250, 400, 300, 450, 250), "polygon shape green"),
]

# 创建形状并设置颜色
for create_func, coords, tags in shapes:
    shape_id = create_func(*coords, tags=tags)
    
    # 根据标签设置颜色
    if "red" in tags:
        tags_canvas.itemconfig(shape_id, fill="#f44336", outline="black", width=2)
    elif "green" in tags:
        tags_canvas.itemconfig(shape_id, fill="#4caf50", outline="black", width=2)
    elif "blue" in tags:
        tags_canvas.itemconfig(shape_id, fill="#2196f3", outline="black", width=2)

# 添加说明文本
tags_canvas.create_text(500, 175, text="点击形状查看其标签\n使用下方按钮筛选形状", fill="black")

# 显示标签的函数
def show_tags(event):
    # 获取点击位置的对象
    item_id = tags_canvas.find_closest(event.x, event.y)[0]
    
    # 获取对象的标签
    tags = tags_canvas.gettags(item_id)
    
    # 更新状态标签
    status_label.config(text=f"标签: {', '.join(tags)}")

# 筛选形状的函数
def filter_by_tag(tag):
    # 首先重置所有形状的状态
    for item_id in tags_canvas.find_all():
        tags_canvas.itemconfig(item_id, state=tk.NORMAL)
    
    # 如果选择了筛选标签
    if tag != "all":
        # 隐藏不匹配的形状
        for item_id in tags_canvas.find_all():
            if tag not in tags_canvas.gettags(item_id):
                tags_canvas.itemconfig(item_id, state=tk.HIDDEN)
    
    # 更新状态标签
    status_label.config(text=f"筛选: {tag}")

# 绑定点击事件
tags_canvas.bind("<Button-1>", show_tags)

# 创建筛选按钮
tk.Button(tags_control_frame, text="显示全部", command=lambda: filter_by_tag("all")).pack(side=tk.LEFT, padx=5)
tk.Button(tags_control_frame, text="矩形", command=lambda: filter_by_tag("rectangle")).pack(side=tk.LEFT, padx=5)
tk.Button(tags_control_frame, text="椭圆", command=lambda: filter_by_tag("oval")).pack(side=tk.LEFT, padx=5)
tk.Button(tags_control_frame, text="多边形", command=lambda: filter_by_tag("polygon")).pack(side=tk.LEFT, padx=5)
tk.Button(tags_control_frame, text="红色", command=lambda: filter_by_tag("red")).pack(side=tk.LEFT, padx=5)
tk.Button(tags_control_frame, text="绿色", command=lambda: filter_by_tag("green")).pack(side=tk.LEFT, padx=5)
tk.Button(tags_control_frame, text="蓝色", command=lambda: filter_by_tag("blue")).pack(side=tk.LEFT, padx=5)

# 创建状态标签
status_label = tk.Label(tags_frame, text="点击形状或使用按钮筛选", pady=10)
status_label.pack()

# 启动主事件循环
root.mainloop()