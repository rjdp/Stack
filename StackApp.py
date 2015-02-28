#!/usr/bin/env python3
from os import system

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.core import handler

phpstatus = system('php --version > /dev/null > /dev/null')
phpstatus_active = system('pgrep -l mysqld > /dev/null')

mysqlstatus = system('dpkg --get-selections | grep mysql > /dev/null')
mysqlstatus_active = system('pgrep -l mysqld > /dev/null')


nginxstatus = system('which nginx ')
nginxstatus_active = system('service nginx status > /dev/null ')

#print(mysqlstatus)


class StackAppBaseController(CementBaseController):

    class Meta:
        label = 'base'
        description = "Stack is Basic Stack Setup Checker."
       

    @expose(help="BlogApp Guide", hide=True)
    def default(self):
        info_msg = "Basic Stack Setup Checker."
        banner = '#' + '@' * (len(info_msg) - 2) + '#'
        border = '|' + ' ' * (len(info_msg) - 2) + '|'
        lines = [banner, border, info_msg, border, banner]
        disp = '\n'.join(lines)
        print(disp)
        
        #self.app.args.parse_args(['--help'])

    @expose(help="second-controller default command", hide=True)
    def install(self):
        self.php()
        self.mysql()
        self.nginx()

    @expose(help="second-controller default command", hide=True)
    def php(self):
        if phpstatus!=0:
        	print("php not installed .. istalling")
        	system('sudo add-apt-repository ppa:eugenesan/ppa && \
        		sudo apt-get update && sudo apt-get install php5')
        else:
        	print("php already installed")

    @expose(help="second-controller default command", hide=True)
    def mysql(self):
        if mysqlstatus!=0:
        	print("mysql not installed .. istalling")
        	system('sudo apt-get install mysql-server && \
        		sudo apt-get install mysql-client')
        else:
        	print("mysql already installed")

    @expose(help="second-controller default command", hide=True)
    def nginx(self):
        if nginxstatus!=0:
        	print("nginx not installed .. istalling")
        	system('sudo apt-get update && sudo apt-get install nginx')
        else:
        	print("nginx already installed")

    


class StatusController(CementBaseController):

    class Meta:
        label = 'status'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "--nginx or --php or --mysql"
        arguments = [(['--nginx'],dict(action='store_true', dest='nginx',
                      help='check nginx status')),(['--php'],dict(action='store_true', dest='php',
                      help='check php status ')),(['--mysql'],dict(action='store_true', dest='mysql',
                      help='check mysql status')),
        ]

    @expose(help="second-controller default command", hide=True)
    def default(self):
    	if self.app.pargs.nginx:
    		if nginxstatus_active!=0:
    			print("nginx is not active")
    		else:
    			print("nginx is active")
    	if self.app.pargs.php:
    		if phpstatus_active!=0:
    			print("php is not active")
    		else:
    			print("php is active")
    	if self.app.pargs.mysql:
    		if mysqlstatus_active!=0:
    			print("mysql is not active")
    		else:
    			print("mysql is active")




def main():
    try:
        # create the application
        app = CementApp('StackApp')

        # register controllers
        handler.register(StackAppBaseController)
        handler.register(StatusController)
        
        # setup the application

        app.setup()

        # run the application
        app.run()

    finally:
        # close the application
        app.close()

if __name__ == '__main__':
    main()
