from PIL import Image
import imagehash
hash = imagehash.average_hash(Image.open('img1.jpg'))
print(hash)
otherhash = imagehash.average_hash(Image.open('img2.jpg'))
print(otherhash)
print(hash == otherhash)
print(hash - otherhash)