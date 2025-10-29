from collections import Counter

def get_num_words(text):
    print("----------- Word Count ----------")
    
    return len(text.split())

def get_num_chars(text):
    print("--------- Character Count -------")
    stats = Counter(text.lower())
    
    return dict(stats)

def sort_report(values):
    report = [{"char": char, "num": num} for char, num in values.items()]
    report.sort(reverse=True, key=lambda x: x["num"])
    
    return report
