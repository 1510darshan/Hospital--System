import tkinter as tk
import customtkinter as ctk
from PIL import Image

def dashboard_frame():
    # Clear current content and display dashboard frame
    clear_frame()
    dash_frame = ctk.CTkFrame(container, corner_radius=0, fg_color="white")
    dash_frame.pack(fill=tk.BOTH, expand=True)

    # define label frame
    dash_label_frame = ctk.CTkFrame(dash_frame, height=40, corner_radius=0, fg_color="white")
    dash_label_frame.pack(side=tk.TOP, fill=tk.X)

    # define frame
    dash_label = ctk.CTkLabel(dash_label_frame, text="Dashboard",text_color="black", font=("Ubuntu", 27))
    dash_label.pack(pady=5)

    




def department_frame():
    # Clear current content and display department frame
    clear_frame()
    main_frame = ctk.CTkFrame(container, height=screen_height, width=screen_width, corner_radius=0, fg_color="orange")
    main_frame.pack()
    dep_label = ctk.CTkLabel(main_frame, text="Department", height=60,text_color="white", 
                            font=("Ubuntu", 35, "bold"))
    dep_label.pack(side=tk.LEFT,padx=50)

def doctor_frame():
    # Clear current content and display doctor frame
    clear_frame()
    main_frame = ctk.CTkFrame(container, height=screen_height, width=screen_width, corner_radius=0, fg_color="blue")
    main_frame.pack()




def patient_frame():
    # Clear current content and display patient frame
    clear_frame()
    main_frame = ctk.CTkFrame(container, height=screen_height, width=screen_width, corner_radius=0)
    main_frame.pack()

    # define label in frame
    label = ctk.CTkLabel(patient_frame, text="Primary Health Care Centre", height=60,text_color="white", 
                                font=("Ubuntu", 35, "bold"))
    label.pack(side=tk.LEFT,padx=50)



def medicine_frame():
    # Clear current content and display medicine frame
    clear_frame()
    main_frame = ctk.CTkFrame(container, height=screen_height, width=screen_width, corner_radius=0, fg_color="yellow")
    main_frame.pack()

def disease_frame():
    # Clear current content and display medicine frame
    clear_frame()
    main_frame = ctk.CTkFrame(container, height=screen_height, width=screen_width, corner_radius=0, fg_color="purple")
    main_frame.pack()

def clear_frame():
    # Clear current content of the container frame
    for widget in container.winfo_children():
        widget.destroy()

# Create the main window
root = tk.Tk()
root.title("CustomTkinter Example")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window geometry to cover the entire screen
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Define the sidebar frame
sidebar_frame = ctk.CTkFrame(root, fg_color="#347B98", width=150, corner_radius=0)
sidebar_frame.pack(fill=tk.Y, side=tk.LEFT)

# Define the logo frame in sidebar frame
profile_frame = ctk.CTkFrame(sidebar_frame, height=40, width=150, fg_color="black", corner_radius=0, border_width=2)
profile_frame.pack()

# Specify the correct image path
image_path = "hospital_dashboard/resources/logo.webp"

# Open the image using PIL
pil_image = Image.open(image_path)

# Create a custom label with the image
logo = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(180, 60))

# Create a label to display the image
image_label = ctk.CTkLabel(profile_frame, image=logo, text="", fg_color="white")
image_label.pack()

# set color of sidebar button
normal_color = "#0a5f68"

# set width and height of sidebar button
btn_height = 50
btn_width = 180
border_width = 1
divider_color = "grey"
hover_color="black"


# Load the icon images
dash_path = "hospital_dashboard/resources/dashboard_icon.png"  # Change this to the path of your icon file
dashboard_icon = Image.open(dash_path)
# Create a custom label with the image
dashboard_icon = ctk.CTkImage(light_image=dashboard_icon, dark_image=dashboard_icon, size=(27, 27))

# Load the icon images
depnt_path = "hospital_dashboard/resources/department_icon.png"  # Change this to the path of your icon file
depnt_icon = Image.open(depnt_path)
# Create a custom label with the image
department_icon = ctk.CTkImage(light_image=depnt_icon, dark_image=depnt_icon, size=(30, 30))

# Load the icon images
doctor_path = "hospital_dashboard/resources/doctor_icon.png"  # Change this to the path of your icon file
doctor_icon = Image.open(doctor_path)
# Create a custom label with the image
doctor_icon = ctk.CTkImage(light_image=doctor_icon, dark_image=doctor_icon, size=(30, 30))

# Load the icon images
petient_path = "hospital_dashboard/resources/patient_icon.png"  # Change this to the path of your icon file
petient_icon = Image.open(petient_path)
# Create a custom label with the image
petient_icon = ctk.CTkImage(light_image=petient_icon, dark_image=petient_icon, size=(35, 35))

# Load the icon images
med_path = "hospital_dashboard/resources/medicine_icon.png"  # Change this to the path of your icon file
med_icon = Image.open(med_path)
# Create a custom label with the image
medicine_icon = ctk.CTkImage(light_image=med_icon, dark_image=med_icon, size=(25, 25))

# Load the icon images
disease_path = "hospital_dashboard/resources/disease.png"  # Change this to the path of your icon file
disease_icon = Image.open(disease_path)
# Create a custom label with the image
disease_icon = ctk.CTkImage(light_image=disease_icon, dark_image=disease_icon, size=(25, 25))

# define department button
dashboard_button = ctk.CTkButton(sidebar_frame, image=dashboard_icon, width=btn_width, height=btn_height, text="Dashboard", fg_color=normal_color, 
                corner_radius=0, font=("sana serif", 16), command=dashboard_frame, hover_color=hover_color, anchor=tk.W)
dashboard_button.pack()

# Create a frame as a divider
divider = ctk.CTkFrame(sidebar_frame, height=1,width=btn_width, fg_color=divider_color)
divider.pack(fill=tk.X)

# define department button
department_button = ctk.CTkButton(sidebar_frame, image=department_icon, width=btn_width, height=btn_height, text="Department", fg_color=normal_color, 
                corner_radius=0, font=("sana serif", 16), command=department_frame, hover_color=hover_color,  anchor=tk.W)
department_button.pack()

# Create a frame as a divider
divider = ctk.CTkFrame(sidebar_frame, height=1,width=btn_width, fg_color=divider_color)
divider.pack(fill=tk.X)

# define doctor button
doctor_button = ctk.CTkButton(sidebar_frame, image=doctor_icon, width=btn_width, height=btn_height, text="Doctor", fg_color=normal_color,
                corner_radius=0, font=("sana serif", 16), command=doctor_frame, hover_color=hover_color, anchor=tk.W)
doctor_button.pack()

# Create a frame as a divider
divider = ctk.CTkFrame(sidebar_frame, height=1,width=btn_width, fg_color=divider_color)
divider.pack(fill=tk.X)


# define petient button
patient_button = ctk.CTkButton(sidebar_frame, image=petient_icon, width=btn_width, height=btn_height, text="Patient", fg_color=normal_color, 
                 corner_radius=0, font=("sana serif", 16), command=patient_frame, hover_color=hover_color, anchor=tk.W)
patient_button.pack()

# Create a frame as a divider
divider = ctk.CTkFrame(sidebar_frame, height=1,width=btn_width, fg_color=divider_color)
divider.pack(fill=tk.X)

# define medicine button
medicine_button = ctk.CTkButton(sidebar_frame, image=medicine_icon, width=btn_width, height=btn_height, text="Medicine Stock", fg_color=normal_color, 
                corner_radius=0, font=("sana serif", 16), command=medicine_frame, hover_color=hover_color, anchor=tk.W)
medicine_button.pack()

# Create a frame as a divider
divider = ctk.CTkFrame(sidebar_frame, height=1,width=btn_width, fg_color=divider_color)
divider.pack(fill=tk.X)

# define medicine button
disease_button = ctk.CTkButton(sidebar_frame, image=disease_icon, width=btn_width, height=btn_height, text="Disease", fg_color=normal_color, 
                corner_radius=0, font=("sana serif", 16), command=disease_frame, hover_color=hover_color, anchor=tk.W)
disease_button.pack()

# Define the header frame
header_frame = ctk.CTkFrame(root, width=200, height=60, corner_radius=0, fg_color="#347B98")
header_frame.pack(fill=tk.X)

# define label in frame
header_label = ctk.CTkLabel(header_frame, text="Primary Health Care Centre", height=60,text_color="white", 
                            font=("Ubuntu", 35, "bold"))
header_label.pack(side=tk.LEFT,padx=50)

# Create a container frame for dynamic content
container = ctk.CTkFrame(root, fg_color="white", width=screen_width, height=screen_height)
container.pack(fill=tk.BOTH, expand=True)

# Set the dashboard frame as the default frame
dashboard_frame()

# Run the application
root.mainloop()
