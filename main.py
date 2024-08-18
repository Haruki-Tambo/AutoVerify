import unittest

if __name__ == "__main__":
    # 'tests' ディレクトリ内のテストを自動的に検出して実行する
    unittest.defaultTestLoader.discover('tests')
    runner = unittest.TextTestRunner()
    runner.run(suite)