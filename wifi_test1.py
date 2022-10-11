import datetime
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd

df = pd.DataFrame(columns=['Iterate', 'Date', 'On_Time', 'Off_Time', 'Status'])
ITERATE = 20
WIFI_NAME = 'Hore-1'
PASSWORD = 'bolbokeno'

desired_cap = {
    "appium:deviceName": "ZH33L274JW",
    "platformName": "Android",
    "appium:appPackage": "ee17c57 u0 com.motorola.launcher3",
    "appium:appActivity": "com.android.launcher3.GoogleNowPanel",
    "appium:platformVersion": "7",
    "appium:adbExecTimeout": "30000",
    "appium:automationName": "UiAutomator2",
    "appium:uiautomator2ServerInstallTimeout": "90000",
    "appium:noReset": "true",
    "appium:fullReset": "false"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


def wifi():
    try:
        driver.press_keycode(3)

        driver.toggle_wifi()
        on_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(10)
        driver.toggle_wifi()
        off_time = datetime.datetime.now().strftime("%H:%M:%S")
        return 'Pass', on_time, off_time

    except Exception as e:
        print(e)
        return 'Fail', None, None


def wifi_new_connection(password: str = None):
    #try:
    driver.press_keycode(3)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'App list').click()
    driver.find_element(AppiumBy.ID, 'com.android.launcher3:id/search_box_input').send_keys('settings')

    # search for settings app
    # search = 'settings'
    # for i in search:
    #     code = 29 + (ord(i) - 97)
    #     driver.press_keycode(code)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Settings').click()
    driver.find_element(AppiumBy.ID, 'com.android.settings:id/dashboard_tile').click()
    driver.find_element(AppiumBy.ID, 'com.android.settings: id / switch_widget').is_enabled()
    # driver.find_element(AppiumBy.XPATH, f'//android.widget.LinearLayout[@content-desc="{WIFI_NAME},,Wi-Fi signal '
    #                                    'full."]/android.widget.RelativeLayout/android.widget.TextView')
    # except Exception as e:
    #     print('Failed to connect! - ', e)


# i = 1
# while i <= ITERATE:
#     status, on_time, off_time = wifi()
#     log = [i, datetime.date.today().strftime("%d/%m/%Y"), on_time, off_time, status]
#     print(log)
#     df.loc[len(df.index)] = log
#     i += 1
#
# writer = pd.ExcelWriter("wifi_test_log.xlsx")
# df.to_excel(writer, sheet_name='sheet', index=False)
# writer.save()
# status = list(df['Status'])
# p_count = status.count('Pass')
# f_count = status.count('Fail')
# print("Iteration = ", ITERATE, "Pass Count = ", p_count, "Fail Count = ", f_count)

wifi_new_connection()
