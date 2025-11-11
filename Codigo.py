import qrcode
from tkinter import messagebox
from tkinter import *
import ttkbootstrap as tb

def genQR(datos, nombre_archivo="QrGenerator.png"):
    try:
        img = qrcode.make(datos)
        img.save(nombre_archivo)
        messagebox.showinfo("QR", f"QR generado en {nombre_archivo}")
        imgQR.configure(image=PhotoImage(file=nombre_archivo))
    except Exception as e:
        print(f"Error al generar QR: {e}")

app = Tk()
app.title("QR-Generator")

style = tb.Style()
style.configure("Custom.TLabel", font=("Segoe UI", 11))
style.configure("Title.TLabel", font=("Segoe UI Semibold", 16))
style.configure("TButton", font=("Segoe UI Semibold", 11), padding=6)
style.configure("TEntry", font=("Segoe UI", 11), padding=4)

frameQR = tb.Frame(app, padding=20)
frameQR.pack()

tb.Label(frameQR, text="QR-Generator", style="Title.TLabel", bootstyle="secondary").pack(pady=(0, 15))
entryURL = tb.Entry(frameQR, width=35)
entryURL.pack(pady=(0, 8))
tb.Button(
    frameQR,
    text="Gen QR",
    bootstyle="secondary",
    command=lambda: genQR(entryURL.get())
).pack(pady=(5, 10))

imgQR = tb.Label(frameQR, image=None)
imgQR.pack(pady=10)

app.mainloop()
