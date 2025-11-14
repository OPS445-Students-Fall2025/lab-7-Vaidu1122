#!/usr/bin/env python3
# Student ID: vpatel278
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    total = Time(0,0,0)
    total.hour = t1.hour + t2.hour
    total.minute = t1.minute + t2.minute
    total.second = t1.second + t2.second

    # carry seconds → minutes
    if total.second >= 60:
        carry_min = total.second // 60
        total.second = total.second % 60
        total.minute += carry_min

    # carry minutes → hours
    if total.minute >= 60:
        carry_hr = total.minute // 60
        total.minute = total.minute % 60
        total.hour += carry_hr
    
    return total

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
