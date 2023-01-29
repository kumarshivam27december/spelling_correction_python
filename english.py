# although this project does not work properly but still it can help to build basic of how this kind of projects are made with the help of python language

# # from textblob import TextBlob
# # from textwo
# # import textblob
# words = ["Data Scence", "Mahine Learnin"]
# corrected_words = []
# for i in words:
#     corrected_words.append(TextBlob(i))
# print("Wrong words :", words)
# print("Corrected Words are :")
# for i in corrected_words:
#     print(i.correct(), end=" ")
from textblob import TextBlob
words = ["Data Scence", "Mahine Learnin","Elephant","Tige"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")
