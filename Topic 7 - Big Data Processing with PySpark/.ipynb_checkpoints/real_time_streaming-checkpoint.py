from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(sentence):
    sentence = sentence.lower()
    sentence = re.sub("s+"," ", sentence)
    sentence = re.sub("W"," ", sentence)
    sentence = re.sub(r"httpS+", "", sentence)
    sentence = ' '.join(word for word in sentence.split() if word not in stop_words)
    sentence = [lemmatizer.lemmatize(token, "v") for token in sentence.split()]
    sentence = " ".join(sentence)
    return sentence.strip()


if __name__ == "__main__":
    sc = SparkContext(appName="Text Cleaning")
    strc = StreamingContext(sc, 3)

    text_data = strc.socketTextStream("localhost", 8084)
    
    strc.start()
    strc.awaitTermination()