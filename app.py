from flask import Flask, request, jsonify, render_template, session
import wikipedia
import spacy

# Initialisation
app = Flask(__name__)
app.secret_key = "chatbot-secret-key"
wikipedia.set_lang("fr")
nlp = spacy.load("fr_core_news_sm")

# Fonction NLP : extraction du mot-clé
def extract_keyword(text):
    doc = nlp(text.lower())
    # Cherche les noms (NOUN) ou noms propres (PROPN) d’au moins 3 lettres
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"] and len(token.text) > 2]

    return keywords[0] if keywords else text

# Route d’accueil
@app.route('/')
def home():
    session['history'] = []
    return render_template('index.html')

# Route API : traitement des questions
@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get("question")
    keyword = extract_keyword(question)

    try:
        search_results = wikipedia.search(keyword)

        if not search_results:
            response_text = "❌ Aucun résultat trouvé."
        else:
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            summary = wikipedia.summary(page_title, sentences=3)

            # Vérifie que le résumé est lié à la finance
            finance_keywords = ["finance", "économie", "monnaie", "banque", "taux", "marché", "change", "capital", "valeur", "investissement", "trésorerie"]
            if not any(k in summary.lower() for k in finance_keywords):
                response_text = "ℹ️ Désolé, je suis un chatbot spécialisé en finance. N'hésitez pas à me poser une autre question dans ce domaine."
            else:
                response_text = (
                    f"Voici ce que j’ai trouvé sur ce sujet :\n\n{summary}\n\n"
                    f"🔗 <a href='{page.url}' target='_blank'>Voir l'article complet</a>\n\n"
                    f"💬 Avez-vous d'autres questions ?"
                )

    except Exception as e:
        response_text = f"⚠️ Une erreur est survenue : {str(e)}"

    # Historique
    history = session.get('history', [])
    history.append({"user": question, "bot": response_text})
    session['history'] = history

    return jsonify({'response': response_text, 'history': history})

# Lancement
if __name__ == '__main__':
    app.run(debug=True)
