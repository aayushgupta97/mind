"""
Rapid Automatic Keyword Extraction (RAKE) is a well-known keyword extraction method which uses a list of stopwords
and phrase delimiters to detect the most relevant words or phrases in a piece of text.
"""
from rake_nltk import Rake


class KeywordExtraction:
    THRESHOLD = 3.5

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



"""
Sample Text lines
I remember when I used to take my red car out for a ride in my sunflower fields. we had a huge villa where our black
 horses, and cute corgi dogs running around. I also remember my beautiful wife and I under the starry nights in new york city.
 
 
I remember when I used to take my red car out for a ride in my sunflower fields. We had a huge farm with a stable full of black horses.
"""
