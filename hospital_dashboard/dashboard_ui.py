import tkinter as tk

def on_button_click():
    print("Button clicked")

# Create the main window
root = tk.Tk()
root.title("Sidebar Example")

# Define the header frame
header_frame = tk.Frame(root, bg="blue", height=50)
header_frame.pack(fill=tk.X)

# Add a label to the header frame
header_label = tk.Label(header_frame, text="Header", fg="white", bg="blue")
header_label.pack()

# Define the sidebar frame
sidebar_frame = tk.Frame(root, bg="gray", width=200)
sidebar_frame.pack(fill=tk.Y, side=tk.LEFT)

# Add components to the sidebar frame
button1 = tk.Button(sidebar_frame, text="Button 1", command=on_button_click)
button1.pack(pady=10)

button2 = tk.Button(sidebar_frame, text="Button 2", command=on_button_click)
button2.pack(pady=10)

# Define the content frame
content_frame = tk.Frame(root)
content_frame.pack(fill=tk.BOTH, expand=True)

# Add components to the content frame
content_label = tk.Label(content_frame, text="Content goes here...")
content_label.pack(padx=20, pady=20)

# Run the application
root.mainloop()
