def devuelvePosiciones(palabra, letra):
    pos = []
    for idx, val in enumerate(palabra):
        if val == letra:
            pos.append(idx)
    if len(pos) == 0:
        return ''
    return pos
