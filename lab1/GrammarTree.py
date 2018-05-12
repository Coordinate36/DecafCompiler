class GrammarTree(object):

    def __init__(self, name, lineno, childs, value=None):
        self.name = name
        self.value = value
        self.lineno = lineno
        self.childs = childs

    def traverse(self, level=0):
        print('  ' * level, self.name, end='')
        if self.value:
            print(':', self.value)
        else:
            print(' ({0})'.format(self.lineno))
        for node in self.childs:
            node.traverse(level + 1)
