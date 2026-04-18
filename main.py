"""
Image Resolver - GUI untuk konversi format gambar dan resize.

Dependensi:
    pip install Pillow cairosvg pymupdf

Jalankan:
    python main.py
"""

import sys

# Validasi tkinter
try:
    import tkinter as tk
except ImportError:
    sys.exit("tkinter tidak tersedia. Pastikan Python diinstal dengan modul tkinter.")

# Validasi Pillow
try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow belum terinstal. Jalankan: pip install Pillow")

from src.app import App


def main():
    """Entry point aplikasi."""
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
