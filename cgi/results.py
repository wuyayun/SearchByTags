import os, sys, json
sys.path.append('support')
import query_index
import cgi, cgitb
cgitb.enable()
print("Content-type:text/html\n")

indexDir = 'support/index'

html_section1 = '''
<html>
<head>
    <title>Search Results</title>
    <link rel="stylesheet" type="text/css" href="/support/style/results.css" />
</head>
<body>
'''

html_query = ''

html_error = ''

html_section2 = '''
    <div class="results">
        <table>
'''

html_results_table = ''

html_section3 = '''
        </table>
    </div>
</body>
</html>
'''

form = cgi.FieldStorage()
query = form['query'].value if 'query' in form else ''
html_query = '<div class="query">query="{}"</div>\n'.format(cgi.escape(query))

f = open(os.path.join(indexDir, 'infoList'), 'r')
infoList = json.load(f)
f.close()
f = open(os.path.join(indexDir, 'invertedIndex'), 'r')
invertedIndex = json.load(f)
f.close()

i = query_index.queryIndex()
i.loadIndex(len(infoList), invertedIndex)
results = i.startQuery(query)

html_error = '<div class="error">\n'
for e in i.errorOutput:
    html_error += '{}<br />\n'.format(cgi.escape(e))
html_error += '</div>\n'

for r in results:
    if infoList[r]['images']:
        image = infoList[r]['images'][0]
    else:
        image = ''
    html_results_table += '<tr><th rowspan="3"><img src="/{}" /></th>\n'.format(image)
    html_results_table += '<td><a href="preview.py?id={}">{}</a></td></tr>\n'.format(r, cgi.escape(infoList[r]['title']))
    html_results_table += '<tr><td>{}</td></tr>\n'.format(cgi.escape(os.path.abspath(infoList[r]['path'])))
    html_results_table += '<tr><td>\n'
    for d in infoList[r]['descriptions']:
        html_results_table += '{}<br />\n'.format(cgi.escape(d))
    html_results_table += '</td></tr>\n'

print(html_section1 + html_query + html_error + html_section2 + html_results_table + html_section3)
