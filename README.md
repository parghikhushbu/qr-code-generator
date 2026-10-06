# QR Code Generator

A simple Python project that creates QR codes using the `qrcode` library. It has two scripts:

- `qr_basic.py` creates a simple black and white QR code.
- `qr_custom_color.py` creates a red QR code with high error correction, so it can still be scanned if part of it is damaged.

## Requirements

- Python 3 installed on your computer
- The `qrcode` and `pillow` libraries

Install them with:

```
pip install qrcode pillow
```

## How to run

In a terminal, inside the project folder:

```
python qr_basic.py
python qr_custom_color.py
```

Or open a file in VS Code and click the **Run** button.

Each script saves a PNG image in the same folder:

- `qr_basic.py` creates `qr_basic.png`
- `qr_custom_color.py` creates `qr_custom_color.png`

## How to use your own link

Both scripts use `https://www.example.com` as a sample. To make a QR code for your own link or text, replace it in the script:

```python
img = qr.make("https://your-link-here.com")
```

In `qr_custom_color.py`, change it inside `qr.add_data(...)`.

## How to change the color

In `qr_custom_color.py`, edit this line:

```python
img = qr.make_image(fill_color="red", back_color="white")
```

Try colors like `"blue"`, `"green"`, or `"black"`.

## License

This project is licensed under the MIT License.
