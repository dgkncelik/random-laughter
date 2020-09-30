import random

DEFAULT_LAUGHTER_SIZE = 10
LEFT_FINGER_SET = ['a', 's', 'd', 'f']
RIGHT_FINGER_SET = ['h', 'j', 'k', 'l']
PICK_SET = {
    0: LEFT_FINGER_SET,
    1: RIGHT_FINGER_SET
}


def create_random(start, end):
    return random.randint(start, end)


def create_laughter(size):
    laughter = ''
    for i in range(0, size):
        set_number = create_random(0, 1)
        finger_set = PICK_SET[set_number]
        char_position = create_random(0, len(finger_set) - 1)
        laughter = '%s%s' % (laughter, finger_set[char_position])

    return laughter


if __name__ == '__main__':
    print(create_laughter(DEFAULT_LAUGHTER_SIZE))
