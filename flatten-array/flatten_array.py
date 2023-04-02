def flatten(iterable):

    flat_pack = []
    for item in iterable:
        if item is None:
            next
        elif isinstance(item, list):
            flat_pack.extend(flatten(item))
        else:
            flat_pack.append(item)

    return flat_pack
