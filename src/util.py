def isStraight(positions):
    return all([positions[0][0] == pos[0] for pos in positions]) or all([positions[0][1] == pos[1] for pos in positions])

def isCoherent(positions):
    xs = sorted([x for (x,y) in positions])
    ys = sorted([y for (x,y) in positions])

    return xs == range(xs[0], xs[-1]+1) or ys == range(ys[0], ys[-1]+1)

