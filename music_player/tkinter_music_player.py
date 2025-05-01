#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import os

# 添加现代化主题
from ttkthemes import ThemedStyle

class MusicPlayerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('音乐播放器')
        self.root.geometry('1024x768')
        
        # 应用现代化主题
        self.style = ThemedStyle(self.root)
        self.style.set_theme('arc')
        
        # 自定义样式
        self.style.configure('blue.TButton', foreground='#2C7BE5', font=('Arial', 10))
        self.style.configure('selected.TButton', foreground='white', background='#2C7BE5')
        
        # 主容器
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.create_top_bar()
        self.create_main_content()
        self.create_player_controls()

    def create_top_bar(self):
        top_frame = ttk.Frame(self.main_frame)
        top_frame.pack(fill=tk.X, pady=5)
        
        # 用户信息
        user_frame = ttk.Frame(top_frame)
        # 使用纯色块代替头像
        tk.Label(user_frame, bg='#2C7BE5', width=20, height=10).pack()
        
        # 用户头像标签组件替换
        tk.Label(user_frame, bg='#2C7BE5', width=10).pack(side=tk.LEFT, padx=5)
        user_info = ttk.Frame(user_frame)
        ttk.Label(user_info, text="Farzan Faruk", font=('Arial', 12, 'bold')).pack(anchor=tk.W)
        ttk.Label(user_info, text="Loova.studio@gmail.com", foreground='#666').pack(anchor=tk.W)
        user_info.pack(side=tk.LEFT, padx=10)
        user_frame.pack(side=tk.LEFT)
        
        # 搜索框
        search_frame = ttk.Frame(top_frame)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=40)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        # 使用文字图标代替图片
        ttk.Button(search_frame, text="🔍").pack(side=tk.LEFT)
        search_frame.pack(side=tk.LEFT, expand=True)
        
        # 右侧按钮
        btn_frame = ttk.Frame(top_frame)
        ttk.Button(btn_frame, text="⚙️", width=3).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Upgrade Pro", style='danger.TButton').pack(side=tk.LEFT)
        btn_frame.pack(side=tk.RIGHT)

    def create_sidebar(self, parent):
        # 侧边栏样式
        self.style.configure('Sidebar.TFrame', background='#F8F9FA')
        sidebar = ttk.Frame(parent, width=220, style='Sidebar.TFrame')
        
        nav_items = [
            ('🏠 Home', 'selected'),
            ('🔍 Browse', 'normal'),
            ('💿 Album', 'normal'),
            ('👤 Artists', 'normal'),
            ('🎬 Videos', 'normal')
        ]
        
        for text, state in nav_items:
            btn = ttk.Button(sidebar, text=text, style=f'{state}.TButton')
            btn.pack(fill=tk.X, pady=2, padx=5)
        
        # 我的音乐部分
        ttk.Separator(sidebar, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        ttk.Label(sidebar, text="MY MUSIC", font=('Arial', 10, 'bold')).pack(anchor=tk.W, padx=5)
        
        for item in ['🕒 Recently Played', '📁 Local Files']:
            ttk.Button(sidebar, text=item, style='blue.TButton').pack(fill=tk.X, pady=2, padx=5)
        
        return sidebar

    def create_album_display(self, parent):
        # 专辑网格布局
        album_frame = ttk.Frame(parent)
        
        # 标题栏
        title_frame = ttk.Frame(album_frame)
        ttk.Label(title_frame, text="Billboard Topchart", font=('Arial', 16, 'bold')).pack(side=tk.LEFT)
        ttk.Button(title_frame, text="<").pack(side=tk.RIGHT)
        ttk.Button(title_frame, text=">").pack(side=tk.RIGHT)
        title_frame.pack(fill=tk.X)
        
        # 专辑网格
        grid_frame = ttk.Frame(album_frame)
        for i in range(5):
            frame = ttk.Frame(grid_frame)
            # 使用纯色块代替专辑封面
            tk.Label(frame, bg='#2C7BE5', width=20, height=10).pack()
            ttk.Label(frame, text="专辑名称", font=('Arial', 10, 'bold')).pack()
            ttk.Label(frame, text="艺术家", foreground='#666').pack()
            
            frame.grid(row=i//3, column=i%3, padx=10, pady=10)
        
        grid_frame.pack(fill=tk.BOTH, expand=True)
        return album_frame

    def create_player_controls(self):
        # 底部播放控制
        control_frame = ttk.Frame(self.main_frame)
        
        # 进度条
        progress = ttk.Scale(control_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        progress.pack(fill=tk.X, padx=20)
        
        # 控制按钮
        btn_frame = ttk.Frame(control_frame)
        controls = ['⏮', '⏯', '⏭', '🔀', '🔁']
        
        for btn in controls:
            ttk.Button(btn_frame, text=btn, width=3).pack(side=tk.LEFT, padx=5)
        
        btn_frame.pack(pady=10)
        control_frame.pack(fill=tk.X)

    def create_main_content(self):
        # 创建主内容容器
        content_frame = ttk.Frame(self.main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
    
        # 创建侧边栏和主内容区
        sidebar = self.create_sidebar(content_frame)
        main_content = self.create_album_display(content_frame)
    
        # 布局管理
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = MusicPlayerApp()
    app.run()