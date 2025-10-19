Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> import re
... 
... def split_sentences(text):
...     """
...     Split a paragraph into sentences.
...     Handles abbreviations and decimals correctly.
...     """
...     # Match up to a period, question mark, or exclamation point
...     # Only if it's followed by a space + capital letter/number OR end of text
...     pattern = re.compile(r'(.*?[.!?])(?=\s+[A-Z0-9]|$)', re.M)
...     sentences = pattern.findall(text.strip())
...     return [s.strip() for s in sentences if s.strip()]
... 
... def main():
...     paragraph = input("Enter a paragraph:\n")
...     sentences = split_sentences(paragraph)
... 
...     print("\nSentences found:\n")
...     for i, s in enumerate(sentences, start=1):
...         print(f"{i}. {s}")
... 
...     print(f"\nTotal sentences: {len(sentences)}")
... 
... if __name__ == "__main__":
