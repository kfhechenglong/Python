import sys
import pygame
from bullet import Bulllet
def check_keydown_events(event,ai_settings, screen,ship, bullets):
  if event.key == pygame.K_RIGHT:
    # 向右移动飞船
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    # 向左移动
    ship.moving_left = True
  elif event.key == pygame.K_SPACE:
    # 按下空格键，创建一颗子弹
    if len(bullets) < ai_settings.bullets_allowed:
      new_bullet = Bulllet(ai_settings, screen, ship)
      bullets.add(new_bullet)
def check_keyup_events(event,ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False
def check_events(ai_settings, screen,ship, bullets):
  # 监听键盘和鼠标事件
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event,ai_settings, screen,ship, bullets)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event,ship)
def update_screen(as_settings, screen, ship, bullets):
  screen.fill(as_settings.background_color)
  # 重绘子弹
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()
  pygame.display.flip()
def update_buttets(bullets):
  bullets.update()
  # 删除已经消失在界面外的子弹
  # 遍历删除需要使用子弹编组的副本
  for bullet in bullets.copy():
    if bullet.rect.bottom <=0:
      bullets.remove(bullet)