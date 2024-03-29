# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

import dynamic_programming


# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"


# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    
    if i == 0 and j == 0:
        s_char = ' '
        t_char = ' '
        cost = 0
    elif i == 0:
        s_char = '-'
        t_char = t[j-1]
        cost = table.get(i, j - 1).cost + cost(s_char, t_char)
    elif j == 0:
        s_char = s[i - 1]
        t_char = '-'
        cost = table.get(i-1, j).cost + cost(s_char, t_char)
    else:
        add_s = table.get(i-1, j).cost + cost(s[i-1], '-')
        add_t = table.get(i, j-1).cost + cost('-', t[j-1])
        add_st = table.get(i-1, j-1).cost + cost(s[i-1],t[j-1])
        if add_s == min(add_s, add_t, add_st):
            s_char = s[i-1]
            t_char = '-'
            cost = add_s
        elif add_t == min(add_s, add_t, add_st):
            s_char = '-'
            t_char = t[j-1]
            cost = add_t
        else:
            s_char = s[i-1]
            t_char = t[j-1]
            cost = add_st
    return DiffingCell(s_char, t_char, cost)


# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called
def cell_ordering(n, m):
    # TODO: YOUR CODE HERE
    rows = [x for y in [[x]*(m+1) for x in range(n+1)] for x in y]
    cols = [x for x in range(m+1)] * (n+1)
    return list(zip(rows,cols))


# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    # TODO: YOUR CODE HERE
    align_s = ''
    align_t = ''
    n = len(s)
    m = len(t)
    cost = table.get(n,m).cost
    while n > 0 or m > 0:
        cell = table.get(n,m)
        align_s = cell.s_char + align_s
        align_t = cell.t_char + align_t
        if cell.s_char == '-':
            m -= 1
        elif cell.t_char == '-':
            n -= 1
        else:
            m -= 1
            n -= 1
    return (cost, align_s, align_t)


# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print align_s
    print align_t
    print "cost was %d"%cost
