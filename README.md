pybot is a python irc bot. he is a project.


10-second TL;DR:
================

1. modify pybotrc with your channels and passwords.
2. `./bot.py pybotrc`
3. rejoice.

Longer explanation:
pybot requires mysqldb. It's probably in your package manager.

Run the included mysql_dump file (as root, `mysql -p < mysql_dump`).
Add a mysql user for pybot with permissions to update, insert, and delete from the created tables.

Set his dbpass in the config file to the password you've given him. 
Copy that config file to the home folder of whatever user will be running the bot.
As that user, `./bot.py.`
