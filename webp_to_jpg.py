import os
import cv2


def webp_to_jpg(webp_path, jpg_path):
    for (dirpath, dirnames, filenames) in os.walk(webp_path):
        for filename in filenames:
            if filename.endswith('.webp'):
                jpg_filename = filename[:(len(filename)-5)] + '.jpg'
                print(filename + " => " + jpg_filename)
                image = cv2.imread(webp_path + filename)
                cv2.imwrite(jpg_path + jpg_filename, image)


webp_to_jpg("~/webp/", "~/jpg/")
