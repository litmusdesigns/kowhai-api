from flask import Flask, request, jsonify
import random, json

app = Flask(__name__)

#  Dictionary of colors and their translations in Maori
with open('./includes/subjects.json') as f:
    subjects = json.load(f)

class Translator:
    def get_random_subject(self, subject, answer_lang, question_lang):
        subject_dict = subjects.get(subject)
        if subject_dict is None:
            return None

        question_dict = subject_dict.get(question_lang)
        answer_dict = subject_dict.get(answer_lang)
        if question_dict is None or answer_dict is None:
            return None

        random_subject = random.choice(list(question_dict.keys()))
        answer_translation = answer_dict[random_subject]
        question_translation = question_dict[random_subject]

        # Get 3 random distractors
        distractors = random.sample([s for s in answer_dict.values() if s != answer_translation], 3)

        options = [answer_translation] + distractors
        random.shuffle(options)

        return answer_translation, question_translation, options


@app.route('/api/get_question', methods=['GET'])
def get_question():
    subject = request.args.get('subject')
    answer_lang = request.args.get('answer_lang')
    question_lang = request.args.get('question_lang')

    subject_dict = subjects.get(subject)
    if subject_dict and subject_dict.get(answer_lang) and subject_dict.get(question_lang):
        translator = Translator()
        answer_translation, question_translation, options = translator.get_random_subject(subject, answer_lang, question_lang)

        if not answer_translation:
            return jsonify({"error": "Invalid subject"}), 400

        body = {
            "question": question_translation,
            "options": options,
            "answer": answer_translation,
        }
        response = jsonify(body)
        response.headers['Content-Type'] = 'application/json'

        return response

    return jsonify({"error": "Invalid parameters"}), 400



if __name__ == '__main__':
    app.run()
