# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np
# import time

# # Initialize an empty array
# dynamic_array = []

# # Create a figure and axis
# fig, ax = plt.subplots()
# ax.set_title("Dynamic Array Plot")
# ax.set_xlabel("Time (seconds)")
# ax.set_ylabel("Value")

# # Initialize the plot with an empty line
# line, = ax.plot([], [], marker='o', color='b', label="Dynamic Array")

# # Set the x-axis limits
# ax.set_xlim(0, 10)  # Adjust as needed

# # Function to update the plot
# def update_plot(i):
#     global dynamic_array
#     value = np.random.randint(1, 10)  # Generate a random value
#     dynamic_array.append(value)  # Add the value to the array

#     # Update the plot data
#     line.set_data(range(len(dynamic_array)), dynamic_array)

#     # Adjust the x-axis limits dynamically
#     ax.set_xlim(0, len(dynamic_array) + 1)
#     ax.plot(dynamic_array, marker='o', color='b', label="Dynamic Array")

#     print(f"Updated dynamic_array: {dynamic_array}")  # Debugging print

# # Animate the plot
# ani = FuncAnimation(fig, update_plot, frames=10, repeat=False)

# # Show the legend
# ax.legend()

# print("Before plt.show()")  # Debugging print
# plt.show()
# print("After plt.show()")  # Debugging print

# import random
# import matplotlib.pyplot as plt

# def update_plot(x_vals, y_vals):
#     plt.cla()  # Clear the current plot
#     plt.plot(x_vals, y_vals)

# if __name__ == "__main__":
#     x_vals = []
#     y_vals = []
#     fig, ax = plt.subplots()

#     for i in range(10):
#         x_vals.append(i)
#         y_vals.append(random.randint(0, 10))
#         update_plot(x_vals, y_vals)
#         plt.pause(0.5)  # Pause to see the plot update

    # plt.show()
