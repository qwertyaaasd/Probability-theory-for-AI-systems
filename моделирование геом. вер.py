import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np

def circle_target(size):
    x0, y0, R = 7, 7, 5
    side = np.sqrt(3 * np.pi * R**2)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax = plt.gca()
    ax.add_patch(Rectangle((0, 0), side, side, facecolor='cyan'))
    ax.add_patch(Circle((x0, y0), R, facecolor='pink'))

    X = np.random.uniform(0, side, size)
    Y = np.random.uniform(0, side, size)
    plt.scatter(X, Y, marker='*', color='black')

    hit = len([d for d in (X - x0)**2 + (Y - y0)**2 if d <= R**2])
    p = hit/size

    plt.show()
    print(f'Из {size} точек попало {hit}')
    print(f'Вероятность попаданий {p}')

def rect_target(size):
    x0, y0 = 7, 7
    side1 = 5
    side2 = 2
    fig, ax = plt.subplots(figsize=(6, 6))
    ax = plt.gca()
    ax.add_patch(Rectangle((0, 0), side1, side1, facecolor='cyan'))
    ax.add_patch(Rectangle((1, 2), side2, side2, facecolor='pink'))

    X = np.random.uniform(0, side1, size)
    Y = np.random.uniform(0, side1, size)
    plt.scatter(X, Y, marker='*', color='black')

    cnt = 0
    for x, y in zip(X, Y):
        if 1 <= x <= 1+side2 and 2 <= y <= 2+side2:
            cnt += 1
        
    p = cnt/size

    plt.show()
    print(f'Из {size} точек попало {cnt}')
    print(f'Вероятность попаданий {p}')

circle_target(1000)
rect_target(1000)
