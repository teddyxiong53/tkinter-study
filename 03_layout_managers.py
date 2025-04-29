#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
03_layout_managers.py - Tkinter布局管理器演示

演示内容：
- pack()的填充与对齐 (side/fill/expand)
- grid()的行列权重配置 (rowconfigure/columnconfigure)
- place()精准定位技巧 (x/y相对定位)
- 混合布局的实践与边界处理
"""

import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("布局的艺术 - 几何管理器")
root.geometry("800x600+100+100")
root.configure(bg="#f0f0f0")

# 创建一个Notebook(选项卡控件)来展示不同的布局管理器
nb = ttk.Notebook(root)
nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ===== 1. pack()布局管理器 =====
pack_frame = ttk.Frame(nb, padding=10)
nb.add(pack_frame, text="pack()布局")

# 创建说明标签
pack_info = tk.Label(
    pack_frame,
    text="pack()布局管理器根据side参数决定组件的排列方向，\n可以使用fill和expand控制组件的填充行为",
    justify=tk.LEFT,
    pady=10
)
pack_info.pack(anchor=tk.W)

# 创建一个框架来演示side参数
side_demo_frame = tk.LabelFrame(pack_frame, text="side参数演示", padx=10, pady=10)
side_demo_frame.pack(fill=tk.X, pady=10)

# 创建四个不同side的按钮
tk.Button(side_demo_frame, text="左侧(side=LEFT)", bg="#ffcccc").pack(side=tk.LEFT, padx=5)
tk.Button(side_demo_frame, text="右侧(side=RIGHT)", bg="#ccffcc").pack(side=tk.RIGHT, padx=5)
tk.Button(side_demo_frame, text="顶部(side=TOP)", bg="#ccccff").pack(side=tk.TOP, pady=5)
tk.Button(side_demo_frame, text="底部(side=BOTTOM)", bg="#ffffcc").pack(side=tk.BOTTOM, pady=5)

# 创建一个框架来演示fill和expand参数
fill_demo_frame = tk.LabelFrame(pack_frame, text="fill和expand参数演示", padx=10, pady=10)
fill_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建三个不同fill和expand的按钮
tk.Button(fill_demo_frame, text="不填充(默认)").pack(pady=5)
tk.Button(fill_demo_frame, text="水平填充(fill=X)", bg="#e6f2ff").pack(fill=tk.X, pady=5)
tk.Button(fill_demo_frame, text="完全填充(fill=BOTH, expand=True)", bg="#ffe6e6").pack(fill=tk.BOTH, expand=True, pady=5)

# ===== 2. grid()布局管理器 =====
grid_frame = ttk.Frame(nb, padding=10)
nb.add(grid_frame, text="grid()布局")

# 创建说明标签
grid_info = tk.Label(
    grid_frame,
    text="grid()布局管理器使用行和列来定位组件，\n可以通过rowconfigure和columnconfigure设置权重",
    justify=tk.LEFT,
    pady=10
)
grid_info.pack(anchor=tk.W)

# 创建一个框架来演示grid布局
grid_demo_frame = tk.LabelFrame(grid_frame, text="grid布局演示", padx=10, pady=10)
grid_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 配置行和列的权重
for i in range(3):
    grid_demo_frame.columnconfigure(i, weight=1)  # 所有列等宽
    
grid_demo_frame.rowconfigure(2, weight=1)  # 第三行可以扩展

# 添加标签和输入框
tk.Label(grid_demo_frame, text="用户名:").grid(row=0, column=0, sticky=tk.W, pady=5)
tk.Entry(grid_demo_frame).grid(row=0, column=1, columnspan=2, sticky=tk.EW, pady=5)

tk.Label(grid_demo_frame, text="密码:").grid(row=1, column=0, sticky=tk.W, pady=5)
tk.Entry(grid_demo_frame, show="*").grid(row=1, column=1, columnspan=2, sticky=tk.EW, pady=5)

# 添加一个跨越多行多列的文本框
text_area = tk.Text(grid_demo_frame, height=5, width=30)
text_area.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW, pady=5)
text_area.insert(tk.END, "这个文本框跨越了3列，并且会随窗口调整大小")

# 添加按钮，使用不同的sticky选项
tk.Button(grid_demo_frame, text="取消").grid(row=3, column=1, sticky=tk.E, padx=5, pady=10)
tk.Button(grid_demo_frame, text="确定").grid(row=3, column=2, sticky=tk.W, padx=5, pady=10)

# ===== 3. place()布局管理器 =====
place_frame = ttk.Frame(nb, padding=10)
nb.add(place_frame, text="place()布局")

# 创建说明标签
place_info = tk.Label(
    place_frame,
    text="place()布局管理器允许精确定位组件，\n可以使用绝对坐标或相对坐标",
    justify=tk.LEFT,
    pady=10
)
place_info.pack(anchor=tk.W)

# 创建一个框架来演示place布局
place_demo_frame = tk.LabelFrame(place_frame, text="place布局演示", padx=10, pady=10)
place_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 设置place_demo_frame的最小尺寸，以便于观察
place_demo_frame.update()
place_demo_frame.config(width=400, height=300)

# 使用绝对坐标放置按钮
tk.Button(place_demo_frame, text="绝对位置(x=50, y=50)", bg="#ffcccc").place(x=50, y=50)

# 使用相对坐标放置按钮
tk.Button(place_demo_frame, text="相对位置(relx=0.5, rely=0.5)", bg="#ccffcc").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 使用绝对和相对混合放置按钮
tk.Button(place_demo_frame, text="混合位置(relx=0.8, y=30)", bg="#ccccff").place(relx=0.8, y=30, anchor=tk.NE)

# 使用宽度和高度控制按钮大小
tk.Button(place_demo_frame, text="控制大小(width=150, height=40)", bg="#ffffcc").place(x=50, y=150, width=150, height=40)

# 使用relwidth和relheight控制按钮大小
tk.Button(place_demo_frame, text="相对大小(relwidth=0.3, relheight=0.1)", bg="#e6f2ff").place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.1, anchor=tk.CENTER)

# ===== 4. 混合布局 =====
mixed_frame = ttk.Frame(nb, padding=10)
nb.add(mixed_frame, text="混合布局")

# 创建说明标签
mixed_info = tk.Label(
    mixed_frame,
    text="在实际应用中，常常需要混合使用不同的布局管理器\n以下是一个简单的表单示例，混合使用了pack和grid",
    justify=tk.LEFT,
    pady=10
)
mixed_info.pack(anchor=tk.W)

# 创建一个框架来演示混合布局
mixed_demo_frame = tk.Frame(mixed_frame, padx=10, pady=10)
mixed_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 使用pack创建顶部标题
title_label = tk.Label(
    mixed_demo_frame,
    text="用户注册表单",
    font=("Arial", 16, "bold"),
    pady=10
)
title_label.pack()

# 创建一个框架用于表单，使用grid布局
form_frame = tk.Frame(mixed_demo_frame, padx=20, pady=10)
form_frame.pack(fill=tk.X)

# 配置列权重
form_frame.columnconfigure(1, weight=1)

# 添加表单字段
fields = [("用户名:", ""), ("电子邮件:", ""), ("密码:", "*"), ("确认密码:", "*")]

for i, (label_text, show_char) in enumerate(fields):
    tk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky=tk.W, pady=5)
    
    entry = tk.Entry(form_frame)
    if show_char:
        entry.config(show=show_char)
    entry.grid(row=i, column=1, sticky=tk.EW, padx=5, pady=5)

# 创建一个框架用于按钮，使用pack布局
button_frame = tk.Frame(mixed_demo_frame, pady=15)
button_frame.pack()

tk.Button(button_frame, text="注册", width=10, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="取消", width=10).pack(side=tk.LEFT, padx=5)

# 启动主事件循环
root.mainloop()