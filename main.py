from flask import Flask, request, render_template
from functions import *

settings = get_settings()
candidates = get_candidates()

app = Flask(__name__)


@app.route("/")
def page_main():
    if settings.get("online"):
        return "Приложение работает"
    return "Приложение не работает"


@app.route("/candidate/<int:id>/")
def page_candidate(id):
    candidate = get_candidate_by_id(candidates, id)
    return render_template('candidate.html', candidate=candidate)


@app.route("/list/")
def page_list():
    return render_template("candidates_list.html", candidates=candidates)


@app.route("/search")
def search_by_name_page():
    name = request.args.get('name')

    if name:
        candidates_list = get_candidates_by_name(candidates, name, settings.get("case-sensitive"))
        count = len(candidates_list)
        if count:
            return render_template('search_name_list.html', count=count, candidates_list=candidates_list)
        return "Кандидаты не найдены"
    return "Введите имя кандидата"


@app.route("/skill/<sk>/")
def search_by_skill_page(sk):
    candidates_list = get_candidates_by_skill(candidates, sk, settings.get("limit"))
    if candidates_list:
        count = len(candidates_list)
        return render_template('search_skills_list.html', count=count, candidates_list=candidates_list)

    return "Кандидаты не найдены"


app.run()
