import cv2
import numpy as np
import matplotlib.pyplot as plt

from colors import get_n_colors
from bfs import bfs


def get_histogram(img_out, img_out_path):
    print("Salvando histograma...")
    histgram = np.array([len(np.where(img_out == i)[0])
                         for i in np.arange(1, img_out.max())])
    plt.bar(range(len(histgram)), histgram)
    plt.xlabel('Objeto')
    plt.ylabel('# de Pixels')
    plt.savefig(img_out_path + 'output_histogram.png')


def color_objects(img_out, count):
    # "+1" => incluindo o tom de cinza
    colors = get_n_colors(count+1)

    print("Colorindo objetos...")
    return colors[img_out.astype(int)]


def segmentation(img_in_path, img_out_path):
    count = 0
    img_in = cv2.imread(img_in_path, 0)
    hei, wid = img_in.shape[:2]
    img_out = np.zeros((hei, wid))

    print(img_in.max())
    print("Segmentando imagem...")
    for i in range(hei):
        for j in range(wid):
            if img_in[i, j] > 0 and img_out[i, j] == 0:
                count += 1
                img_out[i, j] = count
                bfs(img_in, img_out, i, j, count)

    get_histogram(img_out, img_out_path)
    cv2.imwrite(img_out_path + "output.png", color_objects(img_out, count))
    print(f"Saída salva em: {img_in_path}")


def main():
    segmentation('./input_imgs/numbers_binary.png', './input_imgs/')

if __name__ == "__main__":
    main()
