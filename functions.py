import json


def get_settings():
    """
    Получает из файла словарь с настройками
    """
    with open("data/settings.json", encoding="UTF-8") as file:
        return json.load(file)


def get_candidates():
    """
    Получает из файла список кандидатов
    """
    with open('data/candidates.json', encoding="UTF-8") as file:
        return json.load(file)


def get_candidate_by_id(dict_, id_):
    """
    Возвращает кандидата по id из списка
    :param dict_: список с кандидатами
    :param id_: id искомого кандидата
    :return: искомый кандидат
    """
    for candidate in dict_:
        if candidate.get("id") == id_:
            return candidate


def get_candidates_by_name(dict_, name, case_sensitive):
    """
    Ищет кандидатов по имени в списке
    :param dict_: список с кандидатами
    :param name: имя искомого кандидата
    :param case_sensitive: параметр, указывающий чувствительность к регистру
    :return: список найденных кандидатов
    """
    if case_sensitive:
        return [cand for cand in dict_ if name in cand.get("name")]
    return [cand for cand in dict_ if name.lower() in cand.get("name").lower()]


def get_candidates_by_skill(dict_, skill, limit):
    """
    Ищет кандидатов по навыку в списке.
    :param dict_: список с кандидатами
    :param skill: навык для отбора кандидатов
    :param limit: лимит количества кандидатов для просмотра
                  если отсутствует-выводит всех найденных кандидатов
    :return: список искомых кандидатов
    """
    if limit:
        return [cand for cand in dict_ if skill.lower() in cand.get("skills").lower()][:limit]
    return [cand for cand in dict_ if skill.lower() in cand.get("skills").lower()]
