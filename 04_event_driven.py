#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
04_event_driven.py - Tkinter事件驱动编程演示

演示内容：
- command属性绑定按钮动作
- <Button-1>/<KeyPress>等事件协议
- bind()方法实现高级事件捕获
- 事件对象解析 (x/y坐标, char按键字符)
"""

import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("与用户对话 - 事件驱动编程")
root.geometry("600x500+100+100")
root.configure(bg="#f5f5f5")

# 创建一个Notebook(选项卡控件)来展示不同的事件处理方式
nb = ttk.Notebook(root)
nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ===== 1. command属性绑定 =====
command_frame = ttk.Frame(nb, padding=10)
nb.add(command_frame, text="command属性")

# 创建说明标签
command_info = tk.Label(
    command_frame,
    text="command属性是最简单的事件绑定方式，\n通常用于按钮点击等简单交互",
    justify=tk.LEFT,
    pady=10
)
command_info.pack(anchor=tk.W)

# 创建一个框架来演示command属性
command_demo_frame = tk.LabelFrame(command_frame, text="command属性演示", padx=10, pady=10)
command_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建一个标签用于显示结果
result_label = tk.Label(
    command_demo_frame,
    text="点击下方按钮查看效果",
    font=("Arial", 12),
    pady=20
)
result_label.pack()

# 创建几个使用command属性的按钮
def show_message1():
    result_label.config(text="你点击了第一个按钮！")

def show_message2():
    result_label.config(text="你点击了第二个按钮！")

def show_message_with_param(message):
    result_label.config(text=message)

# 基本command用法
tk.Button(command_demo_frame, text="按钮1", command=show_message1).pack(pady=5)
tk.Button(command_demo_frame, text="按钮2", command=show_message2).pack(pady=5)

# 使用lambda传递参数
tk.Button(
    command_demo_frame, 
    text="带参数的按钮", 
    command=lambda: show_message_with_param("这是通过lambda传递的参数！")
).pack(pady=5)

# 使用不同的控件类型
var = tk.IntVar()

def checkbox_changed():
    if var.get() == 1:
        result_label.config(text="复选框已选中！")
    else:
        result_label.config(text="复选框已取消选中！")

tk.Checkbutton(
    command_demo_frame, 
    text="这是一个复选框", 
    variable=var, 
    command=checkbox_changed
).pack(pady=10)

# ===== 2. 事件协议绑定 =====
event_frame = ttk.Frame(nb, padding=10)
nb.add(event_frame, text="事件协议")

# 创建说明标签
event_info = tk.Label(
    event_frame,
    text="Tkinter提供了丰富的事件协议，\n可以通过bind()方法捕获各种用户交互",
    justify=tk.LEFT,
    pady=10
)
event_info.pack(anchor=tk.W)

# 创建一个框架来演示事件协议
event_demo_frame = tk.LabelFrame(event_frame, text="事件协议演示", padx=10, pady=10)
event_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建一个标签用于显示结果
event_result = tk.Label(
    event_demo_frame,
    text="在下方区域交互以触发事件",
    font=("Arial", 12),
    pady=10
)
event_result.pack()

# 创建一个画布用于演示鼠标事件
event_canvas = tk.Canvas(event_demo_frame, width=400, height=150, bg="white")
event_canvas.pack(pady=10)

# 绑定鼠标事件
def on_mouse_click(event):
    event_result.config(text=f"鼠标点击: 坐标({event.x}, {event.y})")
    # 在点击位置绘制一个小圆
    event_canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="red")

def on_mouse_move(event):
    event_result.config(text=f"鼠标移动: 坐标({event.x}, {event.y})")
    # 可选：绘制鼠标轨迹
    # event_canvas.create_oval(event.x-1, event.y-1, event.x+1, event.y+1, fill="blue")

def on_mouse_right_click(event):
    event_result.config(text="鼠标右键点击: 清除画布")
    event_canvas.delete("all")  # 清除画布上的所有内容

# 绑定事件
event_canvas.bind("<Button-1>", on_mouse_click)  # 鼠标左键点击
event_canvas.bind("<Motion>", on_mouse_move)      # 鼠标移动
event_canvas.bind("<Button-3>", on_mouse_right_click)  # 鼠标右键点击

# 创建一个输入框用于演示键盘事件
key_frame = tk.Frame(event_demo_frame)
key_frame.pack(pady=10, fill=tk.X)

tk.Label(key_frame, text="键盘事件测试:").pack(side=tk.LEFT, padx=5)

key_entry = tk.Entry(key_frame)
key_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

def on_key_press(event):
    event_result.config(text=f"按键按下: {event.char} (键码: {event.keycode})")

def on_return_key(event):
    event_result.config(text="回车键按下: 输入内容为 " + key_entry.get())
    key_entry.delete(0, tk.END)  # 清空输入框

# 绑定键盘事件
key_entry.bind("<KeyPress>", on_key_press)  # 任意键按下
key_entry.bind("<Return>", on_return_key)   # 回车键按下

# ===== 3. 高级事件处理 =====
advanced_frame = ttk.Frame(nb, padding=10)
nb.add(advanced_frame, text="高级事件处理")

# 创建说明标签
advanced_info = tk.Label(
    advanced_frame,
    text="高级事件处理包括事件传播、事件拦截和自定义事件等",
    justify=tk.LEFT,
    pady=10
)
advanced_info.pack(anchor=tk.W)

# 创建一个框架来演示高级事件处理
advanced_demo_frame = tk.LabelFrame(advanced_frame, text="高级事件处理演示", padx=10, pady=10)
advanced_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建嵌套框架来演示事件传播
outer_frame = tk.Frame(advanced_demo_frame, bg="#ffcccc", width=300, height=200)
outer_frame.pack(pady=10)
outer_frame.pack_propagate(False)  # 防止框架被子组件压缩

middle_frame = tk.Frame(outer_frame, bg="#ccffcc", width=200, height=150)
middle_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

inner_frame = tk.Frame(middle_frame, bg="#ccccff", width=100, height=100)
inner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 创建一个标签用于显示结果
advanced_result = tk.Label(
    advanced_demo_frame,
    text="点击不同颜色的区域查看事件传播",
    font=("Arial", 12),
    pady=10
)
advanced_result.pack()

# 绑定点击事件
def on_outer_click(event):
    advanced_result.config(text="点击了红色外层框架")
    return "break"  # 阻止事件继续传播

def on_middle_click(event):
    advanced_result.config(text="点击了绿色中层框架")
    # 不返回"break"，事件会继续传播

def on_inner_click(event):
    advanced_result.config(text="点击了蓝色内层框架")
    # 不返回"break"，事件会继续传播

outer_frame.bind("<Button-1>", on_outer_click)
middle_frame.bind("<Button-1>", on_middle_click)
inner_frame.bind("<Button-1>", on_inner_click)

# 创建一个按钮来演示事件绑定的优先级
def on_button_click(event):
    advanced_result.config(text="通过bind()方法捕获的按钮点击")
    return "break"  # 阻止command回调执行

def on_button_command():
    advanced_result.config(text="通过command属性捕获的按钮点击")

event_button = tk.Button(
    advanced_demo_frame, 
    text="测试事件优先级", 
    command=on_button_command
)
event_button.pack(pady=10)
event_button.bind("<Button-1>", on_button_click)

# 添加一个说明
tk.Label(
    advanced_demo_frame,
    text="注意: bind()方法绑定的事件处理函数会先于command属性执行\n如果bind()处理函数返回'break'，则command不会被调用",
    justify=tk.LEFT,
    pady=5
).pack()

# 启动主事件循环
root.mainloop()