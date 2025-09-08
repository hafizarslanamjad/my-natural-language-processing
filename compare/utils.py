from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import matplotlib.pyplot as plt
import io, base64

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


def bow_analysis(sentence1, sentence2):
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform([sentence1, sentence2])
    feature_names = vectorizer.get_feature_names_out()

    arr = vectors.toarray()
    similarity = cosine_similarity([arr[0]], [arr[1]])[0][0]

    # Create DataFrame
    df = pd.DataFrame({
        "Word": feature_names,
        "Sentence 1 Count": arr[0],
        "Sentence 2 Count": arr[1]
    })

    # --- Create Bar Chart ---
    fig, ax = plt.subplots(figsize=(6,4))
    x = range(len(feature_names))
    ax.bar([i - 0.2 for i in x], arr[0], width=0.4, label="Sentence 1")
    ax.bar([i + 0.2 for i in x], arr[1], width=0.4, label="Sentence 2")

    ax.set_xticks(x)
    ax.set_xticklabels(feature_names, rotation=45)
    ax.set_ylabel("Word Count")
    ax.set_title("Bag-of-Words Word Frequencies")
    ax.legend()

    # Save plot to base64 string
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode("utf-8")
    plt.close(fig)

    return similarity, df, graphic
