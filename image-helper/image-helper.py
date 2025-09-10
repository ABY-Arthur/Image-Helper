from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

def resize_image(img, width, height):
    return img.resize((width, height), resample=Image.LANCZOS)

def crop_image(img, left, upper, right, lower):
    return img.crop((left, upper, right, lower))

def new_image(width, height, color):
    return Image.new("RGB", (width, height), color)

def main():
    root = tk.Tk()
    root.withdraw()

    print("Welcome to the Image helper programme ya lm3gaz ")
    print("1. Resize an image")
    print("2. Crop an image")
    print("3. Create a new image")
    choice = input("Enter your choice (1/2/3): ")

    if choice in ['1', '2']:
        print("Select the image file:")
        img_path = filedialog.askopenfilename(title="Select an image")
        if not img_path:
            print("No file selected, exiting...")
            return
        img = Image.open(img_path)

    print("Select where to save the image (choose folder and filename):")
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if not save_path:
        print("No save path selected, exiting...")
        return
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    if choice == '1':
        input_width = int(input("Enter new width: "))
        input_height = int(input("Enter new height: "))
        result_img = resize_image(img, input_width, input_height)
        result_img.save(save_path)

    elif choice == '2':
        left = int(input("Enter the left coordinate: "))
        upper = int(input("Enter the upper coordinate: "))
        right = int(input("Enter the right coordinate: "))
        lower = int(input("Enter the lower coordinate: "))
        result_img = crop_image(img, left, upper, right, lower)
        result_img.save(save_path)
    
    elif choice == '3':
        width = int(input("Enter the width of the new image: "))
        height = int(input("Enter the height of the new image: "))
        color = input("Enter the background color (e.g., 'red', '#00FF00'): ")
        result_img = new_image(width, height, color)
        result_img.save(save_path)
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    print(f"Operation completed! Image saved at {save_path}")

if __name__ == "__main__":
    main()
