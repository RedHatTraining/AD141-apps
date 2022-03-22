#!/usr/bin/env python3
url = "www.redhat.com"
result = url.startswith("www")
print(result)
print(url.endswith(".org"))
new_url = url.upper()
print("ORIGINAL", url, "RETURNED", new_url)
