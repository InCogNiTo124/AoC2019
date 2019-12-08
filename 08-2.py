image_sif = input()
W = 25
H = 6
#image = [['2' for _ in range(W)] for _ in range(H)]
image = None
for cursor in range(0, len(image_sif), W*H):
    layer = []
    for j in range(H):
        layer.append(list(image_sif[cursor+j*W:cursor+(j+1)*W]))
    if cursor == 0:
        image = layer.copy()
    else:
        #has_transparent = False
        for i, row in enumerate(image):
            for j, pixel in enumerate(row):
                if pixel == '2' and layer[i][j] != '2':
                    has_transparent = True
                    image[i][j] = layer[i][j]
        #if not has_transparent:
        #    break
    #print(image)
print('\n'.join(''.join(row) for row in image))
