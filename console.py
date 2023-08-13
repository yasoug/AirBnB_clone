#!/usr/bin/python3
"""
Implementing the console for AirBnB project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Prints empty line when no argument"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
