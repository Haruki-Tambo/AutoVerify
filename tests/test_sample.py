from test_base import BaseTest
from pages.base_page import BasePage
import os
from selenium.webdriver.common.by import By

class SampleScreenshotTest(BaseTest):
    def test_take_screenshot(self):
        """
        指定されたWebページにアクセスし、スクリーンショットを撮影するテスト。
        """
        # テストでアクセスするURL
        url = "https://wa3.i-3-i.info/"
        
        # Webページにアクセス
        self.driver.get(url)
        
        # BasePageを初期化
        base_page = BasePage(self.driver)
        
        # スクリーンショットの保存先
        screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
        
        # スクリーンショットを撮影
        base_page.take_screenshot(screenshot_path)
        
        # スクリーンショットが保存されているかを確認
        self.assertTrue(os.path.exists(screenshot_path), "スクリーンショットが保存されていません")
    
    def test_click(self):
        """
        検索ウィンドウに文字列を入力して検索をクリックするテスト
        """
        # テストでアクセスするURL
        url = "https://wa3.i-3-i.info/"
        
        # Webページにアクセス
        self.driver.get(url)
        
        # BasePageを初期化
        base_page = BasePage(self.driver)

        # 検索ウィンドウのロケータを指定
        input_locator = (By.NAME, "q")

        # 検索ウィンドウに入力する文字列
        input_text = "レイテンシ"

        # 検索ウィンドウに文字列を入力
        base_page.input_text(input_text, input_locator)

        # 検索ボタンのロケータを指定
        button_locator = (By.ID, "submitSearch")

        # 検索ボタンをクリック
        base_page.click(button_locator)

        # 想定したページに遷移したかの確認
        self.assertTrue(base_page.is_text_present("往復レイテンシ"), "検索が成功しました")

if __name__ == "__main__":
    import unittest
    unittest.main()