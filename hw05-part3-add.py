from collections import defaultdict
from pathlib import Path
import sys


def parse_log_line(line: str) -> dict:
    pars_log = {}
    pars_log = line.rstrip('\n').split(" ", 3)
    return pars_log


def load_logs(file_path: str) -> list:
    file_path = Path(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            list_log = []
            for line in f:
                list_log.append(parse_log_line(line))
    except:
        print(f"{file_path} does not exist or is not a file")
    return list_log


def filter_logs_by_level(logs: list, level: str = "") -> list:
    if level == '':
        return
    print(f'\nДеталі логів для рівня {level.upper()}:')
    for i in range(len(logs)):
        if level.upper() in logs[i]:
            print (f'{logs[i][0]} {logs[i][1]} - {logs[i][3]}')
 
    return


def count_logs_by_level(logs: list) -> dict:
    num_logs = defaultdict(int)
    for i in range(len(logs)):
        list_num = logs[i][2]
        num_logs[list_num] +=1
    return(num_logs)


def display_log_counts(counts: dict):
    print('\nРівень логування | Кількість ')
    print(f'{"-"*17}|{"-"*11}')
    for key, value in counts.items():
        print(f'{key}{" "*(17-len(key))}|  {value}')
    print(f'{"-"*17}|{"-"*11}')


def main():
    if len(sys.argv) == 3:
        path = sys.argv[1]
        level = sys.argv[2]
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        level = ''
    else:
        return
    list = load_logs(path)
    dict = count_logs_by_level(list)
    display_log_counts(dict)
    if level:
        filter_logs_by_level(list, level)

if __name__ == "__main__":
    main()
