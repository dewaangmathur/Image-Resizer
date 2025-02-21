from PIL import Image

# Define required sizes
IMAGE_SIZES = {
    "300x250": (300, 250),
    "728x90": (728, 90),
    "160x600": (160, 600),
    "300x600": (300, 600)
}

def resize_image(image_path):
    """Resize the uploaded image into predefined sizes."""
    resized_images = {}
    with Image.open(image_path) as img:
        for size, dimensions in IMAGE_SIZES.items():
            resized_img = img.resize(dimensions)
            resized_images[size] = resized_img
    return resized_images
