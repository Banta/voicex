#!/usr/bin/python
"""
Copyright (c) 2012 Anant Bhardwaj

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

'''
Application database 

@author: Anant Bhardwaj
@date: Aug 21, 2012
'''

import psycopg2, sys


con = None

try: 
	conn = psycopg2.connect(user='postgres', password='postgres', host="localhost", dbname="trish") 
	cur = conn.cursor()
	cur.execute('CREATE TABLE posts (id serial PRIMARY KEY, phone varchar(20), post text, zipcode varchar(10));')  
	cur.execute('CREATE TABLE follow_tags (id serial PRIMARY KEY, tag varchar(20), subscription_list varchar(500));')
	conn.commit()
except psycopg2.DatabaseError, e:
	print 'Error %s' % e    
	sys.exit(1)    

finally:    
	if conn:
		conn.close()