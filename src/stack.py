class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = Node(None, None)

    def __str__(self):
        return

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.top.data == None:
            self.top = Node(data, None)
        else:
            self.top = Node(data, self.top)


    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        first_out = self.top.data
        if self.top.next_node == None:
            self.top = None
        else:
            self.top = Node(self.top.next_node.data, self.top.next_node.next_node)

        return first_out
