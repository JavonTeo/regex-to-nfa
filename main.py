from graph import Graph

def parse(r, idx):
    idx, node = parse_split(r, idx)
    if idx != len(r):
        # parsing stopped at a bad ")"
        raise Exception('unexpected ")"')
    return node
    
def parse_split(r, idx):
    idx, prev = parse_concat(r, idx)
    while idx < len(r):
        if r[idx] == ')':
            # return to the outer parse_node
            break
        assert r[idx] == '|', 'BUG'
        idx, node = parse_concat(r, idx+1)
        prev = ('split', prev, node)
    return idx, prev

def parse_concat(r, idx):
    prev = None
    while idx < len(r):
        if r[idx] in '|)':
            break
        idx, node = parse_node(r, idx)
        if prev is None:
            prev = node
        else:
            prev = ('cat', prev, node)
    return idx, prev

def parse_node(r, idx):
    ch = r[idx]
    idx += 1
    assert ch not in '|)'
    if ch == '(':
        idx, node = parse_split(r, idx)
        if idx < len(r) and r[idx] == ')':
            idx += 1
        else:
            raise Exception('unbalanced paranthesis')
    elif ch == '.':
        node = 'dot'
    elif ch in '*+':
        raise Exception('nothing to repeat')
    else:
        node = ch
    
    idx, node = parse_repeat(r, idx, node)
    return idx, node

def parse_repeat(r, idx, node):
    if idx == len(r) or r[idx] not in '*+':
        return idx, node
    
    ch = r[idx]
    idx += 1
    if ch == '*':
        rmin, rmax = 0, float('inf')
    elif ch == '+':
        rmin, rmax = 1, float('inf')
    
    #sanity checks
    if rmax < rmin:
        raise Exception('min repeat is less than max repeat')
    
    node = ('repeat', node, rmin, rmax)
    return idx, node

if __name__ == "__main__":
    regex = input("Please input a regular expression: ")
    parsed_res = parse(regex, 0)
    print("Here is the parsed result:")
    print(parsed_res)
    graph = Graph(parsed_res)
    graph.show_dfa()
