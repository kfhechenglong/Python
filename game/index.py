import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
def run_game():
  # 初始化游戏，并创建一个屏幕对象
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")
  # 创建一个用于存储游戏统计信息的实例
  stats = GameStats(ai_settings)
  # 设置背景颜色
  background_color=ai_settings.background_color
  # 创建一艘飞船
  ship = Ship(ai_settings, screen)
  # 创建存储子弹的编组
  bullets = Group()
  # 创建外星人
  aliens = Group()
  gf.create_fleet(ai_settings, screen,ship, aliens)
  while True:
    gf.check_events(ai_settings, screen,ship, bullets)
    if stats.game_active:
      ship.update()
      gf.update_buttets(ai_settings, screen, ship,aliens, bullets)
      gf.update_aliens(ai_settings,stats,screen,ship, aliens, bullets)
    gf.update_screen(ai_settings, screen,ship,aliens, bullets)
run_game()