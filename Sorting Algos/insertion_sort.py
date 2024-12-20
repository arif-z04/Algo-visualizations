import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def insertion_sort_visualization(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            yield data, j + 1, i
        data[j + 1] = key
        yield data, j + 1, i

def update(frame):
    global elapsed_time_text
    data, moving_index, current_index = frame
    for i, bar in enumerate(bar_container.patches):
        bar.set_height(data[i])
        if i == moving_index or i == current_index:
            bar.set_color("red")
        else:
            bar.set_color("blue")
    elapsed_time_text.set_text(f"Time Elapsed: {time.time() - start_time:.2f}s")

def generate_data(size, max_value):
    return [random.randint(1, max_value) for _ in range(size)]

def visualize_insertion_sort(size=50, max_value=100):
    global start_time, elapsed_time_text
    data = generate_data(size, max_value)

    fig, ax = plt.subplots()
    ax.set_title("Insertion Sort Visualization")

    global bar_container
    bar_container = ax.bar(range(len(data)), data, align="center", alpha=0.7, color="blue")
    ax.set_xlim(-1, size)
    ax.set_ylim(0, max_value + 10)

    elapsed_time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, color="green")

    start_time = time.time()
    ani = animation.FuncAnimation(
        fig, update, frames=insertion_sort_visualization(data), interval=100, repeat=False
    )

    def on_close(event):
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_text.set_text(f"Sorting Completed in {elapsed_time:.2f}s")

    fig.canvas.mpl_connect('close_event', on_close)
    plt.show()

if __name__ == "__main__":
    visualize_insertion_sort(size=30, max_value=100)
