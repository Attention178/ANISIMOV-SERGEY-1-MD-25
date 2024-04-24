from PIL import Image, ImageDraw, ImageFont
def task1():
    img = Image.open(r'D:\UserFolders\Downloads\grass.jpg')
    img.show()
    print(img.format)
    print(img.size)
    print(img.mode)

def task2():
    img = Image.open(r'D:\UserFolders\Downloads\grass.jpg')
    resize_img = img.resize(
        (img.width // 3, img.height // 3)
    )
    converted_vertical_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_horizontal_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    resize_img.save("1.jpg")
    converted_vertical_img.save("2.jpg")
    converted_horizontal_img.save("3.jpg")


def task3_1(img,k):
    from PIL import ImageFilter
    names = ['grass.jpg','planeta.jpg','luna.jpg','cosmos.jpg']
    img_gray_smooth = img.filter(ImageFilter.SMOOTH)
    edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    edges_smooth.save(names[k])
def task3():
    img = Image.open(r'D:\UserFolders\Downloads\grass.jpg')
    task3_1(img,0)
    img = Image.open(r'D:\UserFolders\Downloads\luna.jpg')
    task3_1(img,1)
    img = Image.open(r'D:\UserFolders\Downloads\planeta.jpg')
    task3_1(img,2)
    img = Image.open(r'D:\UserFolders\Downloads\cosmos.jpg')
    task3_1(img,3)


def task4():
    image = Image.open("grass.jpg")

    font = ImageFont.truetype("arial.ttf", 55)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, 100), "УРА УРА УРА УРА УРА УРА УРА УУУУУУУУУУУУУУУ!", font=font, fill='white')

    image.save('new_img.jpg')
    image.show()
task4()



