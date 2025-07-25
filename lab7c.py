#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0
    """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True


def time_to_sec(t):
    """Convert a Time object to total seconds"""
    return t.hour * 3600 + t.minute * 60 + t.second


def sec_to_time(seconds):
    """Convert total seconds to a Time object"""
    t = Time()
    t.hour = seconds // 3600
    seconds %= 3600
    t.minute = seconds // 60
    t.second = seconds % 60
    return t


def sum_times(t1, t2):
    """Add two Time objects using seconds math"""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)


def change_time(time, seconds):
    """Change a Time object by adding or subtracting seconds"""
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None
