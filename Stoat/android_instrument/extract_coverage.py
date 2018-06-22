import re


reg = re.compile("<td>Total</td><td class=\"bar\">(.*?) of .*?</td><td class=\"ctr2\">(.*?)%</td>")
with open(argv[1], 'r') as target:
	html = target.read()
	matches = reg.search(html)
	cov_line = matches[1]
	cov_percent = matches[2]

print cov_line + ' ' + cov_percent