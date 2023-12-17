import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#
driver = webdriver.Chrome()

# driver.get("https://testautomationpractice.blogspot.com/")

driver.get("https://www.google.com/search?q=mahadbtmahait&rlz=1C1ONGR_enIN1067IN1068&oq=mahadbtmahait&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTIwODM0ajBqNKgCALACAA&sourceid=chrome&ie=UTF-8")
time.sleep(10)
if True:
    driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[1]/div/div/span/a/div").click()
else:
    assert False

# check_boxes = driver.find_elements(By.XPATH, "//*[@id='post-body-1307673142697428135']/div[4]//div")
# length_of_checkbox = len(check_boxes) # 7
# print(length_of_checkbox)
# last_2_checkboxes = length_of_checkbox-2 # 5
#
# print(length_of_checkbox,last_2_checkboxes, length_of_checkbox) # output 5, 7 5=friday 6= saturday it exclude 7
#
# for r in range(last_2_checkboxes, length_of_checkbox):
#     check_boxes[r].click()
#
# driver.save_screenshot("D:\\sudhir\\software testing\\Automation Pytest Selenium Practice\\FAST.COM\\Screenshots\\checkboxes.png")
# time.sleep(4)
# driver.quit()

    # '''last_2_checkboxes=5, length_of_checkbox=7'''
    # # range(last_2_checkboxes, length_of_checkbox)
# b = range(5,7)
# b = list(b)
#
# print(b
# ) # output [5, 6]


# number = [1, 2, 3, 4, 5, 6, 7]
# cn = len(number)-1
#
# number[cn], number[0] = number[0], number[cn]
# print(number)
#
# a = input('give value: ')
# if a % 2 == 0 :
#     print('number is ')
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# # Input a number to check for primality
# number = int(input("Enter a number: "))
#
# if is_prime(number):
#     print(number, "is a prime number.")
# else:
#     print(number, "is not a prime number.")
