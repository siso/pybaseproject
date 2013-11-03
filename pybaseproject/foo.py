import pybaseproject
import pybaseproject.bar


def main():
    print __name__

    bar = pybaseproject.bar.Bar()
    print bar.echo('Hola!')

if __name__ == '__main__':
    main()
