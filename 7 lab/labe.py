from PIL import Image
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
    names = ['1.jpg','2.jpg','3.png','4.jpg','5.png']
    img_gray_smooth = img.filter(ImageFilter.SMOOTH)
    edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    edges_smooth.save(names[k])
def task3():
    img = Image.open()
    task3_1(img,1)
    img = Image.open()
    task3_1(img,2)
    img = Image.open()
    img = Image.open()
    task3_1(img,4)
    img = Image.open()

task3()
