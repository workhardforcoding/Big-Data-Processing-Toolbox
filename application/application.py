from cmd import Cmd
class MyPrompt(Cmd):
    prompt = 'custom_shell> '
    intro = '''Welcome to Big Data Processing application
Please choose the application you want to run:
1. Apache Hadoop
2. Apache Spark
3. Jupyter Notebook
4. SonarQube with SonarScanner
               
Please type to enter it> '''
    hyperlink_format = '<a href="{link}">{text}</a>'
    def do_exit(self, inp):
        print("Bye")
        return True
    def do_repeat(self,inp):
        intro = '''Welcome to Big Data Processing application
Please choose the application you want to run:
1. Apache Hadoop
2. Apache Spark
3. Jupyter Notebook
4. SonarQube with SonarScanner
Please type to enter it> '''
        print(intro)
    def do_hadoop (self,inp):
        print('Please use the below link to access Apache Hadoop:')
        link = "http://34.139.59.200:9870"
        #link = self.hyperlink_format.format(link=link, text='linky text')
        print(link)

    def do_spark(self, inp):
        print('Please use the below link to access Apache Spark:')
        link = "http://34.75.44.181:8080/"
        # link = self.hyperlink_format.format(link=link, text='linky text')
        print(link)

    def do_jupyter(self, inp):
        print('Please use the below link to access Jupyter Notebook:')
        link = "http://34.74.76.190:8888/"
        # link = self.hyperlink_format.format(link=link, text='linky text')
        print(link)

    def do_sonar(self, inp):
        print('Please use the below link to access SonarQube:')
        link = "http://34.139.88.70:9000/"
        #link = self.hyperlink_format.format(link=link, text='linky text')
        print(link)

    def do_something(selfself,inp):
        print('Unrecognized input , please type a number from 1-4')

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_add(self, inp):
        print("adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        if inp == '1':
            return self.do_hadoop(inp)
        elif inp == '2':
            return self.do_spark(inp)
        elif inp == '3':
            return self.do_jupyter(inp)
        elif inp == '4':
            return self.do_sonar(inp)
        elif inp == 'r':
            return self.do_repeat(inp)
        else:
            return self.do_something(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit

if __name__ == '__main__':
    MyPrompt().cmdloop()