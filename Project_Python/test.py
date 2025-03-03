
print("Script is running..")

from textanalysis.textanalysis import count_words

# Count the number of positive words
nb_positive_words = count_words("try.txt", ["good", "great"])

# Count the number of negative words
nb_negative_words = count_words("try.txt", ["bad", "awful"])

print("{} positive words.".format(nb_positive_words))
print("{} negative words.".format(nb_negative_words))