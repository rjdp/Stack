# Stack
CLI app based on Cement Framework to Check whether any of `php`, `nginx`, `mysql` is installed, if not then installs using proper subcommands and also reports their running status .

Using StackApp
==============
**Usage**|**Description**
`StackApp.py install` | Installs any of php,mysql,nginx if not already installed
`StackApp.py php` | Installs php if not already installed
`StackApp.py mysql`| Installs mysql if not already installed
`StackApp.py nginx`| Installs nginx if not already installed
`StackApp.py status --nginx` | reports whether nginx is running
`StackApp.py status --php` | reports whether php is running
`StackApp.py status --mysql` | reports whether mysql is running


Improvements for next version
=================================
1. Enable custom help text
2. Error handling ..etc
