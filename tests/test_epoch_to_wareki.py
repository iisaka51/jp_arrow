import os
import sys
import locale
sys.path.insert(0,"../jp_arrow")
import jp_arrow

class TestClass:
    def test_case01(self):
        data = '1962-01-13'
        format = 'EEYYYY年MM月DD日'
        expect = '昭和37年01月13日'
        result = jp_arrow.get(data).format(format)
        assert result == expect

    def test_case02(self):
        data = '1962-01-13'
        format = 'EEYYYYMMMMDD'
        expect = '昭和37年1月13日'
        result = jp_arrow.get(data).format(format, locale='ja')
        assert result == expect

    def test_case03(self):
        data = '2024-01-13'
        format = 'EEYYYY年MM月DD日'
        expect = '令和06年01月13日'
        result = jp_arrow.get(data).format(format)
        assert result == expect

    def test_case04(self):
        data = '平成36年01月13日'
        format = 'YYYY年MM月DD日'
        expect = '2024年01月13日'
        result = jp_arrow.get(data).format(format)

    def test_case05(self):
        data = '1962-01-13'
        format = jp_arrow.FORMAT_JISX0301
        expect = 'S37.1.13'
        result = jp_arrow.get(data).format(format)
        assert result == expect

    def test_case06(self):
        data = '1962-01-13'
        format = jp_arrow.FORMAT_JISX0301_W
        expect = 'S37.01.13'
        result = jp_arrow.get(data).format(format)
        assert result == expect

    def test_case07(self):
        data = '1962-01-13'
        format = jp_arrow.FORMAT_WAREKI
        expect = '昭和37年1月13日'
        result = jp_arrow.get(data).format(format)
        assert result == expect

    def test_case08(self):
        data = '1962-01-13'
        format = jp_arrow.FORMAT_WAREKI_W
        expect = '昭和37年01月13日'
        result = jp_arrow.get(data).format(format)
        assert result == expect

