import re

class LessengerParser:
    """Class to read and parse the users request"""
    def parse(self, query, indicator):
        query = query.lower().strip()
        words = query.split()

        if len(words) == 1:
            return tuple(words)
  
        reg_word = r"\W*([\w* ]*)"
        regex = r"{}\W*{}{}".format(reg_word,indicator,reg_word)
        pattern = re.compile(regex)
        matches = re.search(pattern, query)
        if matches:
            return matches.groups()
        return ()
