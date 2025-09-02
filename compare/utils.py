from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def bow_similarity(sentence1, sentence2):
    #Convert sentences to Bag of Words vectors
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform([sentence1, sentence2])
    feature_names = vectorizer.get_feature_names_out()

    # Convert sparse matrix to array
    arr = vectors.toarray()
    print("feature_names:", feature_names)
    print("arr[0]", arr[0])
    print("arr[1]", arr[1])

    #Compute Similarity
    similarity = cosine_similarity([arr[0]], [arr[1]])[0][0]

    #Put into dataframe for easier display
    df = pd.DataFrame({
        "Word": feature_names,
        "Sentence1Count": arr[0],
        "Sentence2Count": arr[1], 
    })

    return similarity, df