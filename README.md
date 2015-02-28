# Stack
Checks status whether any of php,nginx,mysql is installed, if not then installs using proper subcommands and also reports their running status

Usage
======
1) StackApp.py install => installs any of php,mysql,nginx if not already installed
2) StackApp.py php => installs php if not already installed
3) StackApp.py mysql => installs mysql if not already installed
4) StackApp.py nginx => installs nginx if not already installed
5) StackApp.py status --nginx => reports whether nginx is running
6) StackApp.py status --php => reports whether php is running
7) StackApp.py status --mysql => reports whether mysql is running


Improvements for next version
=================================
1) Enable custom help text
2) Error handling ..etc
