image_sif = input()
layer_size = 25*6
min_zeros = float("inf")
result = 0
for i in range(0, len(image_sif), layer_size):
    layer = image_sif[i:i+layer_size]
    count = layer.count('0')
    if count < min_zeros:
        min_zeros = count
        result = layer.count('1') * layer.count('2')
print(result)

