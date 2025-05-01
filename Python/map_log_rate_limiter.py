# https://www.lintcode.com/problem/3620
# https://leetcode.com/problems/logger-rate-limiter
"""
Design a logger system that receive stream of messages along with its timestamps.

A message should be printed if and only if it has not been printed in the last 10 seconds.

In the method couldPrintMessage(), given a message and a timestamp in seconds, return true if the message can be 
 printed within the given timestamp, otherwise return false.

Different messages can be printed at the same moment, but not the same message.

At the end of a message, it is possible to immediately print that message again.

The input data will be sorted by timestamp in positive order.

Example
Example 1
Input
[[1,foo],[2,bar],[3,foo],[8,bar],[10,foo],[11,foo]]
Output
True
True
False
False
False
True
Explanation

[1,foo]  => message "foo" needs to be printed at time  1, when the queue for message "foo" is empty and can be printed, return true
[2,bar]  => message "bar" needs to be printed at time  2, when the queue for message "bar" is empty and can be printed, return true
[3,foo]  => message "foo" needs to be printed at time  3, when the queue for message "foo" is not empty
  (predecessor moment 1 is still in progress), so it cannot be printed, return false
[8,bar]  => message "bar" needs to be printed at time  8, when the queue for message "bar" is not empty 
 (predecessor moment 2 is still in progress), so it can't be printed, false
[10,foo] => message "foo" needs to be printed at time 10, when the queue for message "foo" is not empty 
 (predecessor moment 1 is still in progress), so it cannot be printed, return false
[11,foo] => message "foo" needs to be printed at time 11, when the queue for message "foo" is empty 
 (predecessor moment 1 has finished at moment 11), so it can be printed, return true

Example 2
Input
[[1,foo],[1,bar],[1,bar],[11,foo],[11,bar]]
Output
True
True
False
True
True
"""

class Logger:

    def __init__(self):
        self.message_map = dict()

    """
    @param timestamp: Timestamp
    @param message: Message
    @return: Whether the log can be printed
    """
    def could_print_message(self, timestamp: int, message: str) -> bool:
        if message not in self.message_map or abs(timestamp - self.message_map[message])>=10:
            self.message_map[message] = timestamp
            return True
        else: return False
