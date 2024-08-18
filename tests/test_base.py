import unittest
from selenium import webdriver

import os
from dotenv import load_dotenv
load_dotenv()

class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        各テストの前に実行されるセットアップメソッド。
        WebDriverを初期化し、テスト対象のURLにアクセスします。
        """

        edge_driver_path = os.getenv('EDGE_DRIVER_PATH')
        self.driver = webdriver.Edge(executable_path=edge_driver_path)

        self.driver.maximize_window()  # 画面を最大化

    def tearDown(self):
        """
        各テストの後に実行されるティアダウンメソッド。
        WebDriverを終了します。
        """
        if self.driver:
            self.driver.quit()