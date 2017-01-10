import os, json, subprocess
import cgi, cgitb
cgitb.enable()
print("Content-type:text/html\n")

indexDir = 'support/index'

html_section1 = '''
<html>
<head>
    <title>{}</title>
    <link rel="stylesheet" type="text/css" href="/support/style/preview.css" />
</head>
<body>
    <div class="preview">
        <table>
'''

html_table_content = ''

html_section2 = '''
        </table>
    </div>
</body>
</html>
'''

html_invalid = '''
<html>
<head>
    <title>Invalid ID</title>
</head>
<body>
    <h1>Invalid ID</h1>
</body>
</html>
'''

form = cgi.FieldStorage()
if 'id' in form:
    try:
        ID = int(form['id'].value)
        f = open(os.path.join(indexDir, 'infoList'), 'r')
        infoList = json.load(f)
        f.close()
        f = open(os.path.join(indexDir, 'forwardIndex'), 'r')
        forwardIndex = json.load(f)
        f.close()
        info = infoList[ID]
        tags = forwardIndex[ID]
    except:
        print(html_invalid)
    
    html_table_content += '<tr><th>{}</th></tr>\n'.format(cgi.escape(info['title']))
    
    html_table_content += '<tr><td>\n'
    for image in info['images']:
        html_table_content += '<img src="/{}" />\n'.format(image)
    html_table_content += '</td></tr>\n'
    
    html_table_content += '<tr><td>{}</td></tr>\n'.format(cgi.escape(os.path.abspath(info['path'])))
    
    html_table_content += '<tr><td>\n'
    for d in info['descriptions']:
        html_table_content += '{}<br />\n'.format(cgi.escape(d))
    html_table_content += '</td></tr>\n'
    
    for tagsNamespace in tags.keys():
        html_table_content += '<tr><th>{}</th></tr>\n<tr><td>\n'.format(cgi.escape(tagsNamespace))
        for tag in tags[tagsNamespace]:
            html_table_content += '{}&nbsp;\n'.format(cgi.escape(tag))
        html_table_content += '</td></tr>\n'
    
    print(html_section1.format(cgi.escape(info['title'])) + html_table_content + html_section2)
    #if you want this server-side script to open the directory in windows explorer, uncomment the following line:
    #subprocess.Popen(r'explorer "{}"'.format(os.path.abspath(info['path'])))
else:
    print(html_invalid)
