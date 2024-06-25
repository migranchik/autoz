import time

from pywinauto import Application, Desktop
from pywinauto.timings import wait_until


class MEmuDriver():

    def __init__(self):
        self.THREAD_NUM = 1
        self.app = Application(backend='uia').connect(class_name="MainWindow")
        self.main_window = self.app.window()
        self.first = self.main_window.child_window(class_name="VmsTableView")
        self.item = self.first.child_window(control_type="DataItem", found_index=5)

    def open_memu_hub(self):
        self.main_window.minimize()
        self.main_window.set_focus()

    def open_emulator(self):
        self.open_memu_hub()
        self.item.click_input(coords=(230, 30))

        dialog = self.app.window(title='MEmuConsole')
        dialog.child_window(title="Клонировать", control_type="MenuItem").click_input()

        time.sleep(1)

        edit = self.main_window.child_window(class_name="QLineEdit", control_type="Edit")
        edit.set_text(1)

        self.main_window.child_window(title="Окей", control_type="Button").click()
        time.sleep(10)

        self.item = self.first.child_window(control_type="DataItem", found_index=5)
        self.item.click_input(coords=(10, 80))

    def close_emulator(self):
        self.open_memu_hub()

        self.item.click_input(coords=(10, 80))

    def delete_emulator(self):
        self.open_memu_hub()

        self.item.click_input(coords=(200, 80))
        self.main_window.child_window(title="Окей", control_type="Button").click()



'''
main_window.child_window(control_type="CheckBox", found_index=0).click()
time.sleep(2)
main_window.child_window(title="Начать", auto_id="WindowFrameWindow.frame-content-widget.MEmuButtonsWidget.normal_greenButton3", control_type="Button").click()
'''