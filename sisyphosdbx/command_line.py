#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:51:32 2018

@author: samschott
"""

import sys

# generate sys.argv dictionary
if len(sys.argv) > 1:
    parameters = sys.argv[2:]
    wtd = sys.argv[1]
else:
    wtd = "--sync"

if wtd == "--client":
    from sisyphosdbx.client import SisyphosClient

    print("""Sisyphos DBX
(c) Sam Schott, 2018
made with Dropbox SDK from https://www.dropbox.com/developers/reference/sdk \n""")
    client = SisyphosClient()

    if parameters[0] == 'get':
        client.download(parameters[1], parameters[2])
    elif parameters[0] == 'put':
        client.upload(parameters[1], parameters[2])
    elif parameters[0] == 'mv':
        client.move(parameters[1], parameters[2])
    elif parameters[0] == 'rm':
        client.remove(parameters[1])
    elif parameters[0] == 'ls':
        res = client.list_folder(parameters[1], recursive=False)
        print('\t'.join(res.keys()))
    elif parameters[0] == 'mkdir':
        client.make_dir(parameters[1])
    elif parameters[0] == 'uid':
        res = client.get_account_info()
        print("%s, %s" % (res.email, res.account_type))

elif wtd == "--help":
    print("""
Syntax: orphilia [OPTION] [PARAMETERS]

 --help          - displays this text
 --sync          - keeps local folder in sync with Dropbox
 --configuration - runs configuration wizard
 --client        - runs SisyphosDBX API Client
   syntax: orphilia --client [parameter1] [parameter2] [parameter3]
    get   [from path] [to path] - downloads file
    put   [from path] [to path] - uploads file
    mv    [from path] [to path] - moves and renames file
    rm    [path]                - removes a file
    ls    [path]                - creates a list of files in directory
    mkdir [path]                - creates a directory
    uid   [path]                - gets current accounts Dropbox UID""")

elif wtd == "--configuration":
    from sisyphosdbx import SisyphosDBX

    sdbx = SisyphosDBX(run=False)
    sdbx.set_dropbox_directory()
    sdbx.select_excluded_folders()

elif wtd == "--sync":
    from sisyphosdbx import SisyphosDBX
    sdbx = SisyphosDBX()

else:
    print("Invalid syntax. Type orphilia --help for more informations")
