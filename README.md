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

A tags file can have these sections: *title*, *images*, *descriptions* and *tags*. All sections are ended by a line starts with lesser than sign (<) or end of file.

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

Hover over *Add a Tag*
