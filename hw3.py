class CountVectorizer():
    """Класс создает по наборам текстов терм-документную матрицу"""

    def __init__(self):
        self.list_of_words = []
        self.matrix = [[]]
        self.unic_word = 0

    def fit_transform(self, corpus: list) -> list:

        list_with_duplicate = []

        for text_str in corpus:
            list_with_duplicate += text_str.lower().split()

        for element in list_with_duplicate:
            if element not in self.list_of_words:
                self.list_of_words.append(element)

        number_of_texts = len(corpus)
        self.unic_word = len(self.list_of_words)

        self.matrix = [[0]*self.unic_word for _ in range(number_of_texts)]

        for i in range(number_of_texts):
            for j, element in enumerate(self.list_of_words):
                self.matrix[i][j] = corpus[i].lower().count(element)

        return self.matrix

    def get_feature_names(self) -> list:
        return list(self.list_of_words)


if __name__ == '__main__':
    # тест1
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    # тест2
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
        'PASTA like cheese'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
