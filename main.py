from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.clock import Clock
import random

Window.clearcolor = get_color_from_hex('#0a0a12')

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[40, 60, 40, 60], spacing=30)
        title = Label(text="KURDISH NEON LOGIC", font_size='32sp', color=get_color_from_hex('#00f0ff'), bold=True, size_hint=(1, 0.3))
        layout.add_widget(title)
        status = Label(text="[ SYSTEM STATUS: ONLINE ]\n[ PILOT MODE: ACTIVE ]", font_size='16sp', color=get_color_from_hex('#ff007f'), halign='center', size_hint=(1, 0.2))
        layout.add_widget(status)
        start_btn = Button(text="INITIALIZE HACK", font_size='20sp', bold=True, background_normal='', background_color=get_color_from_hex('#00f0ff'), color=get_color_from_hex('#0a0a12'), size_hint=(1, 0.2))
        start_btn.bind(on_press=self.start_game)
        layout.add_widget(start_btn)
        self.add_widget(layout)
        
    def start_game(self, instance):
        self.manager.current = 'game'

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # بەشی کاتژمێر (نوێ)
        self.time_left = 20
        self.timer_label = Label(text=f"TIME REMAINING: {self.time_left}s", font_size='18sp', color=get_color_from_hex('#ffff00'), size_hint=(1, 0.1))
        self.layout.add_widget(self.timer_label)
        
        self.target_val = random.randint(1, 15)
        self.target_label = Label(text=f"TARGET PORT: {self.target_val}", font_size='26sp', color=get_color_from_hex('#ff007f'), bold=True, size_hint=(1, 0.2))
        self.layout.add_widget(self.target_label)
        
        self.info_label = Label(text="Switch bits (8, 4, 2, 1) to match target", font_size='14sp', color=get_color_from_hex('#ffffff'), size_hint=(1, 0.1))
        self.layout.add_widget(self.info_label)
        
        self.bits_layout = GridLayout(cols=4, spacing=15, size_hint=(1, 0.25))
        self.bit_values = [8, 4, 2, 1]
        self.bit_states = [0, 0, 0, 0]
        self.bit_buttons = []
        
        for i in range(4):
            btn = Button(text="0", font_size='32sp', bold=True, background_normal='', background_color=get_color_from_hex('#1e1e2f'), color=get_color_from_hex('#ffffff'))
            btn.bind(on_press=lambda instance, x=i: self.toggle_bit(x))
            self.bit_buttons.append(btn)
            self.bits_layout.add_widget(btn)
            
        self.layout.add_widget(self.bits_layout)
        self.sum_label = Label(text="CURRENT LOGIC: 0", font_size='18sp', color=get_color_from_hex('#00f0ff'), size_hint=(1, 0.1))
        self.layout.add_widget(self.sum_label)
        
        self.next_btn = Button(text="NEXT PORT", font_size='18sp', bold=True, background_normal='', background_color=get_color_from_hex('#1a1a26'), disabled=True, size_hint=(1, 0.15))
        self.next_btn.bind(on_press=self.next_level)
        self.layout.add_widget(self.next_btn)
        self.add_widget(self.layout)
        
        # دەستپێکردنی کاتژمێرەکە لە پاشبنەمادا
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)
        self.game_over = False

    def on_enter(self):
        # کاتێک شاشەکە دەکرێتەوە کاتەکە نوێ دەبێتەوە
        self.reset_game()

    def update_timer(self, dt):
        if self.manager and self.manager.current == 'game' and not self.game_over:
            self.time_left -= 1
            self.timer_label.text = f"TIME REMAINING: {self.time_left}s"
            
            if self.time_left <= 5:
                self.timer_label.color = get_color_from_hex('#ff0000') # سوور دەبێت لە کاتی مەترسیدا
                
            if self.time_left <= 0:
                self.game_over = True
                self.target_label.text = "SYSTEM LOCKED!"
                self.target_label.color = get_color_from_hex('#ff0000')
                self.disable_all_buttons()

    def toggle_bit(self, index):
        if self.game_over: return
        
        if self.bit_states[index] == 0:
            self.bit_states[index] = 1
            self.bit_buttons[index].text = "1"
            self.bit_buttons[index].background_color = get_color_from_hex('#00f0ff')
            self.bit_buttons[index].color = get_color_from_hex('#0a0a12')
        else:
            self.bit_states[index] = 0
            self.bit_buttons[index].text = "0"
            self.bit_buttons[index].background_color = get_color_from_hex('#1e1e2f')
            self.bit_buttons[index].color = get_color_from_hex('#ffffff')
            
        current_sum = sum(self.bit_states[i] * self.bit_values[i] for i in range(4))
        self.sum_label.text = f"CURRENT LOGIC: {current_sum}"
        
        if current_sum == self.target_val:
            self.game_over = True
            self.target_label.text = "PORT HACKED!"
            self.target_label.color = get_color_from_hex('#00ff66')
            self.next_btn.disabled = False
            self.next_btn.background_color = get_color_from_hex('#ff007f')

    def next_level(self, instance):
        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.time_left = 20
        self.timer_label.text = f"TIME REMAINING: {self.time_left}s"
        self.timer_label.color = get_color_from_hex('#ffff00')
        self.target_val = random.randint(1, 15)
        self.target_label.text = f"TARGET PORT: {self.target_val}"
        self.target_label.color = get_color_from_hex('#ff007f')
        self.bit_states = [0, 0, 0, 0]
        for btn in self.bit_buttons:
            btn.text = "0"
            btn.background_color = get_color_from_hex('#1e1e2f')
            btn.color = get_color_from_hex('#ffffff')
            btn.disabled = False
        self.sum_label.text = "CURRENT LOGIC: 0"
        self.next_btn.disabled = True
        self.next_btn.background_color = get_color_from_hex('#1a1a26')

    def disable_all_buttons(self):
        for btn in self.bit_buttons:
            btn.disabled = True
        # نیشاندانی دوگمەیەک بۆ دووبارە دەستپێکردنەوە لە کاتی دۆڕاندا
        self.next_btn.text = "RETRY HACK"
        self.next_btn.disabled = False
        self.next_btn.background_color = get_color_from_hex('#ff0000')

class KurdishNeonLogicApp(App):
    def build(self):
        self.title = "Kurdish Neon Logic"
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    KurdishNeonLogicApp().run()
