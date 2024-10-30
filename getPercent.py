
def get_percent(score:float|int, total_score:int|float = 100) -> float|int:
    '''
    It returns the score in percentage\n
    parameter score is required\n
    parameter total score has a defualt of 100

    '''
    score_in_percent = (score/total_score) * 100
    return score_in_percent

