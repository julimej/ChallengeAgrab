from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

sw = stopwords.words("english")
sw.append("^")
sw.append("–")
sw.append("Archived")
sw.append("Retrieved")
sw.append("original")
sw.append("&")
sw.append("edit")
sw.append("Wikipedia")