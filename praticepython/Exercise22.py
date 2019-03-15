"""
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
and print out the results to the screen.

Extra:

1 . Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
and count how many of each 'category' of each image there are. This text file is actually a list of
files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy
for the images. Once you take a look at the first line or two of the file, it will be clear which part represents
the scene category. To do this, you are going to have to remember a bit about string parsing in Python 3.
I talked a little bit about it in this post.
"""


def count_names_and_frequency_from_file():
    import re
    dic = {}
    with open("/home/leonarbc/PycharmProjects/training/practicepython/list_of_names.txt", 'r+') as filenames:
        pattern = re.compile(r'[\t\s\b\n]*(?P<name>\w+)[\t\s\b\n]')
        match = re.findall(pattern, filenames.read())
        for name in match:
            if name not in dic.keys():
                dic[name]=1
            else:
                dic[name]+=1

    print dic

if __name__ == '__main__':
    count_names_and_frequency_from_file()
