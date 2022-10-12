import datetime
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from csv import writer

# constant parameters
DEVICE_NAME = "ZH33L274JW"
PLATFORM_VERSION = "7"


def wifi(iterate):
    # Initiating test report
    report = ['Main test case', 'Detailed step', 'Intended number of tests', 'Start Time', 'End Time', 'Duration',
              'Actual number of tests', 'Pass', 'Fail', 'Success Rate', 'Remarks', 'Details']
    report[0] = 'Toggle wifi'
    report[1] = 'Turn on wifi, wait for 10 sec, turn off wifi'
    report[2] = iterate
    report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Starting Appium webdriver
    desired_cap = {
        "appium:deviceName": DEVICE_NAME,
        "platformName": "Android",
        "appium:appPackage": "ee17c57 u0 com.motorola.launcher3",
        "appium:appActivity": "com.android.launcher3.GoogleNowPanel",
        "appium:platformVersion": PLATFORM_VERSION,
        "appium:adbExecTimeout": "30000",
        "appium:automationName": "UiAutomator2",
        "appium:uiautomator2ServerInstallTimeout": "90000",
        "appium:noReset": "true",
        "appium:fullReset": "false"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.press_keycode(3)
    driver.set_network_connection(0)

    pass_count, fail_count, test_count = 0, 0, 0
    start = datetime.datetime.now()
    while test_count < iterate:
        try:
            driver.toggle_wifi()
            time.sleep(10)
            driver.toggle_wifi()
            pass_count += 1

        except Exception as e:
            print(f"Iteration = {test_count}| WIFI ON-OFF Failed! | with Error : {e}")
            fail_count += 1
        test_count += 1
    end = datetime.datetime.now()

    # finishing test repost
    report[4] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    report[5] = str(end - start).split('.')[0]
    report[6] = test_count
    report[7] = pass_count
    report[8] = fail_count
    report[9] = round((pass_count / test_count) * 100, 2)
    report[10] = None
    report[11] = None

    # insert test repost to csv file
    with open('automation_stability_test.csv', 'a') as f:
        writer(f).writerow(report)
        f.close()


wifi(3)
