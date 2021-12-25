import json
from flask import Flask, request, render_template

with open("settings.json") as file:
    settings = json.load(file)

with open('candidates.json') as file:
    candidates = json.load(file)

app = Flask(__name__)


@app.route("/")
def page_main():
    if settings["online"]:
        return "Приложение работает"
    return "Приложение не работает"


@app.route("/candidate/<id>/")
def page_candidate(id):
    for candidate in candidates:
        if candidate['id'] == int(id):
            return render_template('candidate.html', **candidate)

#
# @app.route("/candidate/<name>/")
# def page_candidate(name):
#     for candidate in candidates:
#         if candidate['name'].lower() == name.lower():
#             return render_template('candidate.html', **candidate)

    # for cand in candidates:
    #     if x in cand["name"]:
    #        return render_template('candidate.html', candidates=candidates, cand=cand)
    #     else:
    #         return "Кандидат не найден"


@app.route("/list/")
def page_list():
    return render_template("candidates_list.html", candidates=candidates)


@app.route("/search/")
def search():
    if settings["case-sensitive"]:
        search = request.args.get('name').lower()
        if search:
            candidates_list = [cand for cand in candidates if search in cand["name"].lower()]
            if candidates_list:
                return render_template('search_list.html', count=len(candidates_list), list=candidates_list)
            else:
                return "Кандидат не найден"
        else:
            return "Введите имя кандидата"
    else:
        search = request.args.get('name')
        if search:
            candidates_list = [cand for cand in candidates if search in cand["name"]]
            if candidates_list:
                return render_template('search_list.html', count=len(candidates_list), list=candidates_list)
            else:
                return "Кандидат не найден"
        else:
            return "Введите имя кандидата"


@app.route("/skill/<sk>/")
def skill_search(sk):
    candidates_list = [cand for cand in candidates if sk.lower() in cand["skills"]]
    if candidates_list:
        return render_template('search_skills__list.html', count=len(candidates_list), list=candidates_list,
                               limit=settings["limit"])
    return "Кандидат не найден"


app.run()
