#-*-coding:utf-8-*-
"""
@FileName:
    server.py
@Description:
    class PlayWright
@Authors:
    Hanbo Sun(sun-hb17@mails.tsinghua.edu.cn)
@CreateTime:
    2021/12/22 17:14
"""
import threading
from playwright.sync_api import Playwright, sync_playwright

class MyPlayWright(object):
    """
    My PlayWright class
    """
    def __init__(self):
        super(MyPlayWright, self).__init__()

    def _run_chrome(self):
        """
        run chrome, one threading
        """
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()

            # Open new page
            page = context.new_page()
            # Go to https://www.ipaddress.com/search
            page.goto("https://www.ipaddress.com/search")

            # Click [placeholder="IP address, Domain or Hostname"]
            page.click("[placeholder=\"IP address, Domain or Hostname\"]")
            # Fill [placeholder="IP address, Domain or Hostname"]
            page.fill("[placeholder=\"IP address, Domain or Hostname\"]", "github.com")
            # Click button:has-text("Lookup")
            page.click("button:has-text(\"Lookup\")")
            # assert page.url == "https://ipaddress.com/website/github.com"

            query = page.query_selector("td:right-of(th:has-text(\"IP Address\"))")
            ip = query.textContent()



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)


    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

    # return ip
    return ip


with sync_playwright() as playwright:
    ip = run(playwright)
    print("github ip is {ip}")
