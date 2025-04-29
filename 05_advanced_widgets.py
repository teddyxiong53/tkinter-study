#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
05_advanced_widgets.py - Tkinter高级控件演示

演示内容：
- Checkbutton与IntVar状态监控
- Radiobutton单选组的实现技巧
- Scale滑动条的数值控制
- Spinbox数字调节器的回调机制
"""

import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("输入与选择 - 高级控件")
root.geometry("600x650+100+100")
root.configure(bg="#f5f5f5")

# 创建主框架
main_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# 创建标题标签
title_label = tk.Label(
    main_frame,
    text="Tkinter高级控件演示",
    font=("Arial", 16, "bold"),
    bg="#f5f5f5",
    pady=10
)
title_label.pack()

# ===== 1. Checkbutton与IntVar状态监控 =====
check_frame = tk.LabelFrame(main_frame, text="Checkbutton与IntVar状态监控", padx=10, pady=10, bg="#f5f5f5")
check_frame.pack(fill=tk.X, pady=10)

# 创建IntVar变量来存储复选框状态
check_var1 = tk.IntVar()
check_var2 = tk.IntVar()
check_var3 = tk.IntVar()

# 创建状态显示标签
check_status = tk.Label(
    check_frame,
    text="请选择您喜欢的编程语言",
    bg="#f5f5f5",
    pady=5
)
check_status.pack()

# 更新状态显示的函数
def update_check_status():
    selected = []
    if check_var1.get() == 1:
        selected.append("Python")
    if check_var2.get() == 1:
        selected.append("Java")
    if check_var3.get() == 1:
        selected.append("JavaScript")
    
    if selected:
        check_status.config(text=f"您选择了: {', '.join(selected)}")
    else:
        check_status.config(text="请选择您喜欢的编程语言")

# 创建复选框
check1 = tk.Checkbutton(
    check_frame,
    text="Python",
    variable=check_var1,
    command=update_check_status,
    bg="#f5f5f5"
)
check1.pack(anchor=tk.W, pady=2)

check2 = tk.Checkbutton(
    check_frame,
    text="Java",
    variable=check_var2,
    command=update_check_status,
    bg="#f5f5f5"
)
check2.pack(anchor=tk.W, pady=2)

check3 = tk.Checkbutton(
    check_frame,
    text="JavaScript",
    variable=check_var3,
    command=update_check_status,
    bg="#f5f5f5"
)
check3.pack(anchor=tk.W, pady=2)

# 添加全选/取消全选按钮
def select_all():
    check_var1.set(1)
    check_var2.set(1)
    check_var3.set(1)
    update_check_status()

def clear_all():
    check_var1.set(0)
    check_var2.set(0)
    check_var3.set(0)
    update_check_status()

button_frame = tk.Frame(check_frame, bg="#f5f5f5")
button_frame.pack(fill=tk.X, pady=5)

tk.Button(button_frame, text="全选", command=select_all, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="取消全选", command=clear_all, width=10).pack(side=tk.LEFT, padx=5)

# ===== 2. Radiobutton单选组的实现技巧 =====
radio_frame = tk.LabelFrame(main_frame, text="Radiobutton单选组的实现技巧", padx=10, pady=10, bg="#f5f5f5")
radio_frame.pack(fill=tk.X, pady=10)

# 创建IntVar变量来存储单选按钮状态
radio_var = tk.IntVar()
radio_var.set(0)  # 默认选择第一个选项

# 创建状态显示标签
radio_status = tk.Label(
    radio_frame,
    text="您选择了: 初学者",
    bg="#f5f5f5",
    pady=5
)
radio_status.pack()

# 更新状态显示的函数
def update_radio_status():
    value = radio_var.get()
    if value == 0:
        radio_status.config(text="您选择了: 初学者")
    elif value == 1:
        radio_status.config(text="您选择了: 中级开发者")
    elif value == 2:
        radio_status.config(text="您选择了: 高级开发者")

# 创建单选按钮
levels = [("初学者", 0), ("中级开发者", 1), ("高级开发者", 2)]

for text, value in levels:
    radio = tk.Radiobutton(
        radio_frame,
        text=text,
        variable=radio_var,
        value=value,
        command=update_radio_status,
        bg="#f5f5f5"
    )
    radio.pack(anchor=tk.W, pady=2)

# 创建水平排列的单选按钮组
radio_frame2 = tk.Frame(radio_frame, bg="#f5f5f5")
radio_frame2.pack(fill=tk.X, pady=10)

tk.Label(radio_frame2, text="选择您的操作系统:", bg="#f5f5f5").pack(side=tk.LEFT, padx=5)

os_var = tk.StringVar()
os_var.set("windows")  # 默认选择

os_types = [("Windows", "windows"), ("macOS", "macos"), ("Linux", "linux")]

for text, value in os_types:
    radio = tk.Radiobutton(
        radio_frame2,
        text=text,
        variable=os_var,
        value=value,
        bg="#f5f5f5"
    )
    radio.pack(side=tk.LEFT, padx=10)

# ===== 3. Scale滑动条的数值控制 =====
scale_frame = tk.LabelFrame(main_frame, text="Scale滑动条的数值控制", padx=10, pady=10, bg="#f5f5f5")
scale_frame.pack(fill=tk.X, pady=10)

# 创建状态显示标签
scale_status = tk.Label(
    scale_frame,
    text="当前值: 50",
    bg="#f5f5f5",
    pady=5
)
scale_status.pack()

# 创建一个框架来容纳颜色预览
color_preview = tk.Frame(scale_frame, width=100, height=100, bg="#808080")
color_preview.pack(pady=10)
color_preview.pack_propagate(False)  # 防止框架被子组件压缩

# 创建RGB颜色滑动条
color_values = {"R": 128, "G": 128, "B": 128}

def update_color(*args):
    # 更新颜色预览
    r = color_values["R"]
    g = color_values["G"]
    b = color_values["B"]
    color_hex = f"#{r:02x}{g:02x}{b:02x}"
    color_preview.config(bg=color_hex)
    scale_status.config(text=f"RGB: ({r}, {g}, {b}) - HEX: {color_hex}")

# 创建RGB滑动条
for color, default in color_values.items():
    color_frame = tk.Frame(scale_frame, bg="#f5f5f5")
    color_frame.pack(fill=tk.X, pady=5)
    
    tk.Label(color_frame, text=f"{color}:", width=3, bg="#f5f5f5").pack(side=tk.LEFT, padx=5)
    
    def on_scale_change(value, color=color):
        color_values[color] = int(float(value))
        update_color()
    
    scale = tk.Scale(
        color_frame,
        from_=0,
        to=255,
        orient=tk.HORIZONTAL,
        length=300,
        command=lambda v, c=color: on_scale_change(v, c),
        bg="#f5f5f5"
    )
    scale.set(default)
    scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    # 添加数值显示
    value_label = tk.Label(color_frame, text=str(default), width=3, bg="#f5f5f5")
    value_label.pack(side=tk.LEFT, padx=5)
    
    # 更新数值显示
    def update_value_label(val, label=value_label):
        label.config(text=str(int(float(val))))
    
    scale.config(command=lambda v, c=color, l=value_label: (on_scale_change(v, c), update_value_label(v, l)))

# ===== 4. Spinbox数字调节器的回调机制 =====
spin_frame = tk.LabelFrame(main_frame, text="Spinbox数字调节器的回调机制", padx=10, pady=10, bg="#f5f5f5")
spin_frame.pack(fill=tk.X, pady=10)

# 创建状态显示标签
spin_status = tk.Label(
    spin_frame,
    text="请使用Spinbox调整数值",
    bg="#f5f5f5",
    pady=5
)
spin_status.pack()

# 创建数值Spinbox
def on_spin_change():
    try:
        value = int(spin1.get())
        spin_status.config(text=f"当前数值: {value}")
    except ValueError:
        spin_status.config(text="请输入有效的数字")

spin_frame1 = tk.Frame(spin_frame, bg="#f5f5f5")
spin_frame1.pack(fill=tk.X, pady=5)

tk.Label(spin_frame1, text="数值调节:", bg="#f5f5f5").pack(side=tk.LEFT, padx=5)

spin1 = tk.Spinbox(
    spin_frame1,
    from_=0,
    to=100,
    increment=1,
    width=10,
    command=on_spin_change
)
spin1.pack(side=tk.LEFT, padx=5)
spin1.delete(0, tk.END)
spin1.insert(0, "50")

# 创建带有验证功能的Spinbox
def validate_float(value):
    try:
        if value == "" or value == "-":
            return True
        float(value)
        return True
    except ValueError:
        return False

validate_cmd = root.register(validate_float)

spin_frame2 = tk.Frame(spin_frame, bg="#f5f5f5")
spin_frame2.pack(fill=tk.X, pady=5)

tk.Label(spin_frame2, text="浮点数调节:", bg="#f5f5f5").pack(side=tk.LEFT, padx=5)

spin2 = tk.Spinbox(
    spin_frame2,
    from_=-10.0,
    to=10.0,
    increment=0.1,
    width=10,
    validate="key",
    validatecommand=(validate_cmd, "%P")
)
spin2.pack(side=tk.LEFT, padx=5)
spin2.delete(0, tk.END)
spin2.insert(0, "0.0")

# 创建选项Spinbox
spin_frame3 = tk.Frame(spin_frame, bg="#f5f5f5")
spin_frame3.pack(fill=tk.X, pady=5)

tk.Label(spin_frame3, text="选项调节:", bg="#f5f5f5").pack(side=tk.LEFT, padx=5)

days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

def on_day_change():
    spin_status.config(text=f"您选择了: {spin3.get()}")

spin3 = tk.Spinbox(
    spin_frame3,
    values=days,
    width=10,
    command=on_day_change
)
spin3.pack(side=tk.LEFT, padx=5)

# 启动主事件循环
root.mainloop()