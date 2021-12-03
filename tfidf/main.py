import numpy as np


class CountVectorizer:
    """
    Класс создает по наборам текстов терм-документную матрицу
    Методы:
    fit_transform
    get_feature_names
    tf_transform
    idf_transform
    """

    def __init__(self):
        self.list_of_words = []
        self.unic_word = 0

    def fit_transform(self, corpus: list) -> list:
        """
        :param corpus: список текстов
        :return count_matrix: термдокументая матрица
        """

        list_with_duplicate = []

        for text_str in corpus:
            list_with_duplicate.extend(text_str.lower().split())

        for element in list_with_duplicate:
            if element not in self.list_of_words:
                self.list_of_words.append(element)

        self.unic_word = len(self.list_of_words)
        count_matrix = []

        for text_str in corpus:
            final_row = []
            for element in self.list_of_words:
                final_row.append(text_str.lower().count(element))

            count_matrix.append(final_row)

        return count_matrix

    def get_feature_names(self) -> list:
        """
        :return: list_of_words - список слов в порядке их появления
        """
        return list(self.list_of_words)

    def tf_transform(self, count_matrix):
        """
        :param count_matrix: термдокументая матрица
        :return: tf_matrix: частота вхождения каждого слова в текст
        """
        tf_matrix = []

        for vector in count_matrix:
            number_of_word = sum(vector)
            tf_matrix_row = [round(i / number_of_word, 3) for i in vector]
            tf_matrix.append(tf_matrix_row)

        return tf_matrix

    def idf_transform(self, count_matrix):
        """
        :param count_matrix: термдокументая матрица
        :return: idf_matrix: обратная частота относительно всего документа
        idf = ln((всего документов + 1)/(документов со словом + 1)) + 1
        """
        idf_matrix = []
        document_count = len(count_matrix) + 1

        for col in range(len(count_matrix[0])):
            cur_sum = 0
            for row in range(len(count_matrix)):
                cur_sum += bool(count_matrix[row][col])
            idf_matrix.append(cur_sum + 1)

        for i in range(len(idf_matrix)):
            idf_matrix[i] = round(np.log(document_count / idf_matrix[i]) + 1, 3)

        return idf_matrix


class TfidfTransformer:
    """
    Класс для получения tf-idf матрицы
    """

    def fit_transform(self, tf_matrix, idf_matrix):
        """
        :param tf_matrix: частота вхождения каждого слова в текст
                idf_matrix: обратная частота относительно всего документа
        :return: tfidf_matrix: перемножение tf_matrix и idf_matrix
        """
        tfidf_matrix = []

        for vector in tf_matrix:
            tfidf_row = [round(i * j, 3) for i, j in zip(idf_matrix, vector)]
            tfidf_matrix.append(tfidf_row)

        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    """
    Класс наследник от CountVectorizer
    метод:
    fit_transform - возвращает tf-idf матрицу
    """

    def __init__(self):
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        """
        :param corpus: термдокументая матрица
        :return: tf-idf матрица
        """
        count_matrix = super().fit_transform(corpus)
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        return self._tfidf_transformer.fit_transform(tf_matrix, idf_matrix)


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    # тест 1 класса CountVectorize

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    names = vectorizer.get_feature_names()
    tf_matrix = vectorizer.tf_transform(count_matrix)
    idf_matrix = vectorizer.idf_transform(count_matrix)
    print('Тест класса CountVectorizer\n', count_matrix, '\n', names, '\n', tf_matrix, '\n', idf_matrix)

    # тест 2 класса TfidfVectorizer

    vectorizer2 = TfidfVectorizer()
    tfidf_matrix = vectorizer2.fit_transform(corpus)
    tf_matrix = vectorizer2.tf_transform(count_matrix)
    idf_matrix = vectorizer2.idf_transform(count_matrix)
    print('Тест класса TfidfVectorizer\n', tf_matrix, '\n', idf_matrix, '\n', tfidf_matrix)
