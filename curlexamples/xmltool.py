#!/usr/bin/env python

"""
Example usage:

    $ cat tmp.xml | xmltool.py

"""
import re
import sys
import xml.dom.minidom


s = sys.stdin.read()
s = xml.dom.minidom.parseString(s).toprettyxml(indent='  ')
regex = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
print regex.sub('>\g<1></', s)
