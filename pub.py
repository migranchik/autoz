import os
import uiautomator2 as u2
import time
from download_rnd import download_random_dog_images
from uniqueizer import blend_images
from get_code import get_code
from open_menu import MEmuDriver


def get_creo_count(folder_path):
    files = os.listdir(folder_path)
    counter = 0

    for file_name in files:
        # Пропускаем подпапки
        if os.path.isdir(os.path.join(folder_path, file_name)):
            continue
        counter += 1
    return counter


def uniqueize_creo(creo_path, background_path, output_path):
    for i in range(1, creo_count + 1):
        background_image_path = f"{background_path}/{i}.jpg"
        overlay_image_path = f"{creo_path}/cr{i}.jpg"
        output_image_path = f"{output_path}/{i}.jpg"
        blend_images(background_image_path, overlay_image_path, output_image_path)


accounts = open('accounts.txt')
memu_driver = MEmuDriver()
pass_tiktok = "Kutak123#"

for account in accounts:

    # берем аккаунт
    if ':' not in account:
        continue
    mail, mail_pass = account.split(':')
    print(mail)

    # уникализация
    creo_count = get_creo_count('creo')

    print(f'Количество фоток в крео: {creo_count}')
    download_random_dog_images(creo_count)

    uniqueize_creo('creo', 'uniq', 'creo_uniq')

    # создаем и запускаем эмулятор
    memu_driver.open_emulator()

    # подключаемся к эмулятору
    ips = []
    while len(ips) == 0:
        out = os.popen('adb devices')
        print(out.readline())
        for i in out:
            if len(i) > 10:
                ips.append(i.strip().split()[0])
        print(ips)
        time.sleep(1)

    time.sleep(10)

    ip = ips[0]
    print(ip)

    # заливаем
    d = u2.connect(ip)  # connect to device
    time.sleep(1)
    d.xpath('//*[@text="SocksDroid"]').click()
    time.sleep(1)
    d.xpath('//*[@resource-id="net.typeblog.socks:id/switch_action_button"]').click()
    time.sleep(1)
    d.press('home')
    time.sleep(1)
    d.xpath('//*[@text="TikTok"]').click()
    time.sleep(5)
    try:
        d.xpath('//*[@resource-id="android:id/button3"]').click()
    except Exception as e:
        print("not exist button")

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
    d.send_keys(mail)
    time.sleep(1)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/d6r"]').click()
    time.sleep(20)
    code = get_code(mail, mail_pass)
    print(code)
    time.sleep(6)
    d.send_keys(code)
    time.sleep(20)
    d.send_keys(pass_tiktok)
    time.sleep(1)
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/b7_"]').click()
    time.sleep(15)
    d.xpath('//*[@text="Не разрешать"]').click()
    time.sleep(2)
    try:
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/b1v"]').click()
    except Exception as e:
        print('not exist button')
    d.swipe_ext("up", scale=0.8)

    for i in range(6):
        time.sleep(2)
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/efe"]/android.widget.ImageView[1]').click()
        time.sleep(2)
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/dq2"]').click()
        time.sleep(3)
        if i == 0:
            d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/cnj"]').click()
        time.sleep(1)
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/ix4"]').click()
        time.sleep(1)
        d.xpath('//*[@text="Pictures"]').click()
        time.sleep(1)
        if i == 0:
            d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/en9"]').click()
        time.sleep(1)

        d.xpath(
            '//*[@resource-id="com.zhiliaoapp.musically:id/cme"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
        time.sleep(1)

        d.xpath(
            '//*[@resource-id="com.zhiliaoapp.musically:id/cme"]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
        time.sleep(1)

        d.xpath(
            '//*[@resource-id="com.zhiliaoapp.musically:id/cme"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
        time.sleep(1)

        d.xpath(
            '//*[@resource-id="com.zhiliaoapp.musically:id/cme"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
        time.sleep(1)
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/hjx"]').click()
        time.sleep(3)
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/evt"]').click()
        time.sleep(1)
        if i == 0:
            d.xpath(
                '//*[@resource-id="com.zhiliaoapp.musically:id/axw"]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]').click()
            time.sleep(1)
        d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/fya"]').click()
        time.sleep(1)
        if i == 0:
            try:
                d.xpath('//*[@text="Опубликовать"]').click()
                d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/fya"]').click()
            except Exception as e:
                print('Not exist button')

    time.sleep(40)
    # закрываем эмулятор
    memu_driver.close_emulator()
    time.sleep(3)
    # удаляем эмулятор
    memu_driver.delete_emulator()
    time.sleep(3)