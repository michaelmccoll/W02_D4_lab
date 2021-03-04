def get_result(final_score):
    if final_score["home score"] > final_score["away score"]:
        return "HOME WIN"
    elif final_score["home score"] < final_score["away score"]:
        return "AWAY WIN"
    else:
        return "DRAW"

def get_results(final_scores):
    return [get_result(scores) for scores in final_scores]

# ALTERNATIVE longer method...
    # score_list = []
    # for scores in final_scores:
    #     xx = get_result(scores)
    #     score_list.append(xx)
    # return score_list