def main():
    print_args(100, 50, 25)
    print_kwargs(galleons=100, sickles=50, knuts=25)

# *args collects positional arguments into a tuple
def print_args(*args):
    print("Positional:", args)

# **kwargs collects named arguments into a dict
def print_kwargs(**kwargs):
    print("Named:", kwargs)

main()
