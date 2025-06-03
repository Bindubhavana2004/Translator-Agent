class UserAgent:
    def get_input(self):
        return input("Enter text to translate: ")

    def get_target_language(self):
        lang = input("Translate to which language (e.g., 'fr' for French, 'es' for Spanish, 'hi' for Hindi)? ").lower()
        return lang

