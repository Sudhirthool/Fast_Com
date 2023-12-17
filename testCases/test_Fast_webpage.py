from pageObjects import Fast_com_page

class Test_FAST_PAGE:
    def test_fast_page(self, setup):
        self.driver = setup
        self.FP = Fast_com_page.Fast_com_page(self.driver)
        # capture screenshot
        self.FP.capture_screenshot()
        self.driver.save_screenshot("D:\\sudhir\\software testing\\Automation Pytest Selenium Practice\\FAST.COM\\Screenshots\\fasT_page.png")
