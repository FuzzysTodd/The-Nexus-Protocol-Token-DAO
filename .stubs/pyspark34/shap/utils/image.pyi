def is_empty(path):
    """ Function to check if folder at given path exists and is not empty.

    Returns True if folder is empty or does not exist.
    """
def make_dir(path) -> None:
    """
    Function to create a new directory with given path or empty if it already exists.
    """
def add_sample_images(path) -> None:
    """
    Function to add sample images from imagenet50 SHAP data in the given folder.
    """
def load_image(path_to_image):
    """
    Function to load image at given path and return numpy array of RGB float values.
    """
def check_valid_image(path_to_image):
    """
    Function to check if a file has valid image extensions and return True if it does.
    Note: Azure Cognitive Services only accepts below file formats.
    """
def save_image(array, path_to_image) -> None:
    """
    Function to save image(RGB values array) at given path (filename and location).
    """
def resize_image(path_to_image, reshaped_dir):
    """
    Function to resize given image retaining original aspect ratio and save in given directory 'reshaped_dir'.
    Returns numpy array of resized image and path where resized file is saved.
    Note:
    Azure COGS CV has size limit of < 4MB and min size of 50x50 for images.
    Hence, large image files are being reshaped in code below to increase speed of SHAP explanations and run Azure COGS for image captions.
    If image (pixel_size, pixel_size) is greater than 500 for either of the dimensions:
    1 - image is resized to have max. 500 pixel size for the dimension > 500
    2 - other dimension is resized retaining the original aspect ratio
    """
def display_grid_plot(list_of_captions, list_of_images, max_columns: int = 4, figsize=(20, 20)) -> None:
    """
    Function to display grid of images and their titles/captions.
    """
