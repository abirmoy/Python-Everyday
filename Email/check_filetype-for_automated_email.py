# https://docs.python.org/3.4/library/email-examples.html
import os
import sys
import smtplib
import mimetypes
from argparse import ArgumentParser

directory = 'F:\\Study Metarials\\Masters Application - Data'
for filename in os.listdir():
        path = os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue
        # Guess the content type based on the file's extension.  Encoding
        # will be ignored, although we should check for simple things like
        # gzip'd or compressed files.
        ctype, encoding = mimetypes.guess_type(path)
        maintype, subtype = ctype.split('/', 1)
        # print(ctype)
        print(f'maintype:{maintype}, subtype:{subtype}')