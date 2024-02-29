from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = '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'

def generate_image(text): 
    try:
        res = openai.Image.create( 
            prompt=text, 
            n=1, 
            size="256x256", 
        ) 
        return res["output"][0]["url"]
    except Exception as e:
        print("Error:", e)
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    image_url = generate_image(text)
    if image_url:
        return render_template('result.html', image_url=image_url)
    else:
        return "Failed to generate image."

if __name__ == '__main__':
    app.run(debug=True)
