# SearchByTags

Search local directories by tags. Has a web UI for search.

Many things can be put into more than one category. So I decide to manage my directories by tags.

## Prerequisites

You will need Python 3 to run python scripts, and a web browser to view web pages.

## Usage

Copy all the content except *example* directory to a top directory.\* Create a text file named *tags.txt*\*\* in every directory that should be searched under the top directory.

\* You can also change the top directory by changing *contentDir* variable in *build_index.py*. However, if the top directory is not under the web directory (where *webserver.py* is), or you use an absolute path, the images won't be shown correctly on web pages.

\*\* You can use other filename by changing *tagsFileName* variable in *build_index.py*.

### Format of Tags File

A tags file can have these sections: *title*, *images*, *descriptions* and *tags*. All sections are ended by a line starts with \< or end of file.

Title section starts with a line that **is** *\<title\>*. Only the last line in this section will be used as title.

Images section starts with a line that **is** *\<image\>* or *\<images\>*. It should contains relative paths to image files. If there are more than one image, all images would be shown in the preview page, but only the first one would be shown in the search results page. If an image file is not under the web directory (where *webserver.py* is), that image won't be shown correctly on web pages.

Descriptions section starts with a line that **is** *\<description\>* or *\<descriptions\>*.

Tags section starts with a line that **starts with** *\<tag\>* or *\<tags\>*. Right part of this line is the namespace of tags in this section. Following lines are tags separated by delimiter vertical bar (|) or newline.

So a tags file may look like this:

```
<title>
title
<images>
img1path
img2path
<descriptions>
description_line1
description_line2
<tags>namespace1
tag11|tag12|tag13
tag14
<tags>namespace2
tag21
```

Note: Double quote sign (") should never be used in a tags file. Vertical bar (|), lesser than sign (<) or greater than sign (>) should not be used in any namespace or any tag. Whitespaces at the beginning or the end of each line, each namespace, or each tag would be stripped.

### Build Index

Run *build_index.py* before searching if tags files were modified.

### Search

Run *webserver.py*, then go to *localhost/cgi/search.py* in a web browser.

Hover over *Add a Tag* to see a two-level dropdown menu, from which you can select tags. Click a tag to add it to the input box in format *\<namespace|tag\>*.

This program supports Boolean search. *&*, *and* or joining without operator specifies logical AND. *|* or *or* specifies logical OR. *-* or *not* specifies logical NOT. Round brackets (()) can be used to set order of operations.

So a search query may look like this:

```
<n1|t1>|<n2|t2>-(<n3|t3><n4|t4>)
```

Click *Search* button to start search using query in the input box. In search results page, click a title would go to a preview page.

If you are using Windows and want the directory to be opened automatically by the server-side script, uncomment this line in *preview.py*:

\#subprocess.Popen(r'explorer "{}"'.format(os.path.abspath(info['path'])))
