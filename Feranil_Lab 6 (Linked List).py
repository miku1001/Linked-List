class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(first_list, second_list):
    holder = ListNode(0)     # Create a placeholder node
    current_list = holder        # Create a pointer to iterate the merged list
    
    # Iterate both lists until one of them becomes empty
    while first_list and second_list:
        # Compare the values of the current nodes in both lists
        # If value in first list is less than or equal to value in second list
        if first_list.value <= second_list.value:
            current_list.next = first_list                # Append current node from first list to the merged list
            first_list = first_list.next             # Move the pointer in first list to the next node
        else:
            current_list.next = second_list               # Append the current node from second list to the merged list
            second_list = second_list.next           # Move the pointer in first list to the next node
        current_list = current_list.next                       # Move the pointer in the merged list to the next node
    
    if first_list:                          # Append the remaining nodes from the non-empty list to the merged list
        current_list.next = first_list
    elif second_list:
        current_list.next = second_list
    
    return holder.next                      # Return the head of the merged list (placeholder node is excluded)

# Input Values to the first and second list
first_list = ListNode(1)
first_list.next = ListNode(2)
first_list.next.next = ListNode(4)

second_list = ListNode(1)
second_list.next = ListNode(3)
second_list.next.next = ListNode(6)

merged_list = mergeTwoLists(first_list, second_list) # Using the created function, merge two lists

# Print the merged list
while merged_list:
    print(merged_list.value, end="")
    merged_list = merged_list.next
    if merged_list:
        print(" -> ", end="")
