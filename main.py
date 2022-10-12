import datetime
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from csv import writer

# constant parameters
DEVICE_NAME = "ZH33L274JW"
PLATFORM_VERSION = "7"

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
# Initiating test report
report = ['Main test case', 'Detailed step', 'Intended number of tests', 'Start Time', 'End Time', 'Duration',
          'Actual number of tests', 'Pass', 'Fail', 'Success Rate', 'Remarks', 'Details']


def wifi(iterate):
    """This function Automatically turns ON the WIFI for 10 sec and turns it OFF"""
    # test report
    report[0] = 'Toggle wifi'
    report[1] = 'Turn on wifi, wait for 10 sec, turn off wifi'
    report[2] = iterate
    report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Starting Appium webdriver
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
    driver.close()

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


def playstore_test():
    """
    Store front / Download Stability Test
    event 1 -> open and close Play Store
    event 2 -> download and install any native application
    event 3 -> open downloaded application
    event 4 -> delete downloaded application
    """
    # test report
    report[0] = 'Download Stability Test'

    # Starting Appium webdriver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.press_keycode(3)
    driver.set_network_connection(6)

    def event1(iterate=20):
        report[1] = 'open and close Play Store'
        report[2] = iterate
        report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def event2(iterate=10):
        report[1] = 'download and install any native application'
        report[2] = iterate
        report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def event3(iterate=20):
        report[1] = 'download and install any native application'
        report[2] = iterate
        report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def event4(iterate=1):
        report[1] = 'delete downloaded application'
        report[2] = iterate
        report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# Messaging Stability Tests
desired_cap = {
    "appium:deviceName": "RZ8N91E8TPM",
    "platformName": "Android",
    "appium:appPackage": "com.samsung.android.messaging",
    "appium:appActivity": "com.android.mms.ui.ConversationComposer",
    "appium:platformVersion": "12",
    "appium:adbExecTimeout": "30000",
    "appium:automationName": "UiAutomator2",
    "appium:uiautomator2ServerInstallTimeout": "90000",
    "appium:noReset": "true",
    "appium:fullReset": "false"
}


'''
Messaging Stability Tests
1. 
2.
3.Send an SMS maximum number of characters with out requiring the message to be segmented from the DUT.
4.
'''


def mobile_originating_message_maxCharacters(iterate):
    """This function Automatically test the SMS service of the Messaging app."""
    # test report
    report[0] = 'SMS Automation'
    report[1] = 'Send an SMS maximum number of characters with out requiring the message to be segmented from the DUT.'
    report[2] = iterate
    report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    pass_count, fail_count, test_count = 0, 0, 0
    start = datetime.datetime.now()
    while test_count < iterate:
        # Automation Code
        # send the message
        MT_contact = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="⁨My Jio⁩"]')
        MT_contact.click()
        time.sleep(2)
        text_box = driver.find_element(AppiumBy.ID, 'com.samsung.android.messaging:id/message_edit_text')
        text_box.send_keys(
            '1234567890@#$%^&*()qwertyuiop[]sdfghjkl;qwertyuiopasdfghjklzxcvbnm,./;12345678901234567890!@#$%^&*('
            ')qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfgjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901!@#$%^&*()_+asdfghjklqwertyuopzxcvbnm')
        send_message = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Send')
        send_message.click()
        time.sleep(4)

        # SENT or FAILED
        if:
            fail_count+=1
        else:
            pass_count+=1

        # Delete the message
        delete_settings = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Conversation settings')
        delete_settings.click()
        time.sleep(2)
        delete_message = driver.find_element(AppiumBy.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                             '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                             '/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android'
                                             '.widget.FrameLayout['
                                             '2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')
        delete_message.click()
        select_last_message = driver.find_element(AppiumBy.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout'
                                                  '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                                  '.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.CheckBox')
        select_last_message.click()
        delete_all = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete')
        delete_all.click()
        time.sleep(2)
        move_to_recycle = driver.find_element(AppiumBy.ID, 'android:id/button1')
        move_to_recycle.click()
        test_count += 1
    end = datetime.datetime.now()
    driver.close()

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


def MMS_with_MAXCHAR_AUDIO(iterate):
    """This function Automatically test the MMS service of Messaging app."""
    # test report
    report[0] = 'MMS Automation'
    report[1] = 'Send an SMS maximum number of characters with out requiring the message to be segmented from the DUT.'
    report[2] = iterate
    report[3] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    pass_count, fail_count, test_count = 0, 0, 0
    start = datetime.datetime.now()
    while test_count < iterate:
        # Automation Code
        # send the MMS
        MT_contact = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="⁨My Jio⁩"]')
        MT_contact.click()
        time.sleep(2)
        other_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Other options')
        other_option.click()
        time.sleep(2)
        audio = driver.find_element(AppiumBy.XPATH,
                                    '//android.widget.LinearLayout[@content-desc="Audio"]/android.widget.RelativeLayout')
        audio.click()
        time.sleep(2)
        voice_recorder_folder = driver.find_element(AppiumBy.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]')
        voice_recorder_folder.click()
        select_audio = driver.find_element(AppiumBy.ID, 'com.sec.android.app.myfiles:id/ripple')
        select_audio.click()
        time.sleep(2)
        done = driver.find_element(AppiumBy.XPATH,
                                   '//android.widget.Button[@content-desc="Done"]/android.view.ViewGroup/android.widget.TextView')
        done.click()
        time.sleep(2)
        text_box = driver.find_element(AppiumBy.ID, 'com.samsung.android.messaging:id/message_edit_text')
        text_box.send_keys(
            '1234567890@#$%^&*()qwertyuiop[]sdfghjkl;qwertyuiopasdfghjklzxcvbnm,./;12345678901234567890!@#$%^&*()qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfgjklzxcvbnm1234567890qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901!@#$%^&*()_+asdfghjklqwertyuopzxcvbnm')
        send_message = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Send')
        send_message.click()
        time.sleep(60)

        # SENT or FAILED
        if:
            fail_count += 1
        else:
            pass_count += 1

        # Delete the message
        delete_settings = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Conversation settings')
        delete_settings.click()
        time.sleep(2)
        delete_message = driver.find_element(AppiumBy.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')
        delete_message.click()
        select_last_message = driver.find_element(AppiumBy.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.CheckBox')
        select_last_message.click()
        delete_all = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delete')
        delete_all.click()
        time.sleep(2)
        move_to_recycle = driver.find_element(AppiumBy.ID, 'android:id/button1')
        move_to_recycle.click()
        test_count += 1
    end = datetime.datetime.now()
    driver.close()

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

mobile_originating_message_maxCharacters(20)
MMS_with_MAXCHAR_AUDIO(20)
#wifi(3)
