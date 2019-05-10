#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys, string, time, traceback
import com.xhaus.jyson.JysonCodec as json
from nuget.NuGetClient import NuGetClient

if server is None:
    sys.exit("No server provided.")

if packageId is None:
    sys.exit("No packageId provided.")

if not apiKey:
    apiKey = server["apiKey"]

client = NuGetClient.create_client(server, apiKey, "", "")

try:
    latest_version = client.get_latest_version( packageId )

    triggerState = latest_version
    packageVersion = triggerState

    print("Setting packge [%s] to triggerState/packageVersion [%s]" % (packageId, triggerState))

except Exception, e:
    sys.exit("Failed to find package in NuGet server: [%s]" % str(e))
