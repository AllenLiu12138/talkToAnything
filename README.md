# Talk to Anything

This application is a Python Flask based service which accepts multiple types of documents (.pdf, .doc, .docx, .jpg, .png, .wav, .mp4), extracts and stores the text content. It provides an endpoint to interact with the stored content via GPT-3.5-turbo-16k model.

## Star Me on GitHub

You can also show your support by starring this GitHub repository:

[![GitHub stars](https://img.shields.io/github/stars/Your-Username/Your-Repo-Name.svg?style=social&label=Star)](https://github.com/Your-Username/Your-Repo-Name)

## Support Me

If you find this project useful, you can support me by buying me a coffee:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee--yellow.svg?style=for-the-badge&logo=ko-fi)](https://www.buymeacoffee.com/xliu28x)

## Connect with Me

You can connect with me on LinkedIn:

[![LinkedIn](https://img.shields.io/badge/LinkedIn--blue.svg?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/xu-liu-644666225/)


## Getting Started

These instructions will guide you on how to set up and run this application on your local machine for development and testing purposes.

## Prerequisites

This project requires the following libraries and dependencies:

- Python 3.7+
- Flask
- Textract
- SpeechRecognition
- MoviePy
- PIL
- PyTesseract
- OpenAI
- CV2
- UUID
- pdfplumber
- Werkzeug

In addition to these, you need to get the OpenAI API Key.

## Installation

1. Clone this repository

    \`\`\`sh
    git clone https://github.com/Your-Username/Your-Repo-Name.git
    \`\`\`

2. Navigate to the project directory

    \`\`\`sh
    cd Your-Repo-Name
    \`\`\`

3. Set up a virtual environment

    \`\`\`sh
    python -m venv env
    \`\`\`

4. Activate the virtual environment

    \`\`\`sh
    # Windows
    .\env\Scripts\activate

    # Linux/MacOS
    source env/bin/activate
    \`\`\`

5. Install the requirements

    \`\`\`sh
    pip install -r requirements.txt
    \`\`\`

6. Create a `.env` file and add the following content:

    \`\`\`sh
    OPENAI_API_KEY='Your OpenAI API Key'
    SECRET_KEY='Your Flask Secret Key'
    \`\`\`

7. Run the application

    \`\`\`sh
    flask run
    \`\`\`

The server will start running at http://127.0.0.1:5000.

## Usage

The application has two main routes:

- `POST /upload`: To upload the document and extract text from it. The extracted text is stored in memory.
- `POST /interact`: To send a message to the application and get a response from the GPT-3.5-turbo-16k model.

You can use tools like Postman or Curl to send requests to these endpoints.

## License

This project is licensed under the terms of the MIT license.

## Acknowledgments

- The OpenAI team for their API and models
- The contributors of the Python libraries used in this project

Remember to replace 'Your OpenAI API Key' and 'Your Flask Secret Key' with your actual keys. Also, replace 'Your-Username' and 'Your-Repo-Name' with your actual GitHub username and repository name. Don't forget to replace the license type if you are using any other than MIT.

