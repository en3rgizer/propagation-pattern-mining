class node2:
    label = ''
    parent = ''
    childs = []
    color = 'w'
    def __init__(self, label, parent, cSet, color='w'):
        self.label  = label
        self.parent = parent
        self.childs = cSet
        self.color  = color  #w: not-visited, 'g': visited but not finished, 'b': finished