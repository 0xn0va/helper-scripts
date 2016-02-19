#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('txtmatn.txt', 'rb') as txtmatn:
    
    print(re.findall(r'.{1,16}(?:\s+|$)', txtmatn))
	