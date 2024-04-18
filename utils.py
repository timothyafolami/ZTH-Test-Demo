from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# placing in a function
def calculate_cosine_similarity(generated_sentences):
    # loading the reference dataaset
    df  = pd.read_csv('data_000.csv')
    reference_sentences = df.iloc[0].tolist()[1:]
    # Initialize the TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the sentences to TF-IDF vectors
    tfidf_matrix_reference = vectorizer.fit_transform(reference_sentences)
    tfidf_matrix_generated = vectorizer.transform(generated_sentences)
    

    # Compute cosine similarity between the generated and reference sentences
    cosine_similarities = cosine_similarity(tfidf_matrix_reference, tfidf_matrix_generated)

    return cosine_similarities[0][0]