import os

for (path, dir, files) in os.walk("/Users/mac/Basic_Grammar"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))