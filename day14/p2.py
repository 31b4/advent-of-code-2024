import numpy as np
from PIL import Image
import os

def parse(line):
    p, v = line.split()
    return [int(x) for x in p[2:].split(',') + v[2:].split(',')]

os.makedirs('img', exist_ok=True)

robots = [parse(line) for line in open('i.txt')]
W, H = 101, 103

for t in range(10000):
    img = np.zeros((H, W), dtype=np.uint8)
    for x,y,_,_ in robots:
        img[y][x] = 255
    
    Image.fromarray(img).save(f'img/frame_{t:04d}.png')
    
    robots = [[((x + vx) % W), ((y + vy) % H), vx, vy] for x,y,vx,vy in robots]