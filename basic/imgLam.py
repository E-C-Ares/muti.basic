from.__deps_ import*


def showImg(x):
    if x.shape[-1]>4:
        x=x.transpose(1,2,0)
    import PIL.Image as Image
    Image.fromarray(x).show()