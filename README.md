# task2_lab3
This is task 2 of lab assignment 3.
With module task2.py user can easily navigate in json object (with friends of specific user), 
which is given in result of requesting Twitter. The .txt file with this object is also created.

# Usage
To start, enter user_name of any Twitter user. You can check information maximum about 15 users per 15 minutes. 
Program tells you type and length of object, which you examine now. Then you can ask to print this whole 
object or continue searching inside it. For continue searching choose key from proposed list of keys.
Enter "STOP" anytime you want to stop running program.

# Example 
```python
>>> python task2.py
Enter Twitter Account:@Avicii
Retrieving https://api.twitter.com/1.1/friends/list.json?oauth_consumer_key=wD0ffDg0nQHvlIbZdw4531g1L&oauth_timestamp=1582489543&oauth_nonce=23997528&oauth_version=1.0&screen_name=%40Avicii&count=10&oauth_token
If you want to stop running program, just enter "STOP"
Remaining 14 possible attempts to access data for these 15 minutes.
Here you have dictionary and there are 6 objects.
Do you want to have whole dictionary printed, or continue looking for data inside this dictionary? Please enter 'printing' for printing whole dictionary and 'continue' for continue searching.
continue
Dictionary contains next keys:
 ['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
Which of them do you want to choose?
next_cursor
Your path in the file  beginning --> next_cursor
Result: 1579491163957883248
