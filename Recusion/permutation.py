def permuation(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
