"""Create a hello world function to act as a GatorGrade example."""
import rich


def say_hello(name):
    """Print a greeting."""
    print(f"Hello, {name}!")


def say_hello_color(name, color):
    """Print a greeting in color."""
    rich.print(f"[{color}]Hello, {name}!")

# TODO: Call say_hello

# TODO: Call say_hello_color

