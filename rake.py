"""
Rapid Automatic Keyword Extraction (RAKE) is a well-known keyword extraction method which uses a list of stopwords
and phrase delimiters to detect the most relevant words or phrases in a piece of text.
"""
from rake_nltk import Rake


class KeywordExtraction:
    THRESHOLD = 1

    def __init__(self, text):
        self.r = Rake()
        self.text = text

    def return_keywords(self) -> list:
        self.r.extract_keywords_from_text(self.text)
        return self.r.get_ranked_phrases()

    def return_keywords_with_score(self) -> tuple:
        self.r.extract_keywords_from_text(self.text)
        return self.r.get_ranked_phrases_with_scores()

    def return_keywords_with_score_more_than_threshold(self) -> list:
        return [tup[1] for tup in self.return_keywords_with_score() if tup[0] > self.THRESHOLD]




