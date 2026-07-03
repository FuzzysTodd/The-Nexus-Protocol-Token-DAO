from _typeshed import Incomplete

class Tree:
    node_id: Incomplete
    children: Incomplete
    data: Incomplete
    props: Incomplete
    edge_data: Incomplete
    edge_props: Incomplete
    index: Incomplete
    def __init__(self, node_id, children: Incomplete | None = None, data: Incomplete | None = None, props: Incomplete | None = None, edge_data: Incomplete | None = None, edge_props: Incomplete | None = None) -> None:
        """
        A class to facilitate tree manipulation in Cytoscape.
        :param node_id: The ID of this tree, passed to the node data dict
        :param children: The children of this tree, also Tree objects
        :param data: Dictionary passed to this tree's node data dict
        :param props: Dictionary passed to this tree's node dict, containing the node's props
        :param edge_data: Dictionary passed to the data dict of the edge connecting this tree to its
        parent
        :param edge_props: Dictionary passed to the dict of the edge connecting this tree to its
        parent
        """
    def is_leaf(self):
        """
        :return: If the Tree is a leaf or not
        """
    def add_children(self, children) -> None:
        """
        Add one or more children to the current children of a Tree.
        :param children: List of Tree objects (one object or more)
        """
    def get_edges(self):
        """
        Get all the edges of the tree in Cytoscape JSON format.
        :return: List of dictionaries, each specifying an edge
        """
    def get_nodes(self):
        """
        Get all the nodes of the tree in Cytoscape JSON format.
        :return: List of dictionaries, each specifying a node
        """
    def get_elements(self):
        """
        Get all the elements of the tree in Cytoscape JSON format.
        :return: List of dictionaries, each specifying an element
        """
    def find_by_id(self, search_id, method: str = 'bfs'):
        '''
        Find a Tree object by its ID.
        :param search_id: the queried ID
        :param method: Which traversal method to use. Either "bfs" or "dfs"
        :return: Tree object if found, None otherwise
        '''
    def create_index(self):
        """
        Generate the index of a Tree, and set it in place. If there was a previous index, it is
        erased. This uses a BFS traversal. Please note that when a child is added to the tree,
        the index is not regenerated. Furthermore, an index assigned to a parent cannot be
        accessed by its children, and vice-versa.
        :return: Dictionary mapping node_id to Tree object
        """
