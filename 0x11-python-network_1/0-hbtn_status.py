#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request
import urllib.error

if __name__ == "__main__":
        url = "https://alx-intranet.hbtn.io/status"
            try:
                        req = urllib.request.Request(url)
                                with urllib.request.urlopen(req) as response:
                                                html = response.read()
                                                            print("Body response:")
                                                                        print("\t- type: {}".format(type(html)))
                                                                                    print("\t- content: {}".format(html))
                                                                                                print("\t- utf8 content: {}".format(html.decode('utf-8')))
                                                                                                    except urllib.error.URLError as e:
                                                                                                                print("Error fetching URL:", e)
                                                                                                                    except urllib.error.HTTPError as e:
                                                                                                                                print("HTTP Error:", e)

