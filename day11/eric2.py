import numpy as np
from skimage import io, transform

FLOOR = 255
EMPTY = 75
OCCUPIED = 0


def in_bound(x, y, shape):
    return 0 <= x < shape[0] and 0 <= y < shape[1]


def vision(img, x, y):
    directions = [[-1, -1], [-1, 0], [-1, 1],
                  [0, -1],           [0, 1],
                  [1, -1],  [1, 0],  [1, 1]]
    seen = {EMPTY: 0, OCCUPIED: 0}
    for d in directions:
        i = 1
        newX = x + i * d[0]
        newY = y + i * d[1]
        while in_bound(newX, newY, img.shape):
            if img[newX, newY] in (EMPTY, OCCUPIED):
                seen[img[newX, newY]] += 1
                break
            i += 1
            newX = x + i * d[0]
            newY = y + i * d[1]
    return seen


def next_step(src_img):
    img = np.copy(src_img)
    h, w = img.shape
    mask_occupied = src_img == OCCUPIED
    # check new OCCUPIED
    idx = np.where(src_img == EMPTY)
    for i in range(len(idx[0])):
        if vision(src_img, idx[0][i], idx[1][i])[OCCUPIED] == 0:
            img[idx[0][i], idx[1][i]] = OCCUPIED

    # check new EMPTY
    idx = np.nonzero(mask_occupied)

    for i in range(len(idx[0])):
        if vision(src_img, idx[0][i], idx[1][i])[OCCUPIED] >= 5:
            img[idx[0][i], idx[1][i]] = EMPTY
    return img


def load_data():
    viz = {'.': FLOOR, 'L': EMPTY, '#': OCCUPIED}
    with open("input.txt", "r") as f:
        matrix = [[c for c in line.strip("\n")] for line in f.readlines()]

    img = np.array(([[viz[e] for e in line]for line in matrix]), dtype=np.uint8)

    return img


if __name__ == "__main__":
    img = load_data()
    imgs = [img]
    # io.imshow(imgs[-1])
    # io.show()
    imgs.append(next_step(imgs[-1]))
    # io.imshow(imgs[-1])
    # io.show()
    while np.count_nonzero(imgs[-2] == imgs[-1]) != img.shape[0]*img.shape[1]:
        imgs.append(next_step(imgs[-1]))
        # io.imshow(imgs[-2] == imgs[-1]); io.show();
        # io.imshow(imgs[-1]) ;io.show()

    binary = imgs[-1] == OCCUPIED
    print(np.count_nonzero(binary))




    frames = []

    for i in range(len(imgs)):
        io.imsave("gif2/"+str(i)+".png", transform.rescale(imgs[i], 4))
