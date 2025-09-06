# Steganography_Image
"A basic Python implementation of steganography to hide text in image pixels."

# Simple Image Steganography

This Python project demonstrates a basic steganography technique to hide a secret text message within an image file.

## How It Works

The script embeds the secret message by modifying the pixel data of a source image.

-   **Encoding:** Each character of the secret message is converted into its ASCII numerical value. This value then replaces the **Green channel value** of specific pixels in the image. The pixels are chosen based on a predefined pattern (e.g., at horizontal intervals of 100 pixels on a fixed row).

-   **Decoding:** The decoder script reads the Green channel values from the exact same predefined pixel locations. It converts these ASCII values back into characters to reveal the original message.

## Usage

1.  **Prepare:** Place your source image (e.g., `image.jpg`) in the same directory.
2.  **Encode:** Run the `encoder.py` script. It will generate a new image, `encoded_image.png`, containing the hidden message.
3.  **Decode:** Run the `decoder.py` script to extract the message from `encoded_image.png` and print it to the console.

### **Important Note**
You **must** save the output image in a lossless format like **PNG**. Using a lossy format like **JPG** will alter pixel values during compression and corrupt the hidden data.






