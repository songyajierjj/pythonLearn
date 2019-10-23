# -*- coding:utf-8 -*-
import os
import math
import imagehash
from PIL import Image


def imagehash_retrieval(img_path, retrieval_path, hash_mode='dhash', thred=0):#默认是dhash
    hash_encoder = None
    cnt = 0
    if hash_mode == 'phash':
        hash_encoder = imagehash.phash
    elif hash_mode == 'ahash':
        hash_encoder = imagehash.average_hash
    elif hash_mode == 'whash':
        hash_encoder = imagehash.whash
    elif hash_mode == 'dhash':
        hash_encoder = imagehash.dhash
    else:
        assert False, "UNKNOW MODE"
    img_path = img_path.get()
    retrieval_path = retrieval_path.get()
    img = Image.open(img_path)
    img_hash = hash_encoder(img)

    target_img_files, all_files = [], os.listdir(retrieval_path)
    for i, file in enumerate(all_files):
        if file.endswith("png") or file.endswith("jpg"):
            target_img_files.append(os.path.join(retrieval_path, file))

    hash_res = []
    for file in target_img_files:
        obj_hash = hash_encoder(Image.open(file))
        diff = math.fabs(img_hash - obj_hash)/len(img_hash.hash)**2
        cnt += 1
        # x.set( len+'个文件中，处理了'+str(count1)+'张')
        # root1.update()#显示处理过程
        hash_res.append((file, diff))

    hash_res = sorted(hash_res, key=lambda x: x[1])
    hash_res = [i for i in hash_res if i[1] > thred]

    return hash_res


if __name__ == "__main__":
    hash_res = imagehash_retrieval(
        r"./img/background_1.jpg",
        r"./img",
        "ahash")
    print(hash_res)

    hash_res = imagehash_retrieval(
        r"./img/background_1.jpg",
        r"./img",
        "whash")
    print(hash_res)

    hash_res = imagehash_retrieval(
        r"./img/background_1.jpg",
        r"./img",
        "phash")
    print(hash_res)

    hash_res = imagehash_retrieval(
        r"./img/background_1.jpg",
        r"./img",
        "dhash")
    print(hash_res)


