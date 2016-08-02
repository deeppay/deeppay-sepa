#!/usr/bin/python

from os import listdir
from os.path import isfile, join

l = listdir("svg/")

l.sort()
d={}
for f in l:
	if f.endswith(".svg"):
		s = f.split(".")
		mtype = s[0]
		subtype = s[1]
		minor = s[2]
		version = s[3]
		#print("%s/%s/%s/%s"% (mtype, subtype, minor, version))
		if (not mtype in d):
			d[mtype] = {}
		if (not subtype in d[mtype]):
			d[mtype][subtype] = {}
		if (not minor in d[mtype][subtype]):
			d[mtype][subtype][minor] = []
		
		d[mtype][subtype][minor].append(version)
print("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>deepPay ISO20022 XSD's svg-representation </title>
	<link rel="icon" type="image/x-icon" href="img/favicon.ico" />
        <link rel="stylesheet" href="css/style.css" type="text/css" media="screen, projection">
        <script type="text/javascript" src="js/jquery-1.4.2.min.js">
        </script>
        <script type="text/javascript" src="js/scripts.js">
        </script>
        </script>
    </head>
    <body>
	<h1><img src="img/deeppay-text.png" alt="deepPay" height="32px" style="vertical-align:text-bottom;"/> ISO20022 XSD's svg-representation</h1>
        <div id="listContainer">
            <div class="listControl">
                <a id="expandList">Expand All</a>
                <a id="collapseList">Collapse All</a>
            </div>
""")
print("<ul id='expList'>")
for mtype in sorted(d.keys()):
	print("<li>%s<ul>" % (mtype))
	for subtype in sorted(d[mtype].keys()):
		maxminor = max(sorted(d[mtype][subtype].keys()))
		maxversion = max(sorted(d[mtype][subtype][maxminor]))
		print("  <li>%s.%s ( <a href='http://cdn.rawgit.com/deeppay/deeppay-sepa/master/svg/%s.%s.%s.%s.svg'>current</a> ) <ul>" % (mtype, subtype, mtype, subtype, maxminor, maxversion))
		
		for minor in sorted(d[mtype][subtype].keys()):
			#print("  %s.%s.%s" % (mtype, subtype, minor))
			for version in sorted(d[mtype][subtype][minor]):
				print("    <li><a href='http://cdn.rawgit.com/deeppay/deeppay-sepa/master/svg/%s.%s.%s.%s.svg'>%s.%s.%s.%s</a></li>" % (mtype, subtype, minor, version, mtype, subtype, minor, version))
		print("</ul></li>")
	print("</ul></li>")
print("</ul></div>")
print("</body></html>")

