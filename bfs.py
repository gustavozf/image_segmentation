def get_neighbors(i, j, MAX_HEI, MAX_WID):
    neighbors = [(i, j+1),
                 (i, j-1),
                 (i+1, j),
                 (i-1, j)]

    return [z for z in neighbors
            if not False in [z[0] >= 0,
                             z[0] < MAX_HEI,
                             z[1] >= 0,
                             z[1] < MAX_WID]]


def bfs(img_in, img_out, i, j, gray_value):
    pixels = [(i, j)]
    hei, wid = img_in.shape[:2]

    while(len(pixels) > 0):
        # picks a new pixel
        new_pixel = pixels.pop()
        # for all his neighbors
        #print(f"({new_pixel}) : {get_neighbors(new_pixel[0], new_pixel[1])}")
        for neighbor in get_neighbors(new_pixel[0], new_pixel[1], hei, wid):
            # if we're looking to a white pixel
            # and the pixel in the output has not been seen yet
            if img_in[neighbor] > 0 and img_out[neighbor] == 0:
                # mark the output pixel as "seen"
                img_out[neighbor] = gray_value
                # append it to the list
                pixels.append(neighbor)
