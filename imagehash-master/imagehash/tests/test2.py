from PIL import Image
import imagehash
hash = imagehash.dhash(Image.open('img1.jpg'))
print(hash)
otherhash = imagehash.dhash(Image.open('img2.jpg'))
print(otherhash)
print(hash == otherhash)
print(hash - otherhash)