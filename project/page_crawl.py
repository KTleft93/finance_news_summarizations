import time

from playwright.sync_api import sync_playwright
from llm_caller import GroqService
from discord_caller import send_discord_message


groq_service = GroqService()


def page_crawler(link: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(link)

        """
        Get page body
        if yf use bodyItems-wrapper
        """
        text = page.locator(".bodyItems-wrapper").inner_text()

        """
        Output
        """
        if text:
            result_text = "".join(groq_service.run_prompt(text))

            time.sleep(3)
            summary_text = "".join(groq_service.run_prompt_two(result_text))
            send_discord_message(result_text)
            send_discord_message(summary_text)
            browser.close()
        else:
            browser.close()
