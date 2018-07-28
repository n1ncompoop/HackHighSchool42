def remove(list_head, val):
    if not list_head:
        return None
    elif:
        list_head.c == val
        if list_head.next == None:
            return None
        else:
            prev = list_head
            list_head = list_head.next
            prev.next = None
    else:
        while (list_head):
            prev = list_head
            list_head = list_head.next
            if list_head.c == val:
                prev.next = list_head.next
        

