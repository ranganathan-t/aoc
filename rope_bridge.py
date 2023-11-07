def move(file):
    x = y = 0
    for line in file:
        direction, distance = line.split()
        for _ in range(int(distance)):
            x += (direction == 'R') - (direction == 'L')
            y += (direction == 'U') - (direction == 'D')

            # print('##', direction, distance, x, y)
            yield x, y


def follow(head):
    x = y = 0
    for hx, hy in head:
        if abs(hx - x) > 1 or abs(hy - y) > 1:
            y += (hy > y) - (hy < y)
            x += (hx > x) - (hx < x)

        # print('$$', hx, hy, x, y)
        yield x, y


file = open('rope_bridge_input.txt', 'r')
tenth = second = list(follow(move(file)))

for _ in range(8):
    tenth = follow(tenth)

print(len(set(second)))
print(len(set(tenth)))
