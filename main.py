def read_text_file(file_path):
    file = open(file_path, 'r')
    lines = []
    for line in file:
        lines.append(line)
    file.close()
    text = "".join(lines)
    return text

def clean_text(text):
    """Converts the text to lowercase and removes punctuation"""
    # convert to lowercase
    text = text.lower()
    # remove punctuation
    punctuation = ['.', ',', ';', ':', "'", '"', '!', '?', '-', '(', ')', '[', ']', '{', '}', '/', '\\', '|', '<', '>', '@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '`', '~']
    # clean the text
    for punc in punctuation:
        text = text.replace(punc, '')
    return text

def clean_text1(text):
    """Converts the text to lowercase and removes punctuation"""
    text = text.lower()
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for character in punctuation:
        text = text.replace(character, '')
    return text

def clean_text2(text):
    """Converts the text to lowercase and removes punctuation"""
    # convert to lowercase
    text = text.lower()
    # remove punctuation
    punctuation = ['.', ',', ';', ':', "'", '"', '!', '?', '-', '(', ')']
    for punc in punctuation:
        text = text.replace(punc, '')
    return text

def count_words(words):
    """Counts the frequency of each unique word in words"""
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def plot_word_count(word_count, n):
    """Plots the top n words in a word_count dictionary"""
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')

# sort the word_count dictionary by value
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # get the top n words
    top_words = word_count[:n]
    # create the plot
    plt.bar(range(n), [x[1] for x in top_words], align='center')
    plt.xticks(range(n), [x[0] for x in top_words])
    plt.xticks(rotation=70)
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Top {} Words in the Text'.format(n))
    plt.show()


def main():
    """Main method that runs when the python file is run"""
    # read the text file
    text = read_text_file('data/pg26732.txt')
    # clean the text
    words = clean_text(text)
    # count the words
    word_count = count_words(words)
    # plot the top n words
    plot_word_count(word_count, 20)

if __name__ == "__main__":
    main()
