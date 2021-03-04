def latest_score(scores):
    last_score = scores[-1]
    return last_score

def personal_best(scores):
    return max(scores)

#changing and reassinging the actual scores list = could be bad if you want to use the scores later on i.e get the latest score 
# def personal_top_three(scores):
#     scores.sort(reverse=True)
#     return scores[0:3]

# creating a new list of the sorted list = the original data NOT mutated
def personal_top_three(scores):
    sorted_scores = sorted(scores)
    return sorted_scores[-3:][::-1]

def highest_to_lowest(scores):
    scores.sort(reverse=True)
    return scores

