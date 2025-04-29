#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
10_modern_themes.py - Tkinter现代化主题与扩展演示

演示内容：
- ttk的样式引擎 (Style对象)
- 自定义widget皮肤 (XPLite风格)
- 集成第三方主题 (sun-valley等)
- 借助PIL实现高级图像支持
"""

import tkinter as tk
from tkinter import ttk
import os

# 创建主窗口
root = tk.Tk()
root.title("现代化进阶 - 主题与扩展")
root.geometry("800x600+100+100")

# 创建一个Notebook(选项卡控件)来展示不同的主题功能
nb = ttk.Notebook(root)
nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ===== 1. ttk样式引擎 =====
style_frame = ttk.Frame(nb, padding=10)
nb.add(style_frame, text="ttk样式引擎")

# 创建说明标签
style_info = tk.Label(
    style_frame,
    text="ttk模块提供了一个强大的样式引擎，可以自定义控件外观\n使用Style对象可以创建和修改主题样式",
    justify=tk.LEFT,
    pady=10
)
style_info.pack(anchor=tk.W)

# 创建Style对象
style = ttk.Style()

# 显示当前主题
current_theme = style.theme_use()
theme_label = tk.Label(
    style_frame,
    text=f"当前主题: {current_theme}",
    pady=5
)
theme_label.pack()

# 获取可用主题
available_themes = style.theme_names()
themes_label = tk.Label(
    style_frame,
    text=f"可用主题: {', '.join(available_themes)}",
    pady=5
)
themes_label.pack()

# 创建一个框架来展示不同主题的控件
theme_demo_frame = tk.LabelFrame(style_frame, text="主题演示", padx=10, pady=10)
theme_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建一个函数来更改主题
def change_theme(theme_name):
    style.theme_use(theme_name)
    theme_label.config(text=f"当前主题: {theme_name}")

# 创建主题选择按钮
theme_buttons_frame = tk.Frame(theme_demo_frame)
theme_buttons_frame.pack(fill=tk.X, pady=10)

for theme in available_themes:
    ttk.Button(
        theme_buttons_frame,
        text=theme,
        command=lambda t=theme: change_theme(t)
    ).pack(side=tk.LEFT, padx=5)

# 创建各种ttk控件进行演示
widgets_frame = tk.Frame(theme_demo_frame)
widgets_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 左侧控件
left_frame = tk.Frame(widgets_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

ttk.Label(left_frame, text="标签 (ttk.Label)").pack(anchor=tk.W, pady=5)
ttk.Button(left_frame, text="按钮 (ttk.Button)").pack(anchor=tk.W, pady=5)
ttk.Checkbutton(left_frame, text="复选框 (ttk.Checkbutton)").pack(anchor=tk.W, pady=5)

radio_var = tk.StringVar(value="选项1")
ttk.Radiobutton(left_frame, text="单选按钮1 (ttk.Radiobutton)", variable=radio_var, value="选项1").pack(anchor=tk.W, pady=2)
ttk.Radiobutton(left_frame, text="单选按钮2 (ttk.Radiobutton)", variable=radio_var, value="选项2").pack(anchor=tk.W, pady=2)

ttk.Entry(left_frame).pack(anchor=tk.W, pady=5, fill=tk.X)

# 右侧控件
right_frame = tk.Frame(widgets_frame)
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

ttk.Combobox(right_frame, values=["组合框", "选项1", "选项2", "选项3"]).pack(anchor=tk.W, pady=5, fill=tk.X)
ttk.Spinbox(right_frame, from_=0, to=100).pack(anchor=tk.W, pady=5, fill=tk.X)

ttk.Scale(right_frame, from_=0, to=100, orient=tk.HORIZONTAL).pack(anchor=tk.W, pady=5, fill=tk.X)

progress = ttk.Progressbar(right_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress.pack(anchor=tk.W, pady=5, fill=tk.X)
progress['value'] = 75

ttk.Separator(right_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)

ttk.Button(right_frame, text="禁用按钮", state=tk.DISABLED).pack(anchor=tk.W, pady=5)

# ===== 2. 自定义样式 =====
custom_frame = ttk.Frame(nb, padding=10)
nb.add(custom_frame, text="自定义样式")

# 创建说明标签
custom_info = tk.Label(
    custom_frame,
    text="可以使用Style对象自定义控件的外观\n通过configure和map方法设置控件的各种属性",
    justify=tk.LEFT,
    pady=10
)
custom_info.pack(anchor=tk.W)

# 创建一个框架来展示自定义样式
custom_demo_frame = tk.LabelFrame(custom_frame, text="自定义样式演示", padx=10, pady=10)
custom_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 创建自定义样式
def create_custom_style():
    # 创建蓝色按钮样式
    style.configure(
        "Blue.TButton",
        foreground="white",
        background="#0078d7",
        padding=10,
        font=("Arial", 10, "bold")
    )
    style.map(
        "Blue.TButton",
        foreground=[('pressed', 'white'), ('active', 'white')],
        background=[('pressed', '#00559b'), ('active', '#1e88e5')]
    )
    
    # 创建绿色按钮样式
    style.configure(
        "Green.TButton",
        foreground="white",
        background="#4caf50",
        padding=10,
        font=("Arial", 10, "bold")
    )
    style.map(
        "Green.TButton",
        foreground=[('pressed', 'white'), ('active', 'white')],
        background=[('pressed', '#388e3c'), ('active', '#66bb6a')]
    )
    
    # 创建红色按钮样式
    style.configure(
        "Red.TButton",
        foreground="white",
        background="#f44336",
        padding=10,
        font=("Arial", 10, "bold")
    )
    style.map(
        "Red.TButton",
        foreground=[('pressed', 'white'), ('active', 'white')],
        background=[('pressed', '#c62828'), ('active', '#ef5350')]
    )
    
    # 创建自定义复选框样式
    style.configure(
        "Custom.TCheckbutton",
        foreground="#0078d7",
        font=("Arial", 10, "bold")
    )
    
    # 创建自定义进度条样式
    style.configure(
        "Custom.Horizontal.TProgressbar",
        troughcolor="#f0f0f0",
        background="#ff9800",
        thickness=20
    )

# 应用自定义样式
create_custom_style()

# 创建使用自定义样式的控件
ttk.Button(custom_demo_frame, text="蓝色按钮", style="Blue.TButton").pack(pady=10)
ttk.Button(custom_demo_frame, text="绿色按钮", style="Green.TButton").pack(pady=10)
ttk.Button(custom_demo_frame, text="红色按钮", style="Red.TButton").pack(pady=10)

ttk.Checkbutton(custom_demo_frame, text="自定义复选框", style="Custom.TCheckbutton").pack(pady=10)

custom_progress = ttk.Progressbar(
    custom_demo_frame,
    orient=tk.HORIZONTAL,
    length=300,
    mode='determinate',
    style="Custom.Horizontal.TProgressbar"
)
custom_progress.pack(pady=10)
custom_progress['value'] = 75

# 创建自定义框架样式
style.configure(
    "Custom.TFrame",
    background="#e0f7fa",
    relief="ridge",
    borderwidth=5
)

custom_styled_frame = ttk.Frame(
    custom_demo_frame,
    width=300,
    height=100,
    style="Custom.TFrame"
)
custom_styled_frame.pack(pady=10)

ttk.Label(
    custom_styled_frame,
    text="这是一个自定义样式的框架",
    background="#e0f7fa"
).pack(pady=30)

# ===== 3. 模拟第三方主题 =====
third_party_frame = ttk.Frame(nb, padding=10)
nb.add(third_party_frame, text="第三方主题")

# 创建说明标签
third_party_info = tk.Label(
    third_party_frame,
    text="Tkinter可以集成第三方主题，如sun-valley、azure等\n这里我们模拟几种流行的第三方主题效果",
    justify=tk.LEFT,
    pady=10
)
third_party_info.pack(anchor=tk.W)

# 创建一个框架来展示模拟的第三方主题
third_party_demo_frame = tk.LabelFrame(third_party_frame, text="第三方主题演示", padx=10, pady=10)
third_party_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 模拟不同的第三方主题
def apply_dark_theme():
    # 模拟暗色主题
    style.configure("TFrame", background="#2d2d30")
    style.configure("TLabel", background="#2d2d30", foreground="white")
    style.configure("TButton", background="#3e3e42", foreground="white")
    style.configure("TCheckbutton", background="#2d2d30", foreground="white")
    style.configure("TRadiobutton", background="#2d2d30", foreground="white")
    style.configure("TLabelframe", background="#2d2d30", foreground="white")
    style.configure("TLabelframe.Label", background="#2d2d30", foreground="white")
    
    # 更新窗口背景色
    third_party_demo_frame.config(bg="#2d2d30")
    third_party_info.config(bg="#2d2d30", fg="white")
    
    # 更新标题
    theme_title.config(text="暗色主题 (Dark Theme)", bg="#2d2d30", fg="white")

def apply_light_theme():
    # 模拟亮色主题
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", foreground="black")
    style.configure("TButton", background="#e1e1e1", foreground="black")
    style.configure("TCheckbutton", background="#f0f0f0", foreground="black")
    style.configure("TRadiobutton", background="#f0f0f0", foreground="black")
    style.configure("TLabelframe", background="#f0f0f0", foreground="black")
    style.configure("TLabelframe.Label", background="#f0f0f0", foreground="black")
    
    # 更新窗口背景色
    third_party_demo_frame.config(bg="#f0f0f0")
    third_party_info.config(bg="#f0f0f0", fg="black")
    
    # 更新标题
    theme_title.config(text="亮色主题 (Light Theme)", bg="#f0f0f0", fg="black")

def apply_blue_theme():
    # 模拟蓝色主题
    style.configure("TFrame", background="#e3f2fd")
    style.configure("TLabel", background="#e3f2fd", foreground="#0d47a1")
    style.configure("TButton", background="#bbdefb", foreground="#0d47a1")
    style.configure("TCheckbutton", background="#e3f2fd", foreground="#0d47a1")
    style.configure("TRadiobutton", background="#e3f2fd", foreground="#0d47a1")
    style.configure("TLabelframe", background="#e3f2fd", foreground="#0d47a1")
    style.configure("TLabelframe.Label", background="#e3f2fd", foreground="#0d47a1")
    
    # 更新窗口背景色
    third_party_demo_frame.config(bg="#e3f2fd")
    third_party_info.config(bg="#e3f2fd", fg="#0d47a1")
    
    # 更新标题
    theme_title.config(text="蓝色主题 (Blue Theme)", bg="#e3f2fd", fg="#0d47a1")

# 创建主题标题
theme_title = tk.Label(
    third_party_demo_frame,
    text="选择一个主题",
    font=("Arial", 14, "bold"),
    pady=10
)
theme_title.pack()

# 创建主题选择按钮
theme_buttons_frame = tk.Frame(third_party_demo_frame)
theme_buttons_frame.pack(pady=10)

ttk.Button(theme_buttons_frame, text="暗色主题", command=apply_dark_theme).pack(side=tk.LEFT, padx=5)
ttk.Button(theme_buttons_frame, text="亮色主题", command=apply_light_theme).pack(side=tk.LEFT, padx=5)
ttk.Button(theme_buttons_frame, text="蓝色主题", command=apply_blue_theme).pack(side=tk.LEFT, padx=5)

# 创建一些控件来展示主题效果
theme_widgets_frame = ttk.Frame(third_party_demo_frame)
theme_widgets_frame.pack(fill=tk.BOTH, expand=True, pady=10)

ttk.Label(theme_widgets_frame, text="这是一个标签").pack(pady=5)
ttk.Button(theme_widgets_frame, text="这是一个按钮").pack(pady=5)
ttk.Checkbutton(theme_widgets_frame, text="这是一个复选框").pack(pady=5)

theme_radio_var = tk.StringVar(value="选项1")
ttk.Radiobutton(theme_widgets_frame, text="选项1", variable=theme_radio_var, value="选项1").pack(pady=2)
ttk.Radiobutton(theme_widgets_frame, text="选项2", variable=theme_radio_var, value="选项2").pack(pady=2)

ttk.Separator(theme_widgets_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)

ttk.Entry(theme_widgets_frame).pack(pady=5, fill=tk.X)

# ===== 4. PIL图像支持 =====
pil_frame = ttk.Frame(nb, padding=10)
nb.add(pil_frame, text="PIL图像支持")

# 创建说明标签
pil_info = tk.Label(
    pil_frame,
    text="PIL (Pillow) 库可以提供更强大的图像处理能力\n支持更多图像格式，并可以进行图像处理和转换",
    justify=tk.LEFT,
    pady=10
)
pil_info.pack(anchor=tk.W)

# 创建一个框架来展示PIL功能
pil_demo_frame = tk.LabelFrame(pil_frame, text="PIL图像支持演示", padx=10, pady=10)
pil_demo_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# 由于没有实际安装PIL，我们只展示代码示例
pil_code = """# PIL图像处理示例代码
from PIL import Image, ImageTk
import tkinter as tk

# 打开图像文件
image = Image.open("example.jpg")

# 调整图像大小
image = image.resize((300, 200), Image.LANCZOS)

# 转换为PhotoImage对象
photo = ImageTk.PhotoImage(image)

# 在Label中显示图像
label = tk.Label(root, image=photo)
label.image = photo  # 保持引用
label.pack()

# 图像处理示例
from PIL import ImageFilter, ImageEnhance

# 应用滤镜
blurred = image.filter(ImageFilter.BLUR)
sharpened = image.filter(ImageFilter.SHARPEN)
edges = image.filter(ImageFilter.FIND_EDGES)

# 调整亮度、对比度等
enhancer = ImageEnhance.Brightness(image)
brighter = enhancer.enhance(1.5)  # 增加亮度50%

enhancer = ImageEnhance.Contrast(image)
higher_contrast = enhancer.enhance(1.5)  # 增加对比度50%

# 转换模式
grayscale = image.convert('L')  # 转为灰度图
"""

# 创建代码示例标签
pil_code_label = tk.Label(
    pil_demo_frame,
    text=pil_code,
    justify=tk.LEFT,
    font=("Courier", 10),
    bg="#f5f5f5",
    relief=tk.GROOVE,
    padx=10,
    pady=10
)
pil_code_label.pack(pady=10, fill=tk.BOTH, expand=True)

# 创建安装说明
pil_install_label = tk.Label(
    pil_demo_frame,
    text="要使用PIL功能，需要先安装Pillow库:\npip install pillow",
    justify=tk.LEFT,
    font=("Arial", 10, "bold"),
    fg="#d32f2f",
    pady=10
)
pil_install_label.pack()

# 创建模拟的图像处理效果展示
pil_effects_frame = tk.Frame(pil_demo_frame)
pil_effects_frame.pack(fill=tk.X, pady=10)

# 创建几个彩色方块来模拟图像处理效果
effects = [
    ("原图", "#ffffff"),
    ("模糊", "#e0e0e0"),
    ("锐化", "#bdbdbd"),
    ("边缘检测", "#9e9e9e"),
    ("增亮", "#ffecb3"),
    ("增加对比度", "#b3e5fc"),
    ("灰度", "#757575")
]

for name, color in effects:
    effect_frame = tk.Frame(pil_effects_frame)
    effect_frame.pack(side=tk.LEFT, padx=5)
    
    # 创建彩色方块
    canvas = tk.Canvas(effect_frame, width=80, height=60, bg=color, bd=1, relief=tk.RAISED)
    canvas.pack()
    
    # 添加效果名称
    tk.Label(effect_frame, text=name).pack()

# 启动主事件循环
root.mainloop()