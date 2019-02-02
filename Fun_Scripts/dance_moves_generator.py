def lead(n):  # Dance moves generator

    lead_moves = ['F inside', 'F outside', 'L inside', 'L outside', 'Hammer lock', 'lead hammer lock', 'Cuddle', 'Dip', 'Body roll', 'Drapes', 'Sugar push', 'Counter balance', 'Lunge', 'Arm flick']  # 'Salsa lead turn'?

    out = []

    for i in range(n):
        l = random.choice(lead_moves)
        out.append(l)
        lead_moves.remove(l)

    return out


def follow(n):  # Dance moves generator

    follow_moves = ['arm styling', 'foot styling', 'hip styling']

    out = []

    for i in range(n):
        l = random.choice(follow_moves)
        out.append(l)
        follow_moves.remove(l)

    return out


print('lead moves: ' + str(lead(2)) + '\nFollow move: ' + str(follow(1)))