import os
import cv2
import time
import shutil

def getAllPath(dirpath, *suffix):
    PathArray = []
    for r, ds, fs in os.walk(dirpath):
        for fn in fs:
            if os.path.splitext(fn)[1] in suffix:
                fname = os.path.join(r, fn)
                fname = fname.replace("\\","/")
            
                PathArray.append(fname)
    return PathArray

#从源路径中读取所有图片放入一个list，然后逐一进行检查，把其中的脸扣下来，存储到目标路径中
def readPicSaveFace(sourcePath,targetPath,invalidPath,*suffix):
    try:
        ImagePaths=getAllPath(sourcePath, *suffix)
 
        #对list中图片逐一进行检查,找出其中的人脸然后写到目标文件夹下
        count = 1
        # haarcascade_frontalface_alt.xml为库训练好的分类器文件，下载opencv，安装目录中可找到
        face_cascade = cv2.CascadeClassifier('D:/program/python36/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
        print(type(face_cascade))
        print(face_cascade)

        for imagePath in ImagePaths:
            img = cv2.imread(imagePath)
            if type(img) != str:
                faces = face_cascade.detectMultiScale(
                    img, 
                    scaleFactor = 1.15,
                    minNeighbors = 5,
                    minSize = (5,5),
                    flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
                if len(faces):
                    for (x, y, w, h) in faces:
                        # 设置人脸宽度大于128像素，去除较小的人脸
                        if w>=128 and h>=128:
                            # 以时间戳和读取的排序作为文件名称
                            listStr = [str(int(time.time())), str(count)]
                            fileName = ''.join(listStr)
                            # 扩大图片，可根据坐标调整
                            X = int(x*0.5)
                            W = min(int((x + w)*1.2),img.shape[1])
                            Y = int(y*0.3)
                            H = min(int((y + h)*1.4),img.shape[0])
 
                            f = cv2.resize(img[Y:H, X:W], (W-X,H-Y))
                            cv2.imwrite(targetPath+os.sep+'%s.jpg' % fileName, f)
                            count += 1
                else:
                    shutil.move(imagePath, invalidPath)
    except IOError:
        print("Error")
 
    else:
        print('Find '+str(count-1)+' faces to Destination '+targetPath)
 
if __name__ == '__main__':
    invalidPath = 'd:/upload/'
    sourcePath = 'd:/upload/'
    targetPath = 'd:/upload/'
    readPicSaveFace(sourcePath,targetPath,invalidPath,'.jpg','.JPG','png','PNG')

    # img = cv2.imread("D:/upload/3.jpg")
    # # "D:\Test\2.jpg"
    # #创建窗口并显示图像
    # cv2.namedWindow("Image")
    # cv2.imshow("Image",img)
    # cv2.waitKey(0)
    # #释放窗口
    # cv2.destroyAllWindows()
