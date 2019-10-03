# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):

    if i == 0 and j == 0:
        value = True
        ind = 0
    elif i == 0:
        value = False
        ind = -1
    else:
        if T.get(i-1, j).value == True:
            value = True
            ind = T.get(i-1, j).index
        else:
            word = string[i-1:j]
            if is_word(word):
                if T.get(i, j - len(word)).value == True:
                    value = True
                    ind = i
                else:
                    value = False
                    ind = -1
            else:
                value = False
                ind = -1
        
    return RespaceTableCell(value, ind)
                  
# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):

    rows = [x for x in range(N+1)] * (N+1)
    cols = [x for y in [[x]*(N+1) for x in range(N+1)] for x in y]
    return list(zip(rows, cols))

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):

    N = len(s)
    res = ''
    while N > 0:
        cell = table.get(N, N)
        ind = cell.index
        if ind == -1:
            return None
        nextword = s[ind-1:N]
        if N == len(s):
            res = nextword
        else:
            res = nextword + ' ' + res
        N = ind - 1
    return res

if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    s = "itwasthebestoftimes"
    wordlist = ["of", "it", "the", "best", "times", "was"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print respace_from_table(s, D)
