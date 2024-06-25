import os
import uiautomator2 as u2
import time
from get_code import get_code

out = os.popen('adb devices')
print(out.readline())
ips = []
for i in out:
    if len(i) > 10:
        ips.append(i.strip().split()[0])

ip = ips[0]
print(ip)
d = u2.connect(ip)  # connect to device
time.sleep(1)
d.xpath('//*[@text="TikTok"]').click()
'''
time.sleep(3)
try:
    d.xpath('//*[@resource-id="android:id/button3"]').click()
except Exception as e:
    print("not exist button")
'''

time.sleep(9)
d.swipe_ext("up", scale=0.8)
time.sleep(2)
d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/efj"]').click()
time.sleep(1)
d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/afw"]').click()
time.sleep(1)
d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/e9v"]').click()
time.sleep(1)
d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/anm"]/android.view.ViewGroup[1]').click()
time.sleep(1)
d.xpath('//*[@text="Почта / имя пользователя"]').click()
time.sleep(1)
d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/br0"]').click()
time.sleep(1)
d.xpath('//*[@text="Почта"]').click()
time.sleep(1)
d.send_keys('eilbheaodbha@hotmail.com')
time.sleep(1)
d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/d6r"]').click()
time.sleep(25)
code = get_code('eilbheaodbha@hotmail.com', 'IkuYp5uYh9Rc')
time.sleep(6)
d.send_keys(code)
time.sleep(6)
d.send_keys("Ilyasik2006#")
time.sleep(1)
d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/b7_"]').click()
time.sleep(15)
d.xpath('//*[@text="Не разрешать"]').click()
time.sleep(2)
try:
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/esm"]')
except Exception as e:
    print('not exist button')
d.swipe_ext("up", scale=0.8)

for i in range(1, 6):
    time.sleep(2)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/efe"]/android.widget.ImageView[1]').click()
    time.sleep(2)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/dq2"]').click()
    time.sleep(3)
    if i == 0:
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/cnj"]').click()
    time.sleep(1)
    d.xpath('//*[@text="Фото"]').click()
    time.sleep(1)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/ix4"]').click()
    time.sleep(1)
    d.xpath('//*[@text="Pictures"]').click()
    time.sleep(1)
    d.xpath(
        '//*[@resource-id="com.zhiliaoapp.musically:id/d14"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
    time.sleep(1)
    d.xpath(
        '//*[@resource-id="com.zhiliaoapp.musically:id/d14"]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
    time.sleep(1)
    d.xpath(
        '//*[@resource-id="com.zhiliaoapp.musically:id/d14"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
    time.sleep(1)
    d.xpath(
        '//*[@resource-id="com.zhiliaoapp.musically:id/d14"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
    time.sleep(1)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/hjx"]').click()
    time.sleep(3)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/evt"]').click()
    time.sleep(1)
    if i == 0:
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/axw"]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]').click()
        time.sleep(1)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/fya"]').click()
    time.sleep(1)
    if i == 0:
        try:
            d.xpath('//*[@text="Опубликовать"]').click()
            d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/fya"]').click()
        except Exception as e:
            print('Not exist button')

