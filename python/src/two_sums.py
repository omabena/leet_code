class ListNode(object): 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next

    def print_list(self):
        def print_h(list_node):
            if list_node is not None:
                print(list_node.val)
                return print_h(list_node.next)
            else:
                return
        
        print_h(self)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_r = self.reverse_list(l1, '')
        l2_r = self.reverse_list(l2, '')
        lr = self.convert_to_list_node(l1_r + l2_r)
        lr.print_list()
        return lr

    def convert_array_to_list_node(self, array_list, list_node = None):
        if len(array_list) == 0:
            return list_node
        return self.convert_array_to_list_node(array_list[1:], ListNode(array_list[1], list_node))


    def reverse_list(self, l_node, reverse):
        if l_node.next is None:
            return int(str(l_node.val) + reverse)
        return self.reverse_list(l_node.next, str(l_node.val) + reverse )
    
        
    def convert_to_list_node(self, valor):
        def convert_h(valor, list_node):
            if len(valor) == 0:
                return list_node
            else:
                return convert_h(valor[:-1], ListNode(valor[-1], list_node))
        return convert_h(str(valor)[:-1], ListNode(str(valor)[-1], None))


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
s.addTwoNumbers(l1, l2)