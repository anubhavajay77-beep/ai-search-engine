from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import urllib.parse

app = Flask(__name__)

@app.route('/')
def home():
    # HTML पेज रेंडर करेगा जहां सर्च बॉक्स और माइक बटन होगा
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Free Search Engine</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; }
            input[type="text"] { width: 40%; padding: 10px; font-size: 16px; }
            button { padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>My Custom Search Engine</h1>
        <form action="/search" method="get">
            <input type="text" name="query" id="search-box" placeholder="Type or click mic to speak...">
            <br><br>
            <button type="submit">Search</button>
            <button type="button" onclick="startVoice()">🎤 Speak</button>
        </form>

        <script>
            function startVoice() {
                var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                recognition.lang = 'en-US'; // या 'hi-IN' हिंदी के लिए
                recognition.start();
                recognition.onresult = function(event) {
                    document.getElementById('search-box').value = event.results[0][0].transcript;
                };
            </style>
    </body>
    </html>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    if query:
        # अभी के लिए यह डेटा को गूगल/विकिपीडिया पर रीडायरेक्ट करेगा (शुरुआती स्टेज के लिए)
        return f"<h2>Searching for: {query}</h2><p>Results system updating soon...</p>"
    return "Please enter a query."

if __name__ == '__main__':
    app.run(debug=True)
