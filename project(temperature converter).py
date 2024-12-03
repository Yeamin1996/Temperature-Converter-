import tkinter as tk
from tkinter import ttk

# Function to perform the conversion
def convert_temperature():
    try:
        input_temp = float(entry_temperature.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # Conversion logic
        if from_unit == to_unit:
            result = input_temp
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (input_temp * 9/5) + 32
            elif to_unit == "Kelvin":
                result = input_temp + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (input_temp - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (input_temp - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = input_temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (input_temp - 273.15) * 9/5 + 32

        # Display the result
        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        label_result.config(text="Invalid input! Please enter a number.")

# Main GUI window
root = tk.Tk()
root.title("Temperature Converter")

# Input temperature
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, columnspan=2, sticky="EW")

label_input = ttk.Label(frame_input, text="Enter Temperature:")
label_input.pack(side="left")
entry_temperature = ttk.Entry(frame_input, width=10)
entry_temperature.pack(side="left")

# From and To unit dropdowns
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=12)
combo_from.set("Celsius")
combo_from.grid(row=1, column=0, padx=5, pady=5)

combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=12)
combo_to.set("Fahrenheit")
combo_to.grid(row=1, column=1, padx=5, pady=5)

# Convert button
button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
label_result = ttk.Label(root, text="Result: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
