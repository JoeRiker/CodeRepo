#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:   【整理】Python中Cookie的处理：自动处理Cookie，保存为Cookie文件，从文件载入Cookie
            http://www.crifan.com/python_auto_handle_cookie_and_save_to_from_cookie_file

Version:    2013-01-15
Author:     Crifan
Contact:    admin (at) crifan.com
"""

import os;
import http.cookiejar;
import urllib3;


def pythonAutoHandleCookie():
    """
        Demo how to auto handle cookie in Python
            cookies in memory
            cookies in file:
                save cookie to file
                    LWP     format
                    Mozilla format
                load cookie from file
    """

    print("1. Demo how to auto handle cookie (in memory)")
    cookieJarInMemory = http.cookiejar.CookieJar()
    opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cookieJarInMemory))
    urllib3.install_opener(opener)
    print("after init, cookieJarInMemory=", cookieJarInMemory)  # after init, cookieJarInMemory= 
    # !!! following urllib3 will auto handle cookies
    demoUrl = "http://www.google.com/"
    response = urllib3.urlopen(demoUrl)
    # here, we already got response cookies
    print("after urllib3.urlopen, cookieJarInMemory=", cookieJarInMemory)
    # after urllib3.urlopen, cookieJarInMemory= , , ]>

    print("2. Demo how to auto handle cookie in file, LWP format")
    cookieFilenameLWP = "localCookiesLWP.txt"
    cookieJarFileLWP = http.cookiejar.LWPCookieJar(cookieFilenameLWP)
    # will create (and save to) new cookie file
    cookieJarFileLWP.save()
    opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cookieJarFileLWP))
    urllib3.install_opener(opener)
    # !!! following urllib3 will auto handle cookies
    demoUrl = "http://www.google.com/"
    response = urllib3.urlopen(demoUrl)
    # update cookies, save cookies into file
    cookieJarFileLWP.save()
    # for demo, print cookies in file
    print("LWP cookies:")
    print(open(cookieFilenameLWP).read(os.path.getsize(cookieFilenameLWP)))
    # #LWP-Cookies-2.0
    # Set-Cookie3: PREF="ID=34c1415b570a93ae:FF=0:NW=1:TM=1358236121:LM=1358236121:S=gEVVojW4x37ht5n-"; path="/"; domain=".google.com"; path_spec; domain_dot; expires="2015-01-15 07:48:41Z"; version=0
    # Set-Cookie3: NID="67=JI_uEwUm5GDrQ_vCwAp2z_YGU7MdLm5CLMa4CNLF7RQuTDMzrrk1EjRddGcnpoFbht81LaV9spxZQQInf0mPS6lDrvcRqBBL5NOTmy8SwOzA6HWC3iTIo4-o3fO1Udkv"; path="/"; domain=".google.com.hk"; path_spec; domain_dot; expires="2013-07-17 07:48:41Z"; HttpOnly=None; version=0
    # Set-Cookie3: PREF="ID=8f7e4efca89bdb1b:U=f85a4afa4db021aa:FF=2:LD=zh-CN:NW=1:TM=1358236121:LM=1358236121:S=2WR59hDWutdnUJtF"; path="/"; domain=".google.com.hk"; path_spec; domain_dot; expires="2015-01-15 07:48:41Z"; version=0

    print("3. Demo how to auto handle cookie in file, Mozilla Format")
    cookieFilenameMozilla = "localCookiesMozilla.txt"
    cookieJarFileMozilla = http.cookiejar.MozillaCookieJar(cookieFilenameMozilla)
    # will create (and save to) new cookie file
    cookieJarFileMozilla.save()
    opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cookieJarFileMozilla))
    urllib3.install_opener(opener)
    # !!! following urllib3 will auto handle cookies
    demoUrl = "http://www.google.com/"
    response = urllib3.urlopen(demoUrl)
    # update cookies, save cookies into file
    cookieJarFileMozilla.save()
    # for demo, print cookies in file
    print("Mozilla cookies:")
    print(open(cookieFilenameMozilla).read(os.path.getsize(cookieFilenameMozilla)))
    # # Netscape HTTP Cookie File
    # # http://www.netscape.com/newsref/std/cookie_spec.html
    # # This is a generated file!  Do not edit.

    # .google.com   TRUE    /   FALSE   1421308121  PREF    ID=0e05040dd979207c:FF=0:NW=1:TM=1358236121:LM=1358236121:S=jcFid2XgXMIhPUPl
    # .google.com.hk    TRUE    /   FALSE   1374047321  NID 67=klMI_Z5ZPWDjUYrWSUHIE_kYI77_ziJaL0kWRoUGThagME86LKY7H-MNa2wAMI_GklIwYcD8t82qPinxzLd4GLDbmWT0OVLCXhRj0wQDC57dTNAsTs4lhVR7Yjvj2tfn
    # .google.com.hk    TRUE    /   FALSE   1421308121  PREF    ID=028f8b736db06a9a:U=6ba6d080847c8de6:FF=2:LD=zh-CN:NW=1:TM=1358236121:LM=1358236121:S=_1BcC5v3G0ZojVz8

    print("4. read cookies from file")
    parseAndSavedCookieFile = "parsedAndSavedCookies.txt"
    parsedCookieJarFile = http.cookiejar.MozillaCookieJar(parseAndSavedCookieFile)
    # parsedCookieJarFile = cookielib.MozillaCookieJar(cookieFilenameMozilla);
    print(parsedCookieJarFile)
    parsedCookieJarFile.load(cookieFilenameMozilla)
    print(parsedCookieJarFile)  # , , ]>


if __name__ == "__main__":
    pythonAutoHandleCookie()
