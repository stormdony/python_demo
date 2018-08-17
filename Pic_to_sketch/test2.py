from PIL import Image
import os

def transform(imgName):
# 图像组成：红绿蓝  （RGB）三原色组成    亮度（255,255,255）
    image = imgName
    img = Image.open(image)
    img_all = "素描" + image
    new = Image.new("L", img.size, 255)
    width, height = img.size
    img = img.convert("L")

    print(img.size)
    print(img.mode) #RBG

    img_get = img.getpixel((0, 0))
    print(img_get) #三原色通道

    img_L=img.convert('L')
    print(img_L)
    img_get_L=img_L.getpixel((0,0))    #换算 得到灰度值
    print(img_get_L)

    # 定义画笔的大小
    Pen_size = 3
    # 色差扩散器
    Color_Diff = 6
    for i in range(Pen_size + 1, width - Pen_size - 1):
        for j in range(Pen_size + 1, height - Pen_size - 1):
            # 原始的颜色
            originalColor = 255
            lcolor = sum([img.getpixel((i - r, j)) for r in range(Pen_size)]) // Pen_size
            rcolor = sum([img.getpixel((i + r, j)) for r in range(Pen_size)]) // Pen_size

            # 通道----颜料
            if abs(lcolor - rcolor) > Color_Diff:
                originalColor -= (255 - img.getpixel((i, j))) // 4
                new.putpixel((i, j), originalColor)

            ucolor = sum([img.getpixel((i, j - r)) for r in range(Pen_size)]) // Pen_size
            dcolor = sum([img.getpixel((i, j + r)) for r in range(Pen_size)]) // Pen_size

            # 通道----颜料
            if abs(ucolor - dcolor) > Color_Diff:
                originalColor -= (255 - img.getpixel((i, j))) // 4
                new.putpixel((i, j), originalColor)

            acolor = sum([img.getpixel((i - r, j - r)) for r in range(Pen_size)]) // Pen_size
            bcolor = sum([img.getpixel((i + r, j + r)) for r in range(Pen_size)]) // Pen_size

            # 通道----颜料
            if abs(acolor - bcolor) > Color_Diff:
                originalColor -= (255 - img.getpixel((i, j))) // 4
                new.putpixel((i, j), originalColor)

            qcolor = sum([img.getpixel((i + r, j - r)) for r in range(Pen_size)]) // Pen_size
            wcolor = sum([img.getpixel((i - r, j + r)) for r in range(Pen_size)]) // Pen_size

            # 通道----颜料
            if abs(qcolor - wcolor) > Color_Diff:
                originalColor -= (255 - img.getpixel((i, j))) // 4
                new.putpixel((i, j), originalColor)

    new.save(img_all)

    # 打开转换后的图片
    os.system(img_all)

if __name__ == '__main__':
    imageName = "ha.png"
    transform(imageName)