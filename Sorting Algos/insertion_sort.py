import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to perform insertion sort and yield the data state at each step for visualization
def insertion_sort_visualization(data):
    """
    Generator function for insertion sort.
    Yields the current state of the data array and indexes being compared/modified.

    Parameters:
        data (list): The list of numbers to be sorted.

    Yields:
        tuple: (data, moving_index, current_index)
        - data: The current state of the list.
        - moving_index: The index of the element being moved.
        - current_index: The index of the current element being compared.
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        # Shift elements of the sorted segment that are greater than key to the right
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            yield data, j + 1, i
        # Place the key in its correct position
        data[j + 1] = key
        yield data, j + 1, i

# Function to update the bar heights and colors during animation
def update(frame):
    """
    Updates the bar chart for each frame of the animation.

    Parameters:
        frame (tuple): A tuple containing the current state of data and indices.
        - data: The current state of the list.
        - moving_index: The index of the element being moved.
        - current_index: The index of the current element being compared.
    """
    global elapsed_time_text
    data, moving_index, current_index = frame
    for i, bar in enumerate(bar_container.patches):
        bar.set_height(data[i])  # Update bar height
        # Highlight the moving and current elements in red
        if i == moving_index or i == current_index:
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

# Function to visualize the insertion sort process
def visualize(size=50, max_value=100):
    """
    Visualizes the insertion sort algorithm using a bar chart.

    Parameters:
        size (int): The number of elements to sort.
        max_value (int): The maximum possible value of an element.
    """
    global start_time, elapsed_time_text

    # Generate random data for sorting
    data = generate_data(size, max_value)

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_title("Insertion Sort Visualization")

    # Create the bar chart
    global bar_container
    bar_container = ax.bar(range(len(data)), data, align="center", alpha=0.7, color="blue")
    ax.set_xlim(-1, size)  # Set x-axis limits
    ax.set_ylim(0, max_value + 10)  # Set y-axis limits

    # Add a text box to display elapsed time
    elapsed_time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, color="green")

    # Start tracking time
    start_time = time.time()

    # Create the animation
    ani = animation.FuncAnimation(
        fig, update, frames=insertion_sort_visualization(data), interval=100, repeat=False
    )

    # Handle plot window close event
    def on_close(event):
        """
        Callback function to execute when the plot window is closed.
        Displays the total elapsed time.
        """
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_text.set_text(f"Sorting Completed in {elapsed_time:.2f}s")

    fig.canvas.mpl_connect('close_event', on_close)

    # Display the plot
    plt.show()

# Main block to run the visualization
if __name__ == "__main__":
    visualize(size=30, max_value=100)
