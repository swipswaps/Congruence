from ccli.treeview import ConfluenceTree
from ccli.interface import HOST
from ccli.confluence.changes import get_changes
from ccli.confluence.spaces import get_spaces
from ccli.confluence.microblog import get_microblog


def main():
    changes = get_changes()
    #  print(changes)
    #  exit(0)
    microblog = get_microblog()
    spaces = get_spaces()

    content = {
        "name": "Confluence (%s)" % HOST,
        "children": [
            {
                "name": "Latest changes",
                "children": changes,
            },
            {
                "name": "Microblog",
                "children": microblog,
            },
            {
                "name": "Spaces",
                "children": spaces,
            },
        ]
    }
    ConfluenceTree(content).main()
