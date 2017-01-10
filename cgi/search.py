import os, json
import cgi, cgitb
cgitb.enable()
print("Content-type:text/html\n")

indexDir = 'support/index'

html_section1 = '''
<html>
<head>
    <title>Search By Tags</title>
    <link rel="stylesheet" type="text/css" href="/support/style/dropdown.css" />
    <link rel="stylesheet" type="text/css" href="/support/style/input.css" />
    <script type="text/javascript" src="/support/script/tag_onclick.js"></script>
</head>
<body>
    <form method=GET action="results.py">
        <input type="text" id="query" name="query" />
        <input type="submit" id="submit" value="Search" />
    </form>
    <div class="dropdown" style="top:-1em">
        <a class="dropbtn">Add a Tag</a>
        <ul>
'''

html_menu = ''

html_section2 = '''
        </ul>
    </div>
</body>
</html>
'''

f = open(os.path.join(indexDir, 'invertedIndex'), 'r')
invertedIndex = json.load(f)
f.close()

for tagsNamespace in invertedIndex.keys():
    html_menu += '<li><a>{}</a><ul>\n'.format(cgi.escape(tagsNamespace))
    for tag in invertedIndex[tagsNamespace].keys():
        html_menu += '<li><a href="#" id="<{}|{}>" onclick="tag_onclick(this.id); return false;">{}</a></li>\n'.format(tagsNamespace, tag, cgi.escape(tag))
    html_menu += '</ul></li>\n'

print(html_section1 + html_menu + html_section2)
