from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        """
        初期化メソッドでWebDriverインスタンスを受け取り、クラスのプロパティとして保持します。
        """
        self.driver = driver

    def find_element(self, *locator, timeout=10):
        """
        指定されたロケータで要素を探し、見つかった要素を返します。
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"要素が見つかりませんでした: {locator}")
            return None

    def click(self, *locator, timeout=10):
        """
        指定されたロケータの要素をクリックします。
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            print(f"クリックする要素が見つかりませんでした: {locator}")

    def input_text(self, text, *locator, timeout=10):
        """
        指定されたロケータの要素にテキストを入力します。
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            element.clear()  # 既存のテキストをクリアする
            element.send_keys(text)
        except TimeoutException:
            print(f"テキストを入力する要素が見つかりませんでした: {locator}")

    def take_screenshot(self, file_path):
        """
        現在の画面のスクリーンショットを指定されたファイルパスに保存します。
        """
        try:
            # ページ全体のスクリーンショットを取得するために、ページサイズに合わせてウィンドウをリサイズ
            # original_size = self.driver.get_window_size()
            # required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
            # required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
            # self.driver.set_window_size(required_width, required_height)

            self.driver.save_screenshot(file_path)
            print(f"スクリーンショットを保存しました: {file_path}")

            # 元のウィンドウサイズに戻す
            # self.driver.set_window_size(original_size['width'], original_size['height'])
        except Exception as e:
            print(f"スクリーンショットの保存に失敗しました: {e}")