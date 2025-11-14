#!/usr/bin/env python3
# Student ID: vpatel278

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True


def time_to_sec(t):
    """convert Time → total seconds since 00:00:00"""
    minutes = t.hour * 60 + t.minute
    seconds = minutes * 60 + t.second
    return seconds


def sec_to_time(seconds):
    """convert total seconds → Time object"""
    t = Time(0, 0, 0)
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t


def sum_times(t1, t2):
    total_sec = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_sec)


def change_time(time, seconds):
    total_sec = time_to_sec(time) + seconds
    new_t = sec_to_time(total_sec)
    # mutate the original object
    time.hour = new_t.hour
    time.minute = new_t.minute
    time.second = new_t.second
    return None
