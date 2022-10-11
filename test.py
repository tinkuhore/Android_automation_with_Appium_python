import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformname'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'Moto E (4) Plus'
desired_caps['app'] = 'Messages'
desired_caps['appPackage'] = ''Name: Messages
Package: com.google.android.apps.messaging
Signature: 09:80:a1:2b:e9:93:52:8c:19:10:7b:c2:1a:d8:11:47:8c:63:ce:fc
Version name: messages.android_20220916_00_RC01.phone_dynamic
 Version Code: 150147063
desired_caps['']

webdriver.Remote()