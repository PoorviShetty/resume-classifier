from flask import Flask, render_template, request, redirect, session, url_for
import re
import pickle


app = Flask(__name__)
app.secret_key = "any random string"

def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText) 
    resumeText = re.sub('RT|cc', ' ', resumeText) 
    resumeText = re.sub('#\S+', '', resumeText) 
    resumeText = re.sub('@\S+', '  ', resumeText)  
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText) 
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText) 
    return resumeText

mapping = {6: 'Data Science',
 12: 'HR',
 0: 'Advocate',
 1: 'Arts',
 24: 'Web Designing',
 16: 'Mechanical Engineer',
 22: 'Sales',
 14: 'Health and fitness',
 5: 'Civil Engineer',
 15: 'Java Developer',
 4: 'Business Analyst',
 21: 'SAP Developer',
 2: 'Automation Testing',
 11: 'Electrical Engineering',
 18: 'Operations Manager',
 20: 'Python Developer',
 8: 'DevOps Engineer',
 17: 'Network Security Engineer',
 19: 'PMO',
 7: 'Database',
 13: 'Hadoop',
 10: 'ETL Developer',
 9: 'DotNet Developer',
 3: 'Blockchain',
 23: 'Testing'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        resume = request.form['resume']
        sample = loaded_vectorizer.transform([cleanResume(resume)])
        result = mapping[loaded_model.predict(sample)[0]]
        session["resume"] = resume
        session['result'] = result
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    app.run(debug = True)
