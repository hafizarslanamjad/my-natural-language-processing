from django.shortcuts import render
from .utils import bow_similarity

# Create your views here.
def tutorial(request):
    result = None
    table = None
    if request.method == 'POST':
        s1 = request.POST.get('sentence1')
        print(s1)
        s2 = request.POST.get('sentence2')
        print(s2)
        sim, df = bow_similarity(s1, s2)
        print(sim)

        if sim >= 1.0:
            result = "Sentences are SAME (Bag-of-Words)"
        else:
            result = f"Sentences are Different (Similarity: {sim: .2f})"
        
        #Convert Dataframe to list of rows for the template
        table = df.to_dict(orient="records")

    return render(request, "compare/tutorial.html", {"result": result, "table": table})