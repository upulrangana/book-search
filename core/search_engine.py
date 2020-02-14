import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from core.search_result import SearchResult


def read_data(path):
    ted_data = pd.read_csv(path)
    return ted_data


def tf_idf(keys, dataframe, label, min_results=1):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataframe.loc[:, label])

    query = tfidf_vectorizer.transform([keys])
    cs = cosine_similarity(query, tfidf_matrix)
    similarity_list = cs[0].copy()
    result_list = []
    while min_results > 0:
        tmp_index = np.argmax(similarity_list)
        if similarity_list[tmp_index] < 0.1 or tmp_index in result_list:
            min_results -= 1
            break
        result_list.append(tmp_index)
        similarity_list[tmp_index] = 0

        min_results -= 1

    print(f'Found {len(result_list)} results.')
    return [SearchResult(x, cs[0][x], dataframe.iloc[x]['body']) for x in result_list]


def search_book(query, book):
    return tf_idf(query, book.get_dataframe(), 'body', min_results=10)
