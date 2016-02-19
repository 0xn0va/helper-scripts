#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv 

with open('arabisafe.csv', 'rb') as myfile:
	obj = csv.reader(myfile)
	for row in obj:
		print """    
         <dict>
                    <key>test</key>
                    <string>
                    </string>
                    <key>شماره پاراگراف</key>
                    <string>%s</string>
                    <key>متن پاراگراف</key>
                    <string>&quot;
                            %s
         		   			&quot;
                    </string>
                    <key>شماره صوت پاراگراف</key>
                    <string>%s</string>
                    <key>شماره بخش پاراگراف</key>
                    <string>%s</string>
        </dict>   
        """ % (row[1], row[0], row[2], row[3])
