import sys
# sys 대신 argparse라는 라이브러리를 많이 사용한다.
def memo_app():
    option = sys.argv[1]
    if option == '-a':
        content = sys.argv[2]
        f = open('memo.txt', 'a')
        f.write(content)
        f.write('\n')
        f.close()

    elif option == '-v':
        f = open('memo.txt', 'r')
        memo = f.read()
        f.close()
        print(memo)

if __name__ == '__main__':
    memo_app()

