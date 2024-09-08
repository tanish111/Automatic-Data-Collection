Here's a `README.md` file for using the Python script to scrape and download images from istockphoto.com. This README will guide users on setting up the environment, installing the necessary dependencies, and running the script.

---

# Image Scraper using Selenium

This script is a Python-based image scraper that uses Selenium to automate the process of downloading images from istockphoto.com. Given a search query and a number of images to download, the script will scrape the specified number of images and save them to a local folder.

## Prerequisites

To use this script, you'll need to have the following installed:

1. **Python 3.x** - Make sure Python is installed and added to your system's PATH.
2. **Google Chrome Browser** - Ensure that Google Chrome is installed on your machine.
3. **Google ChromeDriver** - The script uses `webdriver_manager` to automatically manage the ChromeDriver for Selenium.

## Installation

1. **Clone the repository** or **download the script**.

2. **Install Required Packages**

   Open a terminal or command prompt in the directory containing the script and run the following command to install the required Python packages:

   ```bash
   pip install selenium webdriver-manager
   ```

## Usage

1. **Set Up the Script**

   Open the `image_scraper.py` script in a text editor and modify the `query` and `num_images` variables to specify your search query and the number of images you want to download:

   ```python
   query = "apple"  # Replace with your search query
   num_images = 50  # Number of images to extract
   ```

2. **Run the Script**

   Run the script using the following command:

   ```bash
   python image_scraper.py
   ```

   The script will create a new folder in the `downloads` directory named after your search query (with spaces replaced by hyphens). Images will be saved in this folder.

## How It Works

1. The script initializes a **headless Chrome browser** using Selenium and opens the istockphoto.com search page for the specified query.
2. It loops through the search results, extracts the URLs of the images, and downloads them using `urllib.request`.
3. The images are saved in a folder named after the search query in the `downloads` directory.

## Important Notes

- **Avoid Overloading the Website**: To avoid getting blocked, the script includes a `time.sleep(5)` delay between page requests. You can adjust this delay as needed.
- **Error Handling**: The script includes basic error handling to manage issues like failed downloads or extraction errors.
- **Automation Controlled**: Some websites can detect automation tools like Selenium and block access. The script attempts to bypass detection using `--disable-blink-features=AutomationControlled`.

## Example Output

If you search for "apple" and request 50 images, the script will create a folder named `downloads/apple` and save the images as `image1.jpg`, `image2.jpg`, ..., `image50.jpg`.

## Troubleshooting

- **Driver Issues**: If you encounter issues with the ChromeDriver, make sure your version of Chrome matches the version of ChromeDriver installed by `webdriver_manager`.
- **Firewall or Network Restrictions**: Ensure that your network or firewall settings allow access to istockphoto.com.

## Disclaimer

This script is intended for educational purposes only. Make sure to comply with the terms and conditions of istockphoto.com when scraping images. Use responsibly and avoid overloading their servers.

## License

This project is licensed under the MIT License.

---

Feel free to adjust the README as needed to better fit your project or specific use case!
