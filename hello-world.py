#!/usr/bin/env python

import os

def main():

    path = '/etc/custom_scripts/foo_bar.config'
    fl = open(path, 'r')
    data = fl.read()
    fl.close()
    print data

    print 'Hello world!'


if __name__ == "__main__":
    main()
