#!/usr/bin/python3
"""
A script that:
    - fetches https://alx-intranet.hbtn.io/status.
    - uses urllib package.
    """

    import urllib.request
    import urllib.error

    if __name__ == '__main__':
            try:
                        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
                                        content = res.read()
                                                    print("Body response:")
                                                                print("\t- type: {}".format(type(content)))
                                                                            print("\t- content: {}".format(content))
                                                                                        print("\t- utf8 content: {}".format(content.decode('utf-8')))
                                                                                            except urllib.error.URLError as e:
                                                                                                        print("URLError:", e)
                                                                                                            except urllib.error.HTTPError as e:
                                                                                                                        print("HTTPErroor:", e)
