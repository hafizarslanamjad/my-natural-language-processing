# NLP Functions Website

This project is a **Django-based web application** that demonstrates **commonly used Natural Language Processing (NLP) functions**.  
It is designed as a learning and reference tool for students, developers, and researchers exploring the intersection of **Django, Machine Learning, and NLP**.

---

## 🚀 Features

- 🌐 Web interface built with **Django**
- 🔤 Implementations of **common NLP functions**, such as:
  - Tokenization  
  - Stopword removal  
  - Bag-of-Words (BoW)  
  - TF-IDF  
  - Word embeddings  
- 🧠 Integration with **ML/NLP libraries** (NLTK, spaCy, scikit-learn, etc.)
- 📊 User-friendly examples and visualizations

---

## 📂 Project Structure

```
bow_checker/         # App handling Bag-of-Words examples
compare/             # App to compare different NLP functions
manage.py            # Django project manager
db.sqlite3           # SQLite database (ignored in .gitignore)
```

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/USERNAME/nlp_functions_site.git
cd nlp_functions_site
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

*(You can generate `requirements.txt` with: `pip freeze > requirements.txt`)*

---

## ▶️ Running the Server

```bash
python manage.py runserver
```

Then open in browser:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)  
- **NLP Libraries**: NLTK, spaCy, scikit-learn  
- **Database**: SQLite (default)  
- **Frontend**: Django Templates, Bootstrap (optional)  

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)  
- [NLTK](https://www.nltk.org/)  
- [spaCy](https://spacy.io/)  
- [scikit-learn](https://scikit-learn.org/)  
