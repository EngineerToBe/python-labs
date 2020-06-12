import click
import random
import psutil
import resource

@click.group()
def main():
    pass


@click.command()
#@click.argument('cpucount')

def cpucount():
    print(f"This is a {psutil.cpu_count()} core Server.")

@click.command()
#@click.argument('cpupercent')
def cpupercent():
    print(f"The current CPU usage is : {psutil.cpu_percent()}")

#print(psutil.disk_partitions())

@click.command()
def memory():
    memory = psutil.virtual_memory()
    print(memory)

main.add_command(cpucount)
main.add_command(cpupercent)
main.add_command(memory)



if __name__ == '__main__':
        main()
