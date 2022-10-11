import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import pandas as pd

df = pd.DataFrame(columns=['Iterate', 'Date', 'Start_Time', 'End_Time', 'Status'])

PHONE_NUMBER = "9614929765"  # put the phone number here
ITERATION = 5
VALUES = {'0': '0,+', '1': '1,', '2': '2,ABC', '3': '3,DEF', '4': '4,GHI', '5': '5,JKL',
          '6': '6,MNO', '7': '7,PQRS', '8': '8,TUV', '9': '9,WXYZ'}

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


def call_automation():
    start_time = datetime.datetime.now().strftime("%H:%M:%S")
    try:
        driver.press_keycode(3)
        call_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Phone')
        call_icon.click()
        time.sleep(1)
        dialer_pad = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'dial pad')
        dialer_pad.click()
        time.sleep(1)

        # Dialing phone number
        for i in str(PHONE_NUMBER):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, VALUES[i]).click()

        dialer_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'dial')
        dialer_icon.click()
        time.sleep(3)
        driver.terminate_app('com.android.dialer')

        end_time = datetime.datetime.now().strftime("%H:%M:%S")

        return 'Pass', start_time, end_time
    except Exception as e:
        print('Call failed : ', e)
        end_time = datetime.datetime.now().strftime("%H:%M:%S")
        return 'Fail', start_time, end_time


i = 0
while i < ITERATION:
    status, start_time, end_time = call_automation()
    log = [i + 1, datetime.date.today().strftime("%d/%m/%Y"), start_time, end_time, status]
    print(log)
    df.loc[len(df.index)] = log
    i += 1

writer = pd.ExcelWriter("call_test_log.xlsx")
df.to_excel(writer, sheet_name=PHONE_NUMBER, index=False)
writer.save()
