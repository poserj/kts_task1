

__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    Use >= Python3.10
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    days = seconds // (24 * 60 * 60)
    hours = seconds // 3600 % 24
    minutes = seconds // 60 % 60
    sec = seconds % 60
    if days == 0 and hours == 0 \
       and minutes == 0:
        return f'{sec:02d}s'
    elif days == 0 and hours == 0:
        return f'{minutes:02d}m{sec:02d}s'
    elif days == 0:
        return f'{hours:02d}h{minutes:02d}m{sec:02d}s'
    else:
        return f'{days:02d}d{hours:02d}h{minutes:02d}m{sec:02d}s'


if __name__ == '__main__':
    print(seconds_to_str(20), '20s')
    print(seconds_to_str(60), '01m00s')
    print(seconds_to_str(65), '01m05s')
    print(seconds_to_str(3700), '01h01m40s')
    print(seconds_to_str(93600), '01d02h00m00s')
