import serial
import matplotlib.pyplot as plt
import time

# Open the serial port (adjust COM port and baud rate as needed)
ser = serial.Serial('COM4', 9600, timeout=1)  # Replace 'COM9' with your Arduino port
time.sleep(2)  # Allow time for the serial connection to initialize

# Lists to store the data for each analog input
data1 = []
data2 = []
data3 = []
time_data = []  # Store time points for the x-axis

# Collect data for 100 seconds
start_time = time.time()
duration = 100  # seconds

print("Collecting data for 100 seconds...")

try:
    while True:
        # Get the current time to check the duration
        current_time = time.time() - start_time
        
        # Stop the loop after 100 seconds
        if current_time >= duration:
            break
        
        # Read a line of data from the serial port and decode it
        line = ser.readline().decode('utf-8').strip()
        
        # Parse the tab-separated values
        if line:
            values = line.split('\t')  # Using tab as the separator based on your Arduino code

            if len(values) == 3:  # Ensure there are exactly 3 values
                try:
                    # Append the values to the respective data lists
                    data1.append(int(values[0]))
                    data2.append(int(values[1]))
                    data3.append(int(values[2]))
                    time_data.append(current_time)
                except ValueError:
                    # Handle cases where data might not be correctly formatted
                    print(f"Invalid data: {values}")
except KeyboardInterrupt:
    print("Data collection interrupted.")
finally:
    ser.close()

# Check if data was collected
if len(time_data) == 0:
    print("No data was collected.")
    exit()

# Plot the data after 60 seconds
print("Plotting the data...")

# Create three separate figures
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

# Plot each dataset in its respective figure
ax1.plot(time_data, data1, label='A0')
ax2.plot(time_data, data2, label='A1')
ax3.plot(time_data, data3, label='A3')

# Set titles and labels for each plot
ax1.set_title("Analog Input A0")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Value")

ax2.set_title("Analog Input A1")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Value")

ax3.set_title("Analog Input A3")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Value")

# Ensure the plots update and show properly
plt.show()

print("Data collection and plotting complete.")
