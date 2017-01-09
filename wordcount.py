# put your code here.


def counting_words(file_name):
    """Print each word in the file and the number of times it appears.

    Each line of the file is read, the extra whitespace at the end is deleted with .rstrip
    and each word is split by whitespace. Then each word is counted and added to
    with each occurrence. If it's the first time the word shows up then it's initialized
    to 1. The output is printing the word and how many times it appears.
    """
    file_name = open(file_name)
    words_count = {}

    for line in file_name:
        words = line.rstrip().split(" ")
        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

    for key_word, number in words_count.iteritems():
        print "{} {}".format(key_word, number)


counting_words("twain.txt")
