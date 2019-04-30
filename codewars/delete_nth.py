def delete_nth(order,max_e):
    # code here
    usage = dict()
    filtered = []
    for el in order:
        if not el in usage:
            filtered.append(el)
            usage.update({el : 1})
        else:
            usage.update({el: (usage.get(el) + 1)})
            if usage.get(el) <= max_e:
                filtered.append(el)
    
    return filtered