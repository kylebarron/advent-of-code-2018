import re
from datetime import datetime

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]

    parsed_lines = [parse_line(line) for line in lines]
    parsed_lines = sorted(parsed_lines, key=lambda tup: tup[0])
    grouped_lines = group_lines(parsed_lines)

    guard_dict = {}
    for group in grouped_lines:
        guard_id, time_asleep = get_time_asleep(group)
        guard_dict[guard_id] = guard_dict.get(guard_id, 0) + time_asleep

    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    max_guard_id = max(guard_dict, key=guard_dict.get)
    minute_most_asleep, _ = get_minute_most_asleep(grouped_lines, max_guard_id)
    print('Part 1:')
    print(int(max_guard_id) * minute_most_asleep)

    data = []
    max(data[])
    for guard_id, minutes_asleep in guard_dict.items():
        if minutes_asleep == 0:
            continue

        minute, times = get_minute_most_asleep(grouped_lines, guard_id)
        data.append((guard_id, minute, times))

    from operator import itemgetter
    max(data, key=itemgetter(2))

def parse_line(line):
    timestamp = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
    action = line[19:]
    return timestamp, action

def group_lines(lines):
    idxs = [ind for ind, line in enumerate(lines) if 'begins shift' in line[1]]
    grouped = []
    for i in range(len(idxs)):
        start_idx = idxs[i]
        if i == len(idxs) - 1:
            grouped.append(lines[start_idx:])
        else:
            end_idx = idxs[i+1]
            grouped.append(lines[start_idx:end_idx])
    return grouped

def get_time_asleep(group):
    guard_id = re.search(r'Guard #(\d+)', group[0][1]).group(1)
    group = group.copy()[1:]
    time_asleep = 0
    for falls_asleep, wakes_up in zip(group[::2], group[1::2]):
        assert falls_asleep[1] == 'falls asleep'
        assert wakes_up[1] == 'wakes up'
        time_asleep += (wakes_up[0] - falls_asleep[0]).seconds

    return guard_id, time_asleep


def get_minute_most_asleep(grouped_lines, guard_id=None):
    groups_of_id = []
    for group in grouped_lines:
        if guard_id == re.search(r'Guard #(\d+)', group[0][1]).group(1):
            groups_of_id.append(group[1:])

    # Get
    flat_list = [item for sublist in groups_of_id for item in sublist]
    minutes = {}
    for falls_asleep, wakes_up in zip(flat_list[::2], flat_list[1::2]):
        assert falls_asleep[1] == 'falls asleep'
        assert wakes_up[1] == 'wakes up'

        asleep_minute = falls_asleep[0].minute
        up_minute = wakes_up[0].minute

        for minute in range(asleep_minute, up_minute):
            minutes[minute] = minutes.get(minute, 0) + 1

    max_minute = max(minutes, key=minutes.get)
    return max_minute, max(minutes)




if __name__ == '__main__':
    main()
