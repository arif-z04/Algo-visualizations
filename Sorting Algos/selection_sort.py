import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def selection_sort_visualization(data):
    """
    Generator function for bubble sort.
    Yields the current state of the data array and indexes being compared.
    
    Parameters:
        data (list): The list of numbers to be sorted.

    Yields:
        tuple: (data, moving_index, current_index)
        - data: The current state of the list.
        - moving_index: The index of the element being moved.
        - current_index: The index of the current element being compared.
    """
    n = len(data)
    for i in range(n):
        min_index = i
        # Fidn the minimum element in the unsorted portion

        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
            yield data, min_index, j

        data[i], data[min_index] = data[min_index], data[i]
        yield data, min_index, i

def update(frame):
   
    """
    Updates the bar chart for each frame of the animation

    Parameters: 
        frame (tuple): A tuple containing the current state of data and indices.
        - data: The current state of the list.
        - min_index: The index of the smallest element in the current pass.
        - current_index: The index of the element being compared.
    """
    data, min_index, current_index = frame
    for i, bar in enumerate(bar_container.patches):
        bar.set_height(data[i])

        #Highlight the smallest element in green and the current element in red
        if i == min_index:
            bar.set_color("green")
        elif i == current_index:
            bar.set_color("red")
        else:
            bar.set_color("blue")

        elapsed_time_text.set_text(f"Time Elapsed: {time.time() - start_time:.2f}s")
def generate_data(size, max_value):
    """
    Generates a list of random integers.

    Parameters: 
        size (int): The number of elements in the list.
        max_value (int): The maximum possible value of an element. 
    """
    return [random.randint(1, max_value) for _ in range(size)]

def visualize_selection_sort(size=50, max_value=100):
    """
    Visualize the selection sort algorithm using a bar chart.

    Parameters:
        size (int): The number of elements to sort.
        max_value (int): The maximum possible value of an element.
    """

    global start_time, bar_container, elapsed_time_text
    
    # Generate random data for sorting
    data = generate_data(size, max_value)
    
    # Set up the plot

    fig, ax = plt.subplots()
    ax.set_title("Selection Sort Visualization")

    # Create the bar chart
    bar_container = ax.bar(range(len(data)), data, align="center", alpha=0.7, color="blue")
    ax.set_xlim(-1, size)
    ax.set_ylim(0, max_value + 10)

    # Add a text box to display elapsed time 
    elapsed_time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, verticalalignment='top')

    # Start tracking time 
    start_time = time.time()

    # Create the animation 
    ani = animation.FuncAnimation(
        fig, update, frames=selection_sort_visualization(data), interval=100, repeat=False, cache_frame_data=False
    )

    plt.show()

if __name__ == "__main__":
    visualize_selection_sort(size=30, max_value=100)