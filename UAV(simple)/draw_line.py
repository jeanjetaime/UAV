# import sys
from PIL import Image, ImageDraw

# lonList = [102.0, 103.0, 102.0, 104.0, 104.0, 105.0, 102.0]
# latList = [35.0, 32.0, 30.0, 30.0, 31.0, 33.0, 35.0]
# ID = "th2"

def draw_line(lonList, latList, ID, x1, y1, x2, y2):
    im = Image.open(ID)
    draw = ImageDraw.Draw(im) #实例化一个对象
    # (x1, y1) = (x1, y1)
    # (x2, y2) = (x2, y2)
    # (x1, y1) = (95.731456, 35.902192)
    # (x2, y2) = (109.897375, 29.66003)
    single_x = im.size[0] / (x2 - x1)
    single_y = im.size[1] / (y1 - y2)
    for i in range(len(lonList) - 1):
        a1, b1 = lonList[i], latList[i]
        a2, b2 = lonList[i + 1], latList[i + 1]
        a1 = (a1 - x1) * single_x + 10
        b1 = (y1 - b1) * single_y + 10
        a2 = (a2 - x1) * single_x + 10
        b2 = (y1 - b2) * single_y + 10
        draw.line((a1, b1) + (a2, b2), fill=(255, 0, 0), width=5)  #线的起点和终点，线宽
    im.save(ID)
# draw_line(lonList, latList, ID)
# 左上 95.731456,35.902192
# 右下 109.897375,29.66003