import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
def run_game():
  # 初始化游戏，并创建一个屏幕对象
  pygame.init()
  as_setting = Settings()
  screen = pygame.display.set_mode((as_setting.screen_width,as_setting.screen_height))
  pygame.display.set_caption("Alien Invasion")
  # 设置背景颜色
  background_color=as_setting.background_color
  # 创建一艘飞船
  ship = Ship(as_setting, screen)
  # 创建存储子弹的编组
  bullets = Group()
  while True:
    gf.check_events(as_setting, screen,ship, bullets)
    ship.update()
    gf.update_buttets(bullets)
    gf.update_screen(as_setting, screen,ship, bullets)
run_game()