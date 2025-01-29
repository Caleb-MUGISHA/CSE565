def heapify(data, total_nodes, current_node):
    
    parent = current_node
    child_left = (current_node * 2) + 1
    child_right = (current_node * 2) + 2
    
    # Find the largest value among parent and children
    if child_left < total_nodes and data[child_left] > data[parent]:
        parent = child_left
        
    if child_right < total_nodes and data[child_right] > data[parent]:
        parent = child_right
        
    # If a child is larger than the parent, swap them and continue restructuring
    if parent != current_node:
        data[current_node], data[parent] = data[parent], data[current_node]
        heapify(data, total_nodes, parent)

def heapsort(data):
    
    if not isinstance(data, list):
        raise TypeError("Expected a list, got {}".format(type(data)))
        
    total_nodes = len(data)
    if total_nodes <= 1:
        return
        
    # Transform the input into a max heap structure
    # Start from last parent node and move upward
    last_parent = (total_nodes // 2) - 1
    for node in range(last_parent, -1, -1):
        heapify(data, total_nodes, node)
        
    # Extract elements from heap one by one
    for end in range(total_nodes - 1, 0, -1):
        # Move current max to the end and rebuild heap
        data[0], data[end] = data[end], data[0]
        heapify(data, end, 0)