# SearchByTags

Search local directories by tags. Has a web UI for search.

Many things can be put into more than one category. So I decide to manage my directories by tags.

## Prerequisites

You will need Python 3 to run python scripts, and a web browser to view web pages.

## Usage

Copy all the content except *example* directory to a top directory.\* Create a text file named *tags.txt*\*\* in every directory that should be searched under the top directory.

\* You can also change the top directory by changing *contentDir* variable in *build_index.py*. However, if the top directory is not under the web directory (where *webserver.py* is), or you use an absolute path, the images won't be shown correctly on web pages.

\*\* You can use other name by changing *tagsFileName* variable in *build_index.py*.

### Format of Tags File
