import argparse

def get_argparser():
    parser = argparse.ArgumentParser(description="Memo app")

    parser.add_argument("-a")
    parser.add_argument("-v", action="store_true")

    return parser

def write_memo(content):
    f = open('memo_extra.txt', 'a')
    f.write(content)
    f.write('\n')
    f.close()

def print_memo():
    f = open('memo_extra.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)

if __name__ == '__main__':
    args = get_argparser().parse_args()

    if args.a:
        write_memo(args.a)
    if args.v:
        print_memo()