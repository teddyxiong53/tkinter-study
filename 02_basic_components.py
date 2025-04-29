#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
02_basic_components.py - Tkinter基础组件演示

演示内容：
- Label/Button/Entry组件的属性调节
- 动态改变组件属性 (config()方法)
- 使用StringVar()实现动态文字绑定
- 颜色与字体系统 (命名规范/RGB/字体族)
"""

import tkinter as tk
from tkinter import font

# 创建主窗口
root = tk.Tk()
root.title("操控元素属性 - 基础组件")
root.geometry("500x600+100+100")
root.configure(bg="#f5f5f5")

# 创建一个Frame作为主容器
main_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# ===== 1. Label组件演示 =====
label_frame = tk.LabelFrame(main_frame, text="Label组件", padx=10, pady=10, bg="#f5f5f5")
label_frame.pack(fill=tk.X, pady=10)

# 创建不同样式的Label
label1 = tk.Label(label_frame, text="普通标签", bg="#f5f5f5")
label1.pack(anchor=tk.W, pady=5)

label2 = tk.Label(label_frame, text="自定义字体标签", font=("Arial", 12, "bold"), bg="#f5f5f5")
label2.pack(anchor=tk.W, pady=5)

label3 = tk.Label(label_frame, text="带颜色的标签", fg="#0066cc", bg="#e6f0ff", padx=5, pady=5)
label3.pack(anchor=tk.W, pady=5)

label4 = tk.Label(label_frame, text="带边框的标签", relief=tk.RIDGE, bd=2, padx=5, pady=5, bg="#f5f5f5")
label4.pack(anchor=tk.W, pady=5)

# ===== 2. Button组件演示 =====
button_frame = tk.LabelFrame(main_frame, text="Button组件", padx=10, pady=10, bg="#f5f5f5")
button_frame.pack(fill=tk.X, pady=10)

# 创建不同样式的Button
button1 = tk.Button(button_frame, text="普通按钮")
button1.pack(anchor=tk.W, pady=5)

button2 = tk.Button(button_frame, text="自定义颜色按钮", bg="#4CAF50", fg="white", activebackground="#45a049")
button2.pack(anchor=tk.W, pady=5)

button3 = tk.Button(button_frame, text="禁用状态按钮", state=tk.DISABLED)
button3.pack(anchor=tk.W, pady=5)

button4 = tk.Button(button_frame, text="带边框按钮", relief=tk.RAISED, bd=3)
button4.pack(anchor=tk.W, pady=5)

# ===== 3. Entry组件演示 =====
entry_frame = tk.LabelFrame(main_frame, text="Entry组件", padx=10, pady=10, bg="#f5f5f5")
entry_frame.pack(fill=tk.X, pady=10)

# 创建不同样式的Entry
entry1 = tk.Entry(entry_frame, width=30)
entry1.insert(0, "普通输入框")
entry1.pack(anchor=tk.W, pady=5)

entry2 = tk.Entry(entry_frame, width=30, show="*")
entry2.insert(0, "密码输入框")
entry2.pack(anchor=tk.W, pady=5)

entry3 = tk.Entry(entry_frame, width=30, bg="#e6f0ff", fg="#0066cc")
entry3.insert(0, "自定义颜色输入框")
entry3.pack(anchor=tk.W, pady=5)

entry4 = tk.Entry(entry_frame, width=30, bd=2, relief=tk.SUNKEN)
entry4.insert(0, "带边框输入框")
entry4.pack(anchor=tk.W, pady=5)

# ===== 4. 动态属性修改演示 =====
dynamic_frame = tk.LabelFrame(main_frame, text="动态属性修改", padx=10, pady=10, bg="#f5f5f5")
dynamic_frame.pack(fill=tk.X, pady=10)

# 创建一个可以动态修改的Label
dynamic_label = tk.Label(
    dynamic_frame, 
    text="这个标签可以被动态修改", 
    bg="#f5f5f5", 
    font=("Arial", 10)
)
dynamic_label.pack(pady=10)

# 创建控制按钮
control_frame = tk.Frame(dynamic_frame, bg="#f5f5f5")
control_frame.pack(fill=tk.X)

def change_text():
    dynamic_label.config(text="文本已被修改!")

def change_color():
    dynamic_label.config(fg="#cc0000")

def change_font():
    dynamic_label.config(font=("Arial", 12, "bold"))

def reset_label():
    dynamic_label.config(
        text="这个标签可以被动态修改",
        fg="black",
        font=("Arial", 10)
    )

tk.Button(control_frame, text="修改文本", command=change_text).pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="修改颜色", command=change_color).pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="修改字体", command=change_font).pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="重置", command=reset_label).pack(side=tk.LEFT, padx=5)

# ===== 5. StringVar绑定演示 =====
var_frame = tk.LabelFrame(main_frame, text="StringVar绑定", padx=10, pady=10, bg="#f5f5f5")
var_frame.pack(fill=tk.X, pady=10)

# 创建StringVar变量
name_var = tk.StringVar()
name_var.set("请输入您的名字")

# 创建绑定到StringVar的组件
name_entry = tk.Entry(var_frame, textvariable=name_var, width=30)
name_entry.pack(pady=10)

name_label = tk.Label(var_frame, textvariable=name_var, bg="#f5f5f5")
name_label.pack(pady=10)

# 创建一个按钮来修改StringVar
def greet_user():
    current_name = name_var.get()
    if current_name == "请输入您的名字" or current_name.strip() == "":
        name_var.set("您还没有输入名字")
    else:
        name_var.set(f"您好，{current_name}!")

tk.Button(var_frame, text="问候", command=greet_user).pack(pady=5)

# ===== 6. 字体和颜色系统演示 =====
font_color_frame = tk.LabelFrame(main_frame, text="字体和颜色系统", padx=10, pady=10, bg="#f5f5f5")
font_color_frame.pack(fill=tk.X, pady=10)

# 显示可用字体
available_fonts = font.families()
font_label = tk.Label(
    font_color_frame, 
    text=f"系统有 {len(available_fonts)} 种可用字体", 
    bg="#f5f5f5"
)
font_label.pack(anchor=tk.W, pady=5)

# 颜色示例
color_frame = tk.Frame(font_color_frame, bg="#f5f5f5")
color_frame.pack(fill=tk.X, pady=5)

colors = [
    ("#FF0000", "红色 (RGB: #FF0000)"),
    ("#00FF00", "绿色 (RGB: #00FF00)"),
    ("#0000FF", "蓝色 (RGB: #0000FF)"),
    ("orange", "橙色 (命名: orange)"),
    ("purple", "紫色 (命名: purple)")
]

for color_code, color_name in colors:
    color_sample = tk.Frame(color_frame, width=20, height=20, bg=color_code)
    color_sample.pack(side=tk.LEFT, padx=5)
    
    color_label = tk.Label(color_frame, text=color_name, bg="#f5f5f5")
    color_label.pack(side=tk.LEFT, padx=5, pady=5)

# 启动主事件循环
root.mainloop()