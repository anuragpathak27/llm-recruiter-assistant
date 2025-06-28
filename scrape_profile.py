import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

def extract_profile_data(linkedin_url):
    options = uc.ChromeOptions()
    options.add_argument("--headless")  # Remove for debugging
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options)

    try:
        # Step 1: Login to LinkedIn
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        driver.find_element(By.ID, "username").send_keys(EMAIL)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        # Step 2: Visit the candidate profile
        driver.get(linkedin_url)
        time.sleep(5)

        # Step 3: Parse content
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract name
        name = soup.find("h1").get_text(strip=True) if soup.find("h1") else "Unknown"

        # Extract headline
        headline_div = soup.find("div", class_="text-body-medium")
        headline = headline_div.get_text(strip=True) if headline_div else "N/A"

        # Extract location
        location_span = soup.find("span", class_="text-body-small")
        location = location_span.get_text(strip=True) if location_span else "N/A"

        # Extract education
        edu_spans = soup.find_all("span", string=lambda t: t and "University" in t)
        education = edu_spans[0].get_text(strip=True) if edu_spans else "N/A"

        # Extract companies
        exp_spans = soup.find_all("span", class_="mr1 t-bold")
        companies = [span.get_text(strip=True) for span in exp_spans[:2]] if exp_spans else []

        return {
            "name": name,
            "headline": headline,
            "location": location,
            "education": education,
            "companies": companies
        }

    except Exception as e:
        print(f"[ERROR] Failed to scrape {linkedin_url}: {e}")
        return {
            "name": "Unknown",
            "headline": "N/A",
            "location": "N/A",
            "education": "N/A",
            "companies": [],
            "error": str(e)
        }

    finally:
        try:
            driver.quit()
            del driver
        except Exception as e:
            print(f"[WARN] Failed to quit Chrome cleanly: {e}")


# Optional: run directly
if __name__ == "__main__":
    test_url = "https://www.linkedin.com/in/example"
    result = extract_profile_data(test_url)
    print(result)
