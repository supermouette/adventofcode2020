import numpy as np
from skimage import io, transform

FLOOR = 255
EMPTY = 75
OCCUPIED = 0


def next_step(src_img):
    img = np.copy(src_img)
    h, w = img.shape
    mask_occupied = src_img == OCCUPIED
    # check new OCCUPIED
    idx = np.where(src_img == EMPTY)
    for i in range(len(idx[0])):
        if len(np.nonzero(mask_occupied[max(0, idx[0][i]-1):min(h, idx[0][i]+2),
                                        max(0, idx[1][i]-1):min(w, idx[1][i]+2)])[0]) == 0:
            img[idx[0][i], idx[1][i]] = OCCUPIED

    # check new EMPTY
    idx = np.nonzero(mask_occupied)

    for i in range(len(idx[0])):
        if np.count_nonzero(mask_occupied[max(0, idx[0][i]-1):min(h, idx[0][i]+2),
                                          max(0, idx[1][i]-1):min(w, idx[1][i]+2)]) >= 5:
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
    imgs.append(next_step(imgs[-1]))
    while np.count_nonzero(imgs[-2] == imgs[-1]) != img.shape[0]*img.shape[1]:
        imgs.append(next_step(imgs[-1]))
        # io.imshow(imgs[-2] == imgs[-1]); io.show();
        # io.imshow(imgs[-1]) ;io.show()

    binary = imgs[-1] == OCCUPIED
    print(np.count_nonzero(binary))




    frames = []

    for i in range(len(imgs)):
        io.imsave("gif/"+str(i)+".png", transform.rescale(imgs[i], 4))
