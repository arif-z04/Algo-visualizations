import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to perform bubble sort and yield the data state at each step for visualization
def bubble_sort_visualization(data):
    """
    Generator function for bubble sort.
    Yields the current state of the data array and indexes being compared.

    Parameters:
        data (list): The list of numbers to be sorted.

    Yields:
        tuple: (data, moving_index, next_index)
        - data: The current state of the list.
        - moving_index: The index of the current element being swapped.
        - next_index: The index of the next element being compared.
    """
    n = len(data)
    # Iterate through the entire list
    for i in range(n):
        # Compare adjacent elements
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:  # Swap if the element is greater than the next
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data, j, j + 1  # Yield the current state of the list and indices

# Function to update the bar heights and colors during animation
def update(frame):
    """
    Updates the bar chart for each frame of the animation.

    Parameters:
        frame (tuple): A tuple containing the current state of data and indices.
        - data: The current state of the list.
        - moving_index: The index of the current element being swapped.
        - next_index: The index of the next element being compared.
    """
    data, moving_index, next_index = frame
    for i, bar in enumerate(bar_container.patches):
        bar.set_height(data[i])  # Update the height of each bar
        # Highlight the elements being swapped in red
        if i == moving_index or i == next_index:
            bar.set_color("red")
        else:
            bar.set_color("blue")
    # Update the elapsed time text
    elapsed_time_text.set_text(f"Time Elapsed: {time.time() - start_time:.2f}s")

# Function to generate a random dataset for sorting
def generate_data(size, max_value):
    """
    Generates a list of random integers.

    Parameters:
        size (int): The number of elements in the list.
        max_value (int): The maximum possible value of an element.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(1, max_value) for _ in range(size)]

# Function to visualize the bubble sort process
def visualize_bubble_sort(size=50, max_value=100):
    """
    Visualizes the bubble sort algorithm using a bar chart.

    Parameters:
        size (int): The number of elements to sort.
        max_value (int): The maximum possible value of an element.
    """
    global start_time, bar_container, elapsed_time_text

    # Generate random data for sorting
    data = generate_data(size, max_value)
    
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")

    # Create the bar chart
    bar_container = ax.bar(range(len(data)), data, align="center", alpha=0.7, color="blue")
    ax.set_xlim(-1, size)  # Set x-axis limits
    ax.set_ylim(0, max_value + 10)  # Set y-axis limits

    # Add a text box to display elapsed time
    elapsed_time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, verticalalignment='top')

    # Start tracking time
    start_time = time.time()

    # Create the animation
    ani = animation.FuncAnimation(
        fig, update, frames=bubble_sort_visualization(data), interval=100, repeat=False
    )

    # Display the plot
    plt.show()

# Main block to run the visualization
if __name__ == "__main__":
    visualize_bubble_sort(size=30, max_value=100)
