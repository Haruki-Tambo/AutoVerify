from test_base import BaseTest
from pages.base_page import BasePage
import os

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
        
if __name__ == "__main__":
    import unittest
    unittest.main()