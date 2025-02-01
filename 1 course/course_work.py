from datetime import datetime

from utils.filesystem import read_file


def parse_log_line(line):
    parts = line.strip().split(', ')
    log_data = {}
    for part in parts:
        key, value = part.split(': ')
        log_data[key] = value
    return log_data


def transform_data(data: str) -> list[dict]:
    return [parse_log_line(line) for line in data.splitlines()]


def get_statistic_period(logs: list[dict]) -> list:
    dates = [datetime.strptime(log['date_connected'], "%d/%m/%Y %H:%M") for log in logs]
    min_date = min(dates).strftime("%d/%m/%Y")
    max_date = max(dates).strftime("%d/%m/%Y")
    return [min_date, max_date]


def count_unique_users(logs: list[dict]) -> int:
    users = set(log['username'] for log in logs)
    return len(users)


def count_user_connections(logs: list[dict]) -> dict:
    connections = dict()
    for log in logs:
        user = log['username']
        connections[user] = connections.get(user, 0) + 1
    return connections


def get_user_unique_ips(logs: list[dict]) -> dict:
    ips = dict()
    for log in logs:
        user = log['username']
        if user not in ips:
            ips[user] = set()
        ips.get(user).add(log['ip'])
    return {user: list(ips[user]) for user in ips}


def count_user_unique_ips(logs: list[dict]) -> dict:
    ips = get_user_unique_ips(logs)
    return {user: len(ips[user]) for user in ips}


def _count_duration_in_seconds(duration: str) -> int:
    hours, minutes, seconds = [int(part) for part in duration.split(':')]
    return hours * 3600 + minutes * 60 + seconds


def count_users_durations_time(logs: list[dict]) -> dict:
    durations = dict()
    for log in logs:
        user = log['username']
        durations[user] = durations.get(user, 0) + _count_duration_in_seconds(log['connection_duration'])
    return durations


def main(logs: list[dict]) -> None:
    statistic_period = get_statistic_period(logs)
    print(f'Statistic period: {statistic_period}')
    unique_users = count_unique_users(logs)
    print(f'Unique users: {unique_users}')
    user_connections_count = count_user_connections(logs)
    print(f'User connections: {user_connections_count}')
    unique_ips = get_user_unique_ips(logs)
    print(f'Unique IPs: {unique_ips}')
    user_unique_ips_count = count_user_unique_ips(logs)
    print(f'User unique IPs count: {user_unique_ips_count}')
    users_durations_time = count_users_durations_time(logs)
    print(f'User durations time: {users_durations_time}')


if __name__ == '__main__':
    filename = "../Homeworks/1 course/test_logs.txt"
    data = read_file(filename)
    logs = transform_data(data)
    main(logs)
