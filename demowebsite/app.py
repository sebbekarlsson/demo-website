from flask import Flask, render_template, request, redirect
from demowebsite.logic.submit import submit_submission, get_submission_by_id
from demowebsite.models.submission import Submission


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submission')
def show_submission():
    idx = request.args.get('id')
    submission = get_submission_by_id(idx)
    print(submission)
    return render_template('submission.html', submission=submission)

@app.route('/submit', methods=['POST', 'GET'])
def submit_page():
    if request.form.get('submit'):
        submission = submit_submission(Submission(
            title=request.form.get('title'),
            description=request.form.get('description')
        ))
        return redirect(f'/submission?id={submission.idx}')
    return render_template('submit.html')