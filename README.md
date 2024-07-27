# MDAD BRUTE FORCER
### Facebook Brute Force Tool

## Overview

This script is designed to perform a brute force attack on Facebook login credentials. It leverages Selenium WebDriver for browser automation and the `rich` library for enhanced logging and console output. 

## Features

- Automated login attempts using Selenium WebDriver
- Headless operation (no GUI) for background execution
- Captures and saves the page source upon successful login or error
- Customizable input for email and password list

## Requirements

- Python 3.6 or higher
- `pip` (Python package installer)
- `selenium` library
- `rich` library
- Google Chrome and ChromeDriver

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/facebook-brute-force-tool.git
   cd facebook-brute-force-tool
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
> You must have Chrome installed

## Usage

1. **Prepare your password list:**
   - Create a file in the script's directory. Each line should contain one password.


2. **Follow the prompts:**
   - Enter the target email/username when prompted.
   - The script will start attempting logins with passwords from the file you will provide or default password lists with almost 3.3 lac passwords commonly used

## Notes

- Ensure that the email and passwords are formatted correctly and that `passs.trx` does not contain any special characters or unnecessary whitespace.
- Running this tool extensively can result in your IP being temporarily blocked by Facebook.

## License

Distributed under the All Rights Reserved License. See the [LICENSE](LICENSE) file for more information.

## Contact

- **Powered By:** MDAD Solutions
- **Created By:** Aman Ali
- **Email:** help.mdad@gmail.com