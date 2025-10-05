from textautocompleteengine import TextAutocompleteEngine

def main():
    import nltk
    nltk.download('brown')
    from nltk.corpus import brown

    freq_dist = nltk.FreqDist(w.lower() for w in brown.words())
    words = list(freq_dist.keys())

    text_autocomplete_engine = TextAutocompleteEngine(words, freq_dist)

    print("""
    ###############################################################################################
    ###############################################################################################
    Welcome to the Text Autocomplete Engine!

    How to use it: Enter a prefix and get suggestions based on word frequency from the Brown corpus.
    ###############################################################################################
    ###############################################################################################
    """)
    print("Enter prefixes to get autocomplete suggestions (type 'exit' to quit):")
    while True:
        prefix = input("Enter a prefix (type 'exit' to quit): ").strip().lower()
        if prefix == "exit":
            break
        suggestions = text_autocomplete_engine.get_suggestions(prefix)
        if suggestions:
            print(f"Suggestions for '{prefix}': {suggestions}")
        else:
            print(f"No suggestions found for '{prefix}'.")
        print("-" * 80)

if __name__ == "__main__":
    main()