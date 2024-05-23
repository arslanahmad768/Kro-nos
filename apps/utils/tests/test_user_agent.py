from django.test import TestCase

from ..user_agent import UserAgent


class TestUserAgent(TestCase):
    def test_parse_windows_browsers(self):
        ua_windows = [
            {
                'string': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
                'os_name': 'Windows',
                'os_version': (10,),
                'client_name': 'Edge',
                'client_version': (12, 246),
            },
            {
                'string': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                'os_name': 'Windows',
                'os_version': (7,),
                'client_name': 'Firefox',
                'client_version': (40, 1),
            },
            {
                'string': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                'os_name': 'Windows',
                'os_version': (7,),
                'client_name': 'Chrome',
                'client_version': (41, 0, 2228),
            },
            {
                'string': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
                'os_name': 'Windows',
                'os_version': (7,),
                'client_name': 'IE',
                'client_version': (11, 0),
            },
        ]

        for user_agent in ua_windows:
            parsed = UserAgent(user_agent['string'])
            self.assertEqual(user_agent['os_name'], parsed.os.family)
            self.assertEqual(user_agent['os_version'], parsed.os.version)
            self.assertEqual(user_agent['client_name'], parsed.browser.family)
            self.assertEqual(user_agent['client_version'], parsed.browser.version)

    def test_parse_macos_browsers(self):
        ua_macos = [
            {
                'string': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
                'os_name': 'Mac OS X',
                'os_version': (10, 10, 1),
                'client_name': 'Chrome',
                'client_version': (41, 0, 2227),
            },
            {
                'string': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
                'os_name': 'Mac OS X',
                'os_version': (10, 10),
                'client_name': 'Firefox',
                'client_version': (33, 0),
            },
            {
                'string': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
                'os_name': 'Mac OS X',
                'os_version': (10, 9, 3),
                'client_name': 'Safari',
                'client_version': (7, 0, 3),
            },
        ]

        for user_agent in ua_macos:
            parsed = UserAgent(user_agent['string'])
            self.assertEqual(user_agent['os_name'], parsed.os.family)
            self.assertEqual(user_agent['os_version'], parsed.os.version)
            self.assertEqual(user_agent['client_name'], parsed.browser.family)
            self.assertEqual(user_agent['client_version'], parsed.browser.version)

    def test_parse_linux_browsers(self):
        ua_macos = [
            {
                'string': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                'os_name': 'Linux',
                'os_version': (),
                'client_name': 'Chrome',
                'client_version': (41, 0, 2227),
            },
            {
                'string': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
                'os_name': 'Linux',
                'os_version': (),
                'client_name': 'Firefox',
                'client_version': (31, 0),
            },
        ]
        for user_agent in ua_macos:
            parsed = UserAgent(user_agent['string'])
            self.assertEqual(user_agent['os_name'], parsed.os.family)
            self.assertEqual(user_agent['os_version'], parsed.os.version)
            self.assertEqual(user_agent['client_name'], parsed.browser.family)
            self.assertEqual(user_agent['client_version'], parsed.browser.version)
