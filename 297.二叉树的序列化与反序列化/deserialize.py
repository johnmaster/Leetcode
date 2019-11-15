class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    queue = [root]
    s = ' '
    while queue:
        temp = queue.pop(0)
        if temp:
            s += str(temp.val)
            queue.append(temp.left)
            queue.append(temp.right)
        else:
            s += 'null'
        s += ' '
    return s


def deserialize(data):
    string = data.split()
    if string[0] == 'null':
        return []
    root = TreeNode(int(string[0]))
    queue = [root]
    i = 1
    while queue:
        temp = queue.pop(0)
        if temp is None:
            continue
        temp.left = TreeNode(int(string[i])) if string[i] != 'null' else None
        temp.right = TreeNode(int(string[i + 1])) if string[i + 1] != 'null' else None
        i += 2
        queue.append(temp.left)
        queue.append(temp.right)
    return root


class Codec:
    pass
