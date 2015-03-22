__author__ = 'lotso'


# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64

from ConfigParser import SafeConfigParser, NoSectionError

# Start your middleware class


class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):

        parser = SafeConfigParser()
        parser.read('config.ini')
        try:
            proxyurl = parser.get('proxy_settings', 'proxyurl')
            username = parser.get('proxy_settings', 'username')
            password = parser.get('proxy_settings', 'password')
            # Set the location of the proxy

            request.meta['proxy'] = proxyurl

            # Use the following lines if your proxy requires authentication
            proxy_user_pass = username + ":" + password
            # setup basic authentication for the proxy
            encoded_user_pass = base64.encodestring(proxy_user_pass)
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        except NoSectionError, e:
            pass