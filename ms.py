# coding=utf8
p,q,n = [int(x) for x in raw_input().split()]

class TreeNode(object):
    def __init__(self, val = '#', left = None, right = None, t_deep = 0, node_pro = 1, t_mark =0, all_p = 1):
        self.data = val
        self.l_child = left
        self.r_child = right
        self.t_deep = t_deep
        self.node_pro = node_pro
        self.t_mark = t_mark
        self.all_p = all_p


class Tree(TreeNode):
    # create a tree
    def create_tree(self, tree, deep, node_pro, num, t_mark, all_p, out_list = 0.0):
        deep += 1
        if num > n:
            tree = None
        elif num == n:
            tree.data = num
            tree.l_child = TreeNode(t_mark=1)
            tree.r_child = TreeNode(t_mark=0)
            tree.t_deep = deep
            tree.node_pro = node_pro
            tree.t_mark = t_mark
            tree.all_p = all_p
            return all_p*(deep-1)
        else:
            if t_mark == -1:
                left_p = p
            elif t_mark == 0:
                left_p = 100 if node_pro + q>100 else node_pro+q # node_pro + q
            else:
                left_p = int(p/2)
            tree.data = num
            tree.l_child = TreeNode(t_mark=1)
            out_list += self.create_tree(tree.l_child, deep, left_p, num+1, 1, all_p=all_p*(float(left_p)/100))
            tree.r_child = TreeNode(t_mark=0)
            if 100 - left_p > 0:
                out_list += self.create_tree(tree.r_child, deep, 100 - left_p, num, 0, all_p=all_p*(float(100 - left_p)/100))
            tree.t_deep = deep
            tree.node_pro = node_pro
            tree.t_mark = t_mark
            tree.all_p = all_p
        return out_list

    # visit a tree node
    def visit(self, tree, p_a):
        # 输入#号代表空树
        if tree.data == n:
            print tree.data


    # 先序遍历
    def pre_order(self, tree, out = 0.0):
        if tree is not None:
            self.visit(tree, out)
            self.pre_order(tree.l_child, out)
            self.pre_order(tree.r_child, out)


t = TreeNode()
tree = Tree()
out_list = tree.create_tree(tree=t, deep=0, node_pro=p, num=0, t_mark=-1, all_p = 1, out_list = 0.0)
print out_list