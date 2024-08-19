from pages.base_page import BasePage
import os
from selenium.webdriver.common.by import By
from selenium import webdriver

import os
from dotenv import load_dotenv
load_dotenv()

"""
検索ウィンドウに文字列を入力して検索をクリックするテスト
"""
# テストでアクセスするURL
url = "https://wa3.i-3-i.info/"

# Webページにアクセス
edge_driver_path = os.getenv('EDGE_DRIVER_PATH')
driver = webdriver.Edge(executable_path=edge_driver_path)

# driver.maximize_window()  # 画面を最大化
driver.get(url)
# BasePageを初期化
base_page = BasePage(driver)

# 検索ウィンドウのロケータを指定
# input_locator = driver.find_element(By.NAME, "q")
# print(input_locator)
# 検索ウィンドウに入力する文字列
input_text = "レイテンシ"

# 検索ウィンドウに文字列を入力
base_page.input_text(input_text, By.NAME, "q")

# 検索ボタンのロケータを指定
button_locator = (By.ID, "submitSearch")

# 検索ボタンをクリック
base_page.click(By.ID, "submitSearch")

driver.quit()