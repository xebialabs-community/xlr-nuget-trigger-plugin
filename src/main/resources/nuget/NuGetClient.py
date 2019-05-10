#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


import sys
import urllib
import com.xhaus.jyson.JysonCodec as json
from xlrelease.HttpRequest import HttpRequest
from distutils.version import LooseVersion

SUCCES_RESULT_STATUS   = 200
RECORD_CREATED_STATUS  = 201

class NuGetClient(object):
    def __init__(self, httpConnection, apiKey, username="", password=""):
        self.headers        = {"X-NuGet-ApiKey": apiKey}
        self.query_params   = ""
        self.httpConnection = httpConnection
        self.httpConnection['username'] = username
        self.httpConnection['password'] = password
        self.httpRequest = HttpRequest(self.httpConnection, username, password)

    @staticmethod
    def create_client(httpConnection, apiKey, username="", password=""):
        return NuGetClient(httpConnection, apiKey, username, password)

    def get_latest_version(self, package_id):
        api_url = '/api/v2/package-versions/%s?semVerLevel=2.0.0&includePrerelease=false' % (package_id)
        response = self.httpRequest.get(api_url, contentType='application/json', headers = self.headers)

        if response.getStatus() == SUCCES_RESULT_STATUS:
            versions_list = json.loads(response.getResponse())
            #print("Versions founds: %s" % str(versions_list))

            # there may be a 'latest' but that's not helpful to us to see if there's a new version 
            if "latest" in versions_list:
                versions_list.remove("latest")
            # End if

            try:
                versions_list.sort(key=LooseVersion)
                #print("Tags sorted %s" % str(versions_list))
            except Exception, e:
                print("Failed to sort, ignoring: %s " % str(e))
            # End try

            if len(versions_list) > 0:
                return versions_list[-1]
            else:
                return None
        else:
            print("get_latest_version error %s" % (response))
            self.throw_error(response)
        # End if
    # End get_latest_version


    def throw_error(self, response):
        print("Error from NuGet server, HTTP Return: %s\n" % (response.getStatus()))
        print("Detailed error: %s\n" % response.response)
        sys.exit(1)

