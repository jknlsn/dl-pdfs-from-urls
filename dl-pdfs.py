"""Downloads all PDFs given in a text file as URLS."""
import argparse
import errno
import os
import sys
import urllib

# TODO: Add a way to change folder mid scan, or save to multiple folders.
# TODO: Add interactive mode.


# Used to make the directory
def makeFolder(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


# Defines and parses the  command line arguments passed to the program
def parse():
    parser = argparse.ArgumentParser(
            description="Download PDFs", conflict_handler='resolve')
    parser.add_argument('-f', type=str, default="./PDFs",
                        help="Enter the name of the folder to store PDFs.")
    parser.add_argument('-s', type=str, default="./urls.txt",
                        help="Set the source file containing URLs to parse.")
    return parser.parse_args()


def read_urls(filename):
    urls = set()
    if os.path.isfile(filename) is True:
        with open(filename, 'r') as file:
            for line in file:
                # TODO: Add a check for comments or empty lines
                words = line.split(" ")
                if len(words) == 1:
                    urls.add(words[0].rstrip())
    return urls


def download_files(urls, folder):
    for url in urls:
        filename = url.split("/")[-1]
        print (filename)
        # urllib.url_retrieve(url, folder + "/" + filename)


def main():
    print ("Starting...")
    args = parse()

    urls = read_urls(args.s)
    # print(urls)
    download_files(urls, args.f)
    # print (args.f)
    # print (args.u)

    print ("Download completed.")

if __name__ == "__main__":
    main()
