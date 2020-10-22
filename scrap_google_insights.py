from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Articles:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.w = WebDriverWait(self.driver, 60)

    def set_category(self, category):
        self.w.until(EC.presence_of_element_located((By.ID, "subjectInput")))
        search = self.driver.find_elements_by_id("subjectInput")[1]
        search.send_keys(category)
        search.send_keys(Keys.RETURN)

    def clicking_on_date_element(self, value):
        elements = self.driver.find_elements_by_class_name("mat-calendar-body-cell-content")
        for element in elements:
            if element.text == value:
                element.click()
                break

    def enter_date(self, date):

        year_arrow = self.driver.find_element_by_class_name("mat-calendar-arrow")
        year_arrow.click()
        day, month, year = date.split()
        self.clicking_on_date_element(year)
        self.clicking_on_date_element(month.upper())
        self.clicking_on_date_element(day)

    def set_duration(self, duration="month"):
        if duration == "month":
            element = self.driver.find_element_by_xpath('//*[@id="cdk-accordion-child-1"]/div/div/div[1]/ul/li[1]')
        else:
            element = self.driver.find_element_by_xpath('//*[@id="cdk-accordion-child-1"]/div/div/div[1]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def download_data(self):

        self.w.until(EC.presence_of_element_located((By.XPATH, '//*[@id="brand-card"]/div/div/div/div/si-chart-list'
                                                               '/div/div/ul')))
        hamburger_icon = self.driver.find_element_by_xpath(
            '/html/body/si-root/div/ng-component/mat-sidenav-container/mat-sidenav-content/main/ng-component/div/div['
            '2]/div/si-card[2]/mat-card/div/div/div[2]/div/mat-icon')

        self.driver.execute_script("arguments[0].click();", hamburger_icon)
        self.w.until(EC.presence_of_element_located((By.CLASS_NAME, 'mat-menu-content')))
        download_button = self.driver.find_element_by_class_name('mat-menu-content').find_element_by_tag_name("button")
        self.driver.execute_script("arguments[0].click();", download_button)

    def main(self, sent_data):
        # print(sent_data)
        from_date = sent_data["from"]
        to_date = sent_data["to"]
        duration = sent_data["duration"]
        category = sent_data["category"]

        self.driver.get("https://shopping.thinkwithgoogle.com/")
        print("Done Fetching URL")
        self.set_category(category)

        from_date_filter = self.driver.find_element_by_class_name("mat-form-field-infix")
        self.driver.execute_script("arguments[0].click();", from_date_filter)
        self.enter_date(from_date)

        self.w.until(EC.presence_of_element_located((By.CLASS_NAME, "mat-form-field-infix")))
        to_date_filter = self.driver.find_elements_by_class_name("mat-form-field-infix")[1]
        self.driver.execute_script("arguments[0].click();", to_date_filter)
        self.enter_date(to_date)

        self.set_duration(duration)
        self.download_data()


if __name__ == "__main__":
    art = Articles()
    art.main({
        "from": "20 Jan 2020",
        "to": "20 Mar 2020",
        "duration": "month",
        "category": "Toys"
    })
