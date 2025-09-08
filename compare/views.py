from django.shortcuts import render
from .utils import bow_analysis

def tutorial(request):
    result = None
    table = None
    chart = None

    if request.method == "POST":
        s1 = request.POST.get("sentence1")
        s2 = request.POST.get("sentence2")

        sim, df, graphic = bow_analysis(s1, s2)

        if sim >= 0.999:
            result = "Sentences are the SAME (Bag-of-Words)"
        else:
            result = f"Sentences are Different (Similarity: {sim:.2f})"

        # Rename columns so template keys are safe
        df = df.rename(columns={
            "Sentence 1 Count": "s1",
            "Sentence 2 Count": "s2"
        })
        table = df.to_dict(orient="records")
        chart = graphic

    return render(request, "compare/tutorial.html", {"result": result, "table": table, "chart": chart})