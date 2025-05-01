#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import wx.adv
import os
import sys

class MusicPlayerFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='音乐播放器', size=(1024, 768), style=wx.DEFAULT_FRAME_STYLE)
        
        # 设置图标和背景颜色
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        
        # 创建主面板
        self.main_panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 创建顶部面板（搜索栏和用户信息）
        self.create_top_panel()
        
        # 创建内容面板
        self.create_content_panel()
        
        # 创建底部播放控制面板
        self.create_player_controls()
        
        # 设置主面板布局
        main_sizer.Add(self.top_panel, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.content_panel, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.player_panel, 0, wx.EXPAND | wx.ALL, 5)
        
        self.main_panel.SetSizer(main_sizer)
        
        # 设置窗口居中
        self.Center()
    
    def create_top_panel(self):
        """创建顶部面板，包含搜索栏和用户信息"""
        self.top_panel = wx.Panel(self.main_panel)
        self.top_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 用户信息区域（左侧）
        user_panel = wx.Panel(self.top_panel)
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 用户头像
        avatar_size = 50
        avatar = wx.Bitmap(wx.Image(avatar_size, avatar_size).ConvertToMono(0, 0, 0))
        avatar_ctrl = wx.StaticBitmap(user_panel, bitmap=avatar)
        
        # 用户信息
        user_info = wx.BoxSizer(wx.VERTICAL)
        user_name = wx.StaticText(user_panel, label="Farzan Faruk")
        user_name.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        user_email = wx.StaticText(user_panel, label="Loova.studio@gmail.com")
        user_email.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        user_email.SetForegroundColour(wx.Colour(120, 120, 120))
        
        user_info.Add(user_name, 0, wx.BOTTOM, 2)
        user_info.Add(user_email, 0)
        
        user_sizer.Add(avatar_ctrl, 0, wx.RIGHT, 10)
        user_sizer.Add(user_info, 0, wx.ALIGN_CENTER_VERTICAL)
        user_panel.SetSizer(user_sizer)
        
        # 搜索栏（中间）
        search_panel = wx.Panel(self.top_panel)
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        search_ctrl = wx.SearchCtrl(search_panel, size=(300, 30), style=wx.TE_PROCESS_ENTER)
        search_ctrl.SetDescriptiveText("Search for song, artists etc...")
        search_ctrl.ShowSearchButton(True)
        search_ctrl.ShowCancelButton(True)
        
        search_sizer.Add(search_ctrl, 1, wx.EXPAND)
        search_panel.SetSizer(search_sizer)
        
        # 右侧按钮区域
        buttons_panel = wx.Panel(self.top_panel)
        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 设置按钮
        settings_btn = wx.Button(buttons_panel, label="⚙️", size=(30, 30), style=wx.BORDER_NONE)
        settings_btn.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        # 升级按钮
        upgrade_btn = wx.Button(buttons_panel, label="Upgrade Pro", size=(100, 30))
        upgrade_btn.SetBackgroundColour(wx.Colour(255, 50, 50))
        upgrade_btn.SetForegroundColour(wx.WHITE)
        
        buttons_sizer.Add(settings_btn, 0, wx.RIGHT, 10)
        buttons_sizer.Add(upgrade_btn, 0)
        buttons_panel.SetSizer(buttons_sizer)
        
        # 添加到顶部布局
        top_sizer.Add(user_panel, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 20)
        top_sizer.Add(search_panel, 1, wx.ALIGN_CENTER_VERTICAL)
        top_sizer.Add(buttons_panel, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        
        self.top_panel.SetSizer(top_sizer)
    
    def create_content_panel(self):
        """创建内容面板，包含侧边栏和主内容区"""
        self.content_panel = wx.Panel(self.main_panel)
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 创建侧边栏
        self.create_sidebar()
        
        # 创建主内容区
        self.create_main_content()
        
        content_sizer.Add(self.sidebar_panel, 0, wx.EXPAND | wx.RIGHT, 10)
        content_sizer.Add(self.main_content_panel, 1, wx.EXPAND)
        
        self.content_panel.SetSizer(content_sizer)
    
    def create_sidebar(self):
        """创建侧边栏"""
        self.sidebar_panel = wx.Panel(self.content_panel)
        self.sidebar_panel.SetBackgroundColour(wx.Colour(250, 250, 250))
        sidebar_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 主导航菜单
        nav_title = wx.StaticText(self.sidebar_panel, label="")
        nav_items = ["Home", "Browse", "Album", "Artists", "Videos"]
        nav_icons = ["🏠", "🔍", "💿", "👤", "🎬"]
        
        for i, (item, icon) in enumerate(zip(nav_items, nav_icons)):
            btn = wx.Button(self.sidebar_panel, label=f"{icon} {item}", size=(-1, 40), style=wx.BORDER_NONE | wx.ALIGN_LEFT)
            btn.SetBackgroundColour(wx.Colour(250, 250, 250))
            if i == 0:  # 高亮当前选中项
                btn.SetBackgroundColour(wx.Colour(240, 240, 255))
                btn.SetForegroundColour(wx.Colour(0, 0, 200))
            sidebar_sizer.Add(btn, 0, wx.EXPAND | wx.BOTTOM, 5)
        
        # 我的音乐区域
        sidebar_sizer.Add(wx.StaticLine(self.sidebar_panel), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)
        my_music_title = wx.StaticText(self.sidebar_panel, label="MY MUSIC")
        my_music_title.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sidebar_sizer.Add(my_music_title, 0, wx.ALL, 5)
        
        my_music_items = ["Recently Played", "Local Files"]
        my_music_icons = ["🕒", "📁"]
        
        for item, icon in zip(my_music_items, my_music_icons):
            btn = wx.Button(self.sidebar_panel, label=f"{icon} {item}", size=(-1, 40), style=wx.BORDER_NONE | wx.ALIGN_LEFT)
            btn.SetBackgroundColour(wx.Colour(250, 250, 250))
            sidebar_sizer.Add(btn, 0, wx.EXPAND | wx.BOTTOM, 5)
        
        # 设备信息
        sidebar_sizer.Add(wx.StaticLine(self.sidebar_panel), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)
        device_panel = wx.Panel(self.sidebar_panel)
        device_panel.SetBackgroundColour(wx.Colour(240, 240, 240))
        device_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        device_icon = wx.StaticText(device_panel, label="📱")
        device_icon.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        device_info = wx.BoxSizer(wx.VERTICAL)
        device_name = wx.StaticText(device_panel, label="iPhone X")
        device_name.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        device_storage = wx.StaticText(device_panel, label="128 GB")
        device_storage.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        device_storage.SetForegroundColour(wx.Colour(120, 120, 120))
        
        device_info.Add(device_name, 0, wx.BOTTOM, 2)
        device_info.Add(device_storage, 0)
        
        device_sizer.Add(device_icon, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        device_sizer.Add(device_info, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        device_panel.SetSizer(device_sizer)
        
        sidebar_sizer.Add(device_panel, 0, wx.EXPAND | wx.ALL, 5)
        
        self.sidebar_panel.SetSizer(sidebar_sizer)
    
    def create_main_content(self):
        """创建主内容区"""
        self.main_content_panel = wx.Panel(self.content_panel)
        main_content_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Billboard Topchart 区域
        topchart_panel = wx.Panel(self.main_content_panel)
        topchart_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 标题和导航按钮
        title_bar = wx.BoxSizer(wx.HORIZONTAL)
        topchart_title = wx.StaticText(topchart_panel, label="Billboard Topchart")
        topchart_title.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        
        nav_buttons = wx.BoxSizer(wx.HORIZONTAL)
        prev_btn = wx.Button(topchart_panel, label="<", size=(30, 30))
        next_btn = wx.Button(topchart_panel, label=">", size=(30, 30))
        
        nav_buttons.Add(prev_btn, 0, wx.RIGHT, 5)
        nav_buttons.Add(next_btn, 0)
        
        title_bar.Add(topchart_title, 1, wx.ALIGN_CENTER_VERTICAL)
        title_bar.Add(nav_buttons, 0, wx.ALIGN_CENTER_VERTICAL)
        
        # 专辑封面区域
        albums_panel = wx.Panel(topchart_panel)
        albums_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        album_titles = ["Coloring Book", "Blue Neighbourhood", "Starboy", "Mirage", "Beerbongs"]
        album_artists = ["Chance The Rapper", "Troye Sivan", "The Weeknd", "Else Twin", "Post Malone"]
        
        for title, artist in zip(album_titles, album_artists):
            album_panel = wx.Panel(albums_panel)
            album_sizer = wx.BoxSizer(wx.VERTICAL)
            
            # 专辑封面（使用占位图）
            cover_size = 150
            cover = wx.Bitmap(wx.Image(cover_size, cover_size).ConvertToMono(0, 0, 0))
            cover_ctrl = wx.StaticBitmap(album_panel, bitmap=cover)
            
            # 专辑信息
            album_title = wx.StaticText(album_panel, label=title)
            album_title.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
            album_artist = wx.StaticText(album_panel, label=artist)
            album_artist.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
            album_artist.SetForegroundColour(wx.Colour(120, 120, 120))
            
            album_sizer.Add(cover_ctrl, 0, wx.BOTTOM, 5)
            album_sizer.Add(album_title, 0, wx.BOTTOM, 2)
            album_sizer.Add(album_artist, 0)
            
            album_panel.SetSizer(album_sizer)
            albums_sizer.Add(album_panel, 0, wx.RIGHT, 15)
        
        albums_panel.SetSizer(albums_sizer)
        
        topchart_sizer.Add(title_bar, 0, wx.EXPAND | wx.BOTTOM, 10)
        topchart_sizer.Add(albums_panel, 0, wx.EXPAND)
        topchart_panel.SetSizer(topchart_sizer)
        
        # 播放列表区域
        playlists_panel = wx.Panel(self.main_content_panel)
        playlists_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 热门歌曲列表
        popular_panel = wx.Panel(playlists_panel)
        popular_sizer = wx.BoxSizer(wx.VERTICAL)
        
        popular_title = wx.StaticText(popular_panel, label="Most Popular")
        popular_title.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        popular_count = wx.StaticText(popular_panel, label="16 songs")
        popular_count.SetForegroundColour(wx.Colour(120, 120, 120))
        
        popular_header = wx.BoxSizer(wx.HORIZONTAL)
        popular_header.Add(popular_title, 0, wx.BOTTOM, 2)
        popular_header.Add(popular_count, 0, wx.LEFT | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 10)
        
        # 歌曲列表
        songs_panel = wx.Panel(popular_panel)
        songs_sizer = wx.BoxSizer(wx.VERTICAL)
        
        song_titles = ["My Stress", "Mirage", "My Stress", "The Hills", "Paralyzed", "Timeless"]
        song_artists = ["NF Real music", "Else Twin", "NF Real music", "The Weeknd", "NF Real music", "Lucidious"]
        song_times = ["3:22", "4:23", "3:58", "5:33", "5:06", "3:50"]
        
        for i, (title, artist, time) in enumerate(zip(song_titles, song_artists, song_times)):
            song_panel = wx.Panel(songs_panel)
            song_panel.SetBackgroundColour(wx.Colour(250, 250, 250) if i % 2 == 0 else wx.Colour(255, 255, 255))
            song_sizer = wx.BoxSizer(wx.HORIZONTAL)
            
            # 序号
            index = wx.StaticText(song_panel, label=f"01")
            index.SetForegroundColour(wx.Colour(120, 120, 120))
            
            # 歌曲封面（小图标）
            cover_size = 40
            cover = wx.Bitmap(wx.Image(cover_size, cover_size).ConvertToMono(0, 0, 0))
            cover_ctrl = wx.StaticBitmap(song_panel, bitmap=cover)
            
            # 歌曲信息
            song_info = wx.BoxSizer(wx.VERTICAL)
            song_title = wx.StaticText(song_panel, label=title)
            song_title.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
            song_artist = wx.StaticText(song_panel, label=artist)
            song_artist.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
            song_artist.SetForegroundColour(wx.Colour(120, 120, 120))
            
            song_info.Add(song_title, 0, wx.BOTTOM, 2)
            song_info.Add(song_artist, 0)
            
            # 时长
            duration = wx.StaticText(song_panel, label=time)
            duration.SetForegroundColour(wx.Colour(120, 120, 120))
            
            # 喜欢按钮
            like_btn = wx.Button(song_panel, label="❤️", size=(30, 30), style=wx.BORDER_NONE)
            if i % 2 == 0:  # 模拟一些歌曲被喜欢
                like_btn.SetForegroundColour(wx.Colour(255, 0, 0))
            else:
                like_btn.SetForegroundColour(wx.Colour(200, 200, 200))
            
            song_sizer.Add(index, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
            song_sizer.Add(cover_ctrl, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
            song_sizer.Add(song_info, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
            song_sizer.Add(duration, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
            song_sizer.Add(like_btn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
            
            song_panel.SetSizer(song_sizer)
            songs_sizer.Add(song_panel, 0, wx.EXPAND | wx.BOTTOM, 2)
        
        songs_panel.SetSizer(songs_sizer)
        
        popular_sizer.Add(popular_header, 0, wx.EXPAND | wx.BOTTOM, 10)
        popular_sizer.Add(songs_panel, 1, wx.EXPAND)
        popular_panel.SetSizer(popular_sizer)
        
        # 正在播放列表
        now_playing_panel = wx.Panel(playlists_panel)
        now_playing_sizer = wx.BoxSizer(wx.VERTICAL)
        
        now_playing_title = wx.StaticText(now_playing_panel, label="Now Playing")
        now_playing_title.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        now_playing_count = wx.StaticText(now_playing_panel, label="65 items on the list")
        now_playing_count.SetForegroundColour(wx.Colour(120, 120, 120))
        
        now_playing_header = wx.BoxSizer(wx.HORIZONTAL)
        now_playing_header.Add(now_playing_title, 0, wx.BOTTOM, 2)
        now_playing_header.Add(now_playing_count, 0, wx.LEFT | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 10)
        
        # 当前播放歌曲信息
        current_song_panel = wx.Panel(now_playing_panel)
        current_song_panel.SetBackgroundColour(wx.Colour(250, 250, 250))
        current_song_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 歌曲封面
        cover_size = 150
        cover = wx.Bitmap(wx.Image(cover_size, cover_size).ConvertToMono(0, 0, 0))
        cover_ctrl = wx.StaticBitmap(current_song_panel, bitmap=cover)
        
        # 歌曲信息
        song_info = wx.StaticText(current_song_panel, label="Chance The Rapper")
        song_info.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        
        # 进度条
        progress_panel = wx.Panel(current_song_panel)
        progress_sizer = wx.BoxSizer(wx.VERTICAL)
        
        slider = wx.Slider(progress_panel, value=30, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        
        time_sizer = wx.BoxSizer(wx.HORIZONTAL)
        current_time = wx.StaticText(progress_panel, label="2:10")
        current_time.SetForegroundColour(wx.Colour(120, 120, 120))
        total_time = wx.StaticText(progress_panel, label="-03:36")
        total_time.SetForegroundColour(wx.Colour(120, 120, 120))
        
        time_sizer.Add(current_time, 0)
        time_sizer.AddStretchSpacer()
        time_sizer.Add(total_time, 0)
        
        progress_sizer.Add(slider, 0, wx.EXPAND | wx.BOTTOM, 5)
        progress_sizer.Add(time_sizer, 0, wx.EXPAND)
        progress_panel.SetSizer(progress_sizer)
        
        # 播放控制按钮
        controls_panel = wx.Panel(current_song_panel)
        controls_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        shuffle_btn = wx.Button(controls_panel, label="🔀", size=(40, 40), style=wx.BORDER_NONE)
        prev_btn = wx.Button(controls_panel, label="⏮", size=(40, 40), style=wx.BORDER_NONE)
        play_btn = wx.Button(controls_panel, label="⏸", size=(40, 40), style=wx.BORDER_NONE)
        next_btn = wx.Button(controls_panel, label="⏭", size=(40, 40), style=wx.BORDER_NONE)
        repeat_btn = wx.Button(controls_panel, label="🔁", size=(40, 40), style=wx.BORDER_NONE)
        
        controls_sizer.AddStretchSpacer()
        controls_sizer.Add(shuffle_btn, 0, wx.RIGHT, 10)
        controls_sizer.Add(prev_btn, 0, wx.RIGHT, 10)
        controls_sizer.Add(play_btn, 0, wx.RIGHT, 10)
        controls_sizer.Add(next_btn, 0, wx.RIGHT, 10)
        controls_sizer.Add(repeat_btn, 0)
        controls_sizer.AddStretchSpacer()
        controls_panel.SetSizer(controls_sizer)
        
        current_song_sizer.Add(cover_ctrl, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        current_song_sizer.Add(song_info, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)
        current_song_sizer.Add(progress_panel, 0, wx.EXPAND | wx.ALL, 10)
        current_song_sizer.Add(controls_panel, 0, wx.EXPAND | wx.ALL, 10)
        
        current_song_panel.SetSizer(current_song_sizer)
        
        now_playing_sizer.Add(now_playing_header, 0, wx.EXPAND | wx.BOTTOM, 10)
        now_playing_sizer.Add(current_song_panel, 1, wx.EXPAND)
        now_playing_panel.SetSizer(now_playing_sizer)
        
        playlists_sizer.Add(popular_panel, 1, wx.EXPAND | wx.RIGHT, 20)
        playlists_sizer.Add(now_playing_panel, 1, wx.EXPAND)
        playlists_panel.SetSizer(playlists_sizer)
        
        main_content_sizer.Add(topchart_panel, 0, wx.EXPAND | wx.BOTTOM, 20)
        main_content_sizer.Add(playlists_panel, 1, wx.EXPAND)
        
        self.main_content_panel.SetSizer(main_content_sizer)
    
    def create_player_controls(self):
        """创建底部播放控制面板"""
        self.player_panel = wx.Panel(self.main_panel)
        self.player_panel.SetBackgroundColour(wx.Colour(245, 245, 245))
        player_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 这里可以添加底部播放控制器的UI元素
        # 但在图片中看不到底部控制器，所以这里留空
        
        self.player_panel.SetSizer(player_sizer)

class MusicPlayerApp(wx.App):
    def OnInit(self):
        frame = MusicPlayerFrame()
        frame.Show()
        return True

def main():
    app = MusicPlayerApp()
    app.MainLoop()

if __name__ == '__main__':
    main()