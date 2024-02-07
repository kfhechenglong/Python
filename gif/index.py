import imageio
from PIL import Image, ImageSequence
# 设置压缩尺寸
rp = 200

img_list = []
img = Image.open('./IMG_0192.gif')

for i in ImageSequence.Iterator(img):
  i = i.convert('RGB')
  if max(i.size[0], i.size[1]) > rp:
    i.thumbnail((rp,rp))
  img_list.append(i)
# 计算帧的频率
durt = (img.info)['duration'] / 1000
print(durt)
# 读取img_list合成新的gif
imageio.mimsave('new.gif', img_list, duration=durt)