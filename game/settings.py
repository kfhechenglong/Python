class Settings():
  def __init__(self):
    self.screen_width = 1200
    self.screen_height = 800
    self.background_color=(230,230,230)
    # 设置飞船速度
    # 通过将速度设置指定为小数值，可在后面加快游戏的节奏时更细致地控制飞船的速度。然而，rect的centerx等属性只能存储整数值
    self.ship_speed_factor = 1.5
    # 子弹设置
    self.bullet_speed_factor = 1
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 60,60,60
    self.bullets_allowed = 3