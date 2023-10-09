# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.tree_list = []
        self.idx = 0

    def dfs_helper_seri(self, root):
        if not root:
            self.tree_list.append('N')
            return
        self.tree_list.append(str(root.val))
        self.dfs_helper_seri(root.left)
        self.dfs_helper_seri(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.dfs_helper_seri(root)
        return ",".join(self.tree_list)
        
    def dfs_helper_dese(self, val_list):
        if val_list[self.idx] == 'N':
            self.idx += 1
            return None
        node = TreeNode(int(val_list[self.idx]))
        self.idx += 1
        node.left = self.dfs_helper_dese(val_list)
        node.right = self.dfs_helper_dese(val_list)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        val_list = data.split(",")
        return self.dfs_helper_dese(val_list)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

