"""Chapter3 parser 예제
"""
import argparse
import time


def timing(f):
    def wrapper():
        ts = time.time()
        f()
        te = time.time()
        print(f"start: {ts}, end: {te}")
    return wrapper


@timing
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")


def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")


def greet(greeting, name):
    print(f'{greeting} {name}')


def test1():
    parser = argparse.ArgumentParser(description="최상위 parser")
    parser.add_argument('--twice', '-t',
                        help='Do it twice',
                        action='store_true')

    # git commit 에서 commit과 같은 function 정의 (ships, sailors)
    sub_parser = parser.add_subparsers(dest="func", description="서브 parser")
    ship_parser = sub_parser.add_parser("ships",
                                        help='Ship related commands')
    sailor_parser = sub_parser.add_parser("sailors",
                                          help='Talk to a sailor')

    # 각 function의 세부 옵션 정의
    # ./parser.py ships {list, sail}
    ship_parser.add_argument('command',
                             choices=['list', 'sail'])
    # ./parser.py sailors name -g hello
    sailor_parser.add_argument('name',
                               help='Sailors name')
    sailor_parser.add_argument('--greeting', '-g',
                               help='Greeting',
                               default='Ahoy there')
    args = parser.parse_args()

    print(args.func)
    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()


if __name__ == "__main__":
    # test1()
    print("hello")
