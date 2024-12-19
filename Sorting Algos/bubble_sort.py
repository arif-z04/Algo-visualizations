import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort_visualization(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data, j, j + 1

def update(frame):
    data, moving_index, next_index = frame
    for i, bar in enumerate(bar_container.patches):
        bar.set_height(data[i])
        if i == moving_index or i == next_index:
            bar.set_color("red")
        else:
            bar.set_color("blue")

def generate_data(size, max_value):
    return [random.randint(1, max_value) for _ in range(size)]

def visualize_bubble_sort(size=50, max_value=100):
    data = generate_data(size, max_value)
    
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    
    global bar_container
    bar_container = ax.bar(range(len(data)), data, align="center", alpha=0.7, color="blue")
    ax.set_xlim(-1, size)
    ax.set_ylim(0, max_value + 10)
    
    ani = animation.FuncAnimation(
        fig, update, frames=bubble_sort_visualization(data), interval=100, repeat=False
    )
    plt.show()

if __name__ == "__main__":
    visualize_bubble_sort(size=30, max_value=100)
