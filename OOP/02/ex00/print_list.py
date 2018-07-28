def print_list(list_head):
    list_iter = __iter__(list_head)
    while(list_iter):
        print(list_iter)
        list_iter = next(list_iter)