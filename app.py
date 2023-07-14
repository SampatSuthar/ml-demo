import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)
    prediction = prediction[:, 1]
    #predict = prediction[:, 1]
    output = np.round(prediction[0], 2)

    import openai
    openai.api_key = ${{ secrets.OPENAI_API_KEY }}
    prompt = "create openai API for pull request summary in github"
    model = "text-davinci-003"
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=10)
    
    generated = response.choices[0].text
    print(generated)
    
    return render_template('index.html',  prediction ='Probability of initiative completion is {}'.format(output))



#if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    app.run(debug=True)
