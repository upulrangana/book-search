import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_data(path):
    ted_data = pd.read_csv(path)
    return ted_data


def tf_idf(keys, dataframe, label, min_videos=1):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataframe.loc[:, label])

    query = tfidf_vectorizer.transform([keys])
    cs = cosine_similarity(query, tfidf_matrix)
    similarity_list = cs[0]
    result_list = []
    while min_videos > 0:
        tmp_index = np.argmax(similarity_list)
        result_list.append(tmp_index)
        similarity_list[tmp_index] = 0
        min_videos -= 1

    print("result_list: %s" % result_list)
    print(dataframe.iloc[[result_list[0]]])
    return result_list


print('Starting up')
data = read_data('../data/transcripts.csv')
tf_idf('women empowerment', data, 'transcript')
