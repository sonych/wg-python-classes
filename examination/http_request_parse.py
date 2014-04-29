# coding: utf-8

import re
import unittest


class HttpRequest(object):

    def __init__(self, method, url, http_version, headers=None):
        self.method = method
        self.url = url
        self.http_version = http_version
        self.headers = headers or {}


def parse_request(request_str):

    method_and_resource, raw_heaers = request_str.split('\n', 1)

    pattern = r'(?P<method>GET|POST|HEAD) (?P<url>(\/?[\w\?\.\=\&\-\#\+\/]+)) HTTP\/(?P<http_version>1.0|1.1)'
    result = re.match(pattern, method_and_resource)
    d = result.groupdict()

    request = HttpRequest(d['method'], d['url'], d['http_version'])

    headers = dict(re.findall(r"\s*(?P<name>.*?)\s*:\s*(?P<value>.*?)\s*\n", raw_heaers))
    request.headers = headers

    return request


class HttpRequestParserTest(unittest.TestCase):

    def test_one(self):
        request_str = """GET /2/library/re.html HTTP/1.1
            Accept       :  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
         Accept-Encoding      : gzip, deflate
          Accept-Language  : en-US,en;q=0.5
        Cache-Control:   max-age=0
        Connection:  keep-alive
        Host:    docs.python.org
        If-Modified-Since:   Mon, 28 Apr 2014 22:18:44 GMT
        User-Agent:  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0
        """

        request = parse_request(request_str)

        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.url, '/2/library/re.html')
        self.assertEqual(request.http_version, '1.1')
        self.assertEqual(request.headers['Accept'], 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        self.assertEqual(request.headers['Host'], 'docs.python.org')
        self.assertEqual(request.headers['Accept-Encoding'], 'gzip, deflate')


if __name__ == '__main__':
    unittest.main()

