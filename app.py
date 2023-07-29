from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Dictionary of colors and their translations in Maori
subjects = {
    "colors": {
        "red": "whero",
        "blue": "kikorangi",
        "green": "kakariki",
        "yellow": "kowhai",
        "black": "mangu",
        "white": "ma",
    },
    "numbers": {
        "1": "tahi",
        "2": "rua",
        "3": "toru",
        "4": "wha",
        "5": "rima",
        "6": "ono",
        "7": "whitu",
        "8": "waru",
        "9": "iwa",
        "10": "tekau",
    },
}


class Translator:
    def get_random_subject(self, subject):
        # Select a random subject from the subjects dictionary
        subject_dict = subjects.get(subject)
        if subject_dict is None:
            return None

        random_subject = random.choice(list(subject_dict.keys()))
        answer_translation = random_subject
        question_translation = subject_dict[random_subject]

        # Generate three distractors by randomly selecting subjects other than the correct one
        distractors = random.sample([s for s in subject_dict.keys() if s != random_subject], 3)

        # Combine the correct answer and distractors to form multiple-choice options
        options = [answer_translation] + [d for d in distractors]

        # Shuffle the options to randomize the order
        random.shuffle(options)

        return answer_translation, question_translation, options


@app.route('/api/get_question', methods=['GET'])
def get_random_subject():
    subject = request.args.get('subject')
    a_lang = request.args.get('answer_lang')
    q_lang = request.args.get('question_lang')

    # Check if the subject is valid and languages are 'en' and 'maori'
    if subject in subjects and a_lang == 'en' and q_lang == 'mi':
        translator = Translator()
        answer_translation, question_translation, options = translator.get_random_subject(subject)

        if not answer_translation:
            return jsonify({"error": "Invalid subject"}), 400

        # Prepare the response with the question, options, and correct answer
        response = {
            "question": question_translation,
            "options": options,
            "answer": answer_translation,
        }

        return jsonify(response)

    return jsonify({"error": "Invalid parameters"}), 400


if __name__ == '__main__':
    app.run()
