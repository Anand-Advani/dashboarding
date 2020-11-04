import time
from selenium import webdriver
from pywinauto import application

app = application.Application()
app2 = application.Application()
app.start("Notepad.exe")
time.sleep(2)
app2.start("Notepad.exe")

app.UntitledNotepad.SetFocus()
time.sleep(2)
app.Notepad.Edit.TypeKeys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)
time.sleep(2)
app2.UntitledNotepad.SetFocus()
time.sleep(2)
app2.Notepad.Edit.TypeKeys("Hiiiiiiiiii !!!!!!!!!" , with_spaces = True)
browser=webdriver.Chrome(executable_path='chromedriver.exe')
browser.get('http:/apple.com')
main_window = browser.current_window_handle
#second tab
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")
browser.get('http://bing.com')
time.sleep(2)
browser.switch_to_window(main_window)

app2.UntitledNotepad.SetFocus()
time.sleep(2)
app2.Notepad.Edit.TypeKeys('   Welcome to Medium AGAINNN!!!!!!', with_spaces = True)

browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window("tab3")
browser.get('http://apple.com')

app2.UntitledNotepad.SetFocus()
time.sleep(2)
app2.Notepad.Edit.TypeKeys('   typing bit more  !!!!!', with_spaces = True)

app.UntitledNotepad.SetFocus()
app.UntitledNotepad.menu_select("File -> Exit")
time.sleep(2)
app.Notepad.DontSave.click()

app2.UntitledNotepad.SetFocus()
app2.UntitledNotepad.menu_select("File -> Exit")
time.sleep(2)
app2.Notepad.DontSave.click()

time.sleep(2)
browser.close()
time.sleep(2)
browser.switch_to.window("tab2")
browser.close()
time.sleep(2)
browser.switch_to_window(main_window)
browser.close()