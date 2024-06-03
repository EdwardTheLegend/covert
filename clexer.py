TOKENS = {
    
}

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.current = 0
        self.line = 1
        self.column = 0

