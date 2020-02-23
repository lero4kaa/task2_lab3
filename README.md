# task2_lab3
This is task 2 of lab assignment 3.
With module task2.py user can easily navigate in json object (with friends of specific user), 
which is given in result of requesting Twitter. The .txt file with this object is also created.

# Example 
```python
>>> python task2.py
Enter Twitter Account:@Avicii
Retrieving https://api.twitter.com/1.1/friends/list.json?oauth_consumer_key=wD0ffDg0nQHvlIbZdw4531g1L&oauth_timestamp=1582489184&oauth_nonce=80648566&oauth_version=1.0&screen_name=%40Avicii&count=10&oauth_token
If you want to stop running program, just enter "STOP"
Remaining 12 possible attempts to access data for these 15 minutes.
Here you have dictionary and there are 6 objects.
Do you want to have whole dictionary printed, or continue looking for data inside this dictionary? Please enter 'printing' for printing whole dictionary and 'continue' for continue searching.
continue
Dictionary contains next keys:
 ['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count']
Which of them do you want to choose?
users
Your path in the file  beginning --> users
Here you have list and there are 10 objects.
Do you want to have whole list printed, or continue looking for data inside this list?. Please enter 'printing' for printing whole list and 'continue' for continue searching.
continue
Which of the list`s elements do you want to choose? Please, enter number in in range from 1 to 10
4
Your path in the file  beginning --> users --> 4
Here you have dictionary and there are 47 objects.
Do you want to have whole dictionary printed, or continue looking for data inside this dictionary? Please enter 'printing' for printing whole dictionary and 'continue' for continue searching.
continue
Dictionary contains next keys:
 ['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone
', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_backgrou
nd_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile
_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'bl
ocked_by', 'translator_type']
 Which of them do you want to choose?
screen_name
Your path in the file  beginning --> users --> 4 --> screen_name
RitaOra
