import sys


def replace_content(src):
    f = open(src)
    tab_content = f.read()
    f.close()

    space_content = tab_content.replace("\t", " " * 4)
    return space_content


def write_content(dst, content):
    f = open(dst, 'w')
    f.write(content)
    f.close()


if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2]

    content = replace_content(src)
    write_content(dst, content)
