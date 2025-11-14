#!/usr/bin/env python3
# Student ID: vpatel278

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """used by print()"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """used by interactive shell"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

    def sum_times(self, t2):
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        return sec_to_time(self_sec + t2_sec)

    def change_time(self, seconds):
        now = self.time_to_sec()
        new_t = sec_to_time(now + seconds)
        self.hour = new_t.hour
        self.minute = new_t.minute
        self.second = new_t.second
        return None


def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
