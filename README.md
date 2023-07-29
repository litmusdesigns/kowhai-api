# Kowhai Learning Api

This is a simple Flask application that translates colors and numbers between English and Maori (Te Reo Māori). It provides a REST API endpoint to get random translation questions and options for colors and numbers.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of `Python`

## Installing the Api

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:litmusdesigns/kowhai-api.git
   cd kowhai-api
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Api

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. The app will be running locally at `http://127.0.0.1:5000`.

3. To get a random translation question, make a GET request to the following endpoint:

   ```
   GET http://127.0.0.1:5000/api/get_question?subject=<subject>&answer_lang=en&question_lang=mi
   ```

   Replace `<subject>` with either `colors` or `numbers` to get a random translation question for colors or numbers, respectively.

   Example usage with `curl`:

   ```bash
   curl "http://127.0.0.1:5000/api/get_question?subject=colors&answer_lang=en&question_lang=mi"
   ```

   The response will be in JSON format, containing the question, options, and the correct answer.

7. Remember to deactivate the virtual environment after using the app:

    ```bash
    deactivate
    ```

That's it! You can now use the Kowhai Learning Api to get random translation questions and test your knowledge of Maori colors and numbers. Enjoy!

## How to Run Unit Tests

The application includes a set of unit tests to verify its functionality. To run the unit tests, execute the following command:

```bash
python -m unittest discover -s tests
```

Make sure the Flask app is not running when executing the tests to avoid port conflicts.


## Contributing to the Api
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to the Kowhai Learning Api, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin kowhai-api/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

The following people have contributed to this project:

* [@litmusdesigns](https://github.com/litmusdesigns) 📖 💻 🐛

## Contact

If you want to contact me you can reach me at <peter@litmusdesigns.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [The Unlicense](./LICENSE).