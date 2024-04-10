import tkinter as tk
from tkinter import ttk, font, simpledialog
import pyperclip
import random

def cipher(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr((ord(char)) + key)
    return cipher2(encrypted_text)

def cipher2(text):
    encrypted_text = ""
    for word in text.split():
        n = len(word)
        val = key(n)
        for char in word:
            encrypted_text += chr((ord(char)) + val)
    print(encrypted_text)
    return encrypted_text


def decrypt(text, user_key):
    text=decrypt2(text)
    decrypted_text = ""
    random_integer = random.randint(25, 100)
    keys = simpledialog.askinteger(f"Key", f"Enter your key: {random_integer}:")
    if (random_integer // 10) - 1 == keys:
        for char in text:
            decrypted_text += chr((ord(char)) - user_key)
    return decrypted_text

def decrypt2(text):
    encrypted_text = ""
    for word in text.split():
        n = len(word)
        val = key(n)
        for char in word:
            encrypted_text += chr((ord(char)) - val)
    return encrypted_text


def key(n):
    n = n * 2
    n += 2
    n *= 5
    n += 5
    return prime(n)

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(n):
    lower_prime = n - 1
    upper_prime = n + 1
    if not isprime(lower_prime):
        lower_prime = -1
    if not isprime(upper_prime):
        upper_prime += 1
    if abs(n - lower_prime) <= abs(n - upper_prime):
        return lower_prime
    else:
        return upper_prime

def on_encrypt_button_click():
    plain_text = plain_text_entry.get()
    if plain_text:
        key = int(encryption_key.get())
        cipher_text = cipher(plain_text, key)
        result_label.config(text=f'Cipher Text: {cipher_text}', font=large_font)
        plain_text_entry.delete(0, tk.END)
        encryption_key.delete(0,tk.END)
        encrypt_button.configure(bg='#28B463', fg='white', font=('Helvetica', 12, 'bold'))

def on_decrypt_button_click():
    cipher_text = cipher_text_entry.get()
    if cipher_text:
        secret_key = simpledialog.askinteger("Input", "Enter Secret Key")
        if secret_key is not None:
            try:
                secret_key = int(secret_key)
                plain_text = decrypt(cipher_text, secret_key)
                print(plain_text)
                result_label.config(text=f'Plain Text: {plain_text}', font=large_font)
                cipher_text_entry.delete(0, tk.END)
                decrypt_button.configure(bg='#3498DB', fg='white', font=('Helvetica', 12, 'bold'))
            except ValueError:
                result_label.config(text="Secret Key must be an integer.", font=large_font, fg="red")


def on_copy_button_click():
    cipher_text = result_label.cget("text").split(":")[1].strip()
    window.clipboard_clear()
    window.clipboard_append(cipher_text)
    window.update()

# Create the main window
window = tk.Tk()
window.title("Text Converter")

# Center the window on the screen
window_width = 800
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
window.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')

# Configure Styles
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12, 'bold'))

# Set color variables
bg_color = '#34495E'  # Dark Blue-Gray
fg_color = 'white'
button_bg_color = '#28B463'  # Dark Mint Green
button_hover_color = '#239B56'  # Light Mint Green

# Create and place widgets with enhanced styling
plain_text_label = tk.Label(window, text="Enter Plain Text:", font=('Helvetica', 14, 'bold'), bg=bg_color, fg=fg_color)
plain_text_label.pack(pady=10)

plain_text_entry = tk.Entry(window, width=80, font=('Helvetica', 12), bd=3)
plain_text_entry.pack(pady=5)

encryption_key_label = tk.Label(window, text="Secret Key:", font=('Helvetica', 14, 'bold'), bg=bg_color, fg=fg_color)
encryption_key_label.pack(pady=5)

encryption_key = tk.Entry(window, width=10, font=('Helvetica', 12), bd=3)
encryption_key.pack(pady=5)

encrypt_button = tk.Button(window, text="Encrypt", command=on_encrypt_button_click, bg=button_bg_color, fg=fg_color, font=('Helvetica', 12, 'bold'), bd=3)
encrypt_button.pack(pady=10)

cipher_text_label = tk.Label(window, text="Enter Cipher Text:", font=('Helvetica', 14, 'bold'), bg=bg_color, fg=fg_color)
cipher_text_label.pack(pady=10)

cipher_text_entry = tk.Entry(window, width=80, font=('Helvetica', 12), bd=3)
cipher_text_entry.pack(pady=5)

decrypt_button = tk.Button(window, text="Decrypt", command=on_decrypt_button_click, bg=button_bg_color, fg=fg_color, font=('Helvetica', 12, 'bold'), bd=3)
decrypt_button.pack(pady=10)

large_font = font.Font(family='Helvetica', size=14)
result_label = tk.Label(window, text="", width=50, font=large_font, bg=bg_color, fg=fg_color)
result_label.pack(pady=20)

copy_button = tk.Button(window, text="Copy Result", command=on_copy_button_click, font=('Helvetica', 12, 'bold'), bg=button_bg_color, fg=fg_color, bd=3)
copy_button.pack()

# Run the GUI
window.mainloop()
