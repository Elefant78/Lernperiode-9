import difflib

class SpellChecker:
    def __init__(self, dictionary_path="wortliste.txt"):
        with open(dictionary_path, encoding="utf-8") as f:
            self.dictionary = set(word.strip().lower() for word in f if word.strip())

    def check_word(self, word):
        word = word.lower()
        if word in self.dictionary:
            return True, []
        else:
            suggestions = difflib.get_close_matches(word, self.dictionary, n=3, cutoff=0.75)
            return False, suggestions

    def check_text(self, text):
        import re
        words = re.findall(r'\b\w+\b', text.lower())  # trennt sauber Wörter, ignoriert Satzzeichen
        result = []
        for word in words:
            is_correct, suggestions = self.check_word(word)
            result.append({
                'word': word,
                'correct': is_correct,
                'suggestions': suggestions
            })
        return result