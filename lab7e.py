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

    def __str__(self):
        '''return a string representation for the object self'''
        return  f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''return a string representation for the object self'''
        return  f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return this Time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def valid_time(self):
        """Check for the validity of the time object attributes"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

    def change_time(self, seconds):
        """Change this Time object by adding or subtracting seconds"""
        total_seconds = self.time_to_sec() + seconds
        t = Time.sec_to_time(total_seconds)
        self.hour = t.hour
        self.minute = t.minute
        self.second = t.second
        return None

    def sum_times(self, other):
        """Add this Time object with another Time object"""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return Time.sec_to_time(total_seconds)

    def time_to_sec(self):
        """Convert this Time object to total seconds"""
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def sec_to_time(seconds):
        """Convert total seconds to a Time object"""
        t = Time()
        t.hour = seconds // 3600
        seconds %= 3600
        t.minute = seconds // 60
        t.second = seconds % 60
        return t
