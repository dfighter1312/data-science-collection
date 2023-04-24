from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stop_words = set(stopwords.words('english'))

def clean_text(sentence):
    sentence = sentence.lower()
    sentence = re.sub("s+"," ", sentence)
    sentence = re.sub("W"," ", sentence)
    sentence = re.sub(r"httpS+", "", sentence)
    sentence = ' '.join(word for word in sentence.split() if word not in stop_words)
    return sentence.strip()


if __name__ == "__main__":
    sc = SparkContext(appName="Text Cleaning")
    strc = StreamingContext(sc, 3)

    text_data = strc.socketTextStream("localhost", 8083)

    cleaned_text = text_data.map(lambda line: clean_text(line))
    cleaned_text.pprint()
    
    strc.start()
    strc.awaitTermination()