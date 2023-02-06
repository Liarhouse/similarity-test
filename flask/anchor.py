import random

anchor = {'candy':["flask/static/img/similarity/anchor/candy.jpg", '/static/img/similarity/anchor/candy.jpg', 0.35],\
    'table':["flask/static/img/similarity/anchor/table.jpg", "/static/img/similarity/anchor/table.jpg", 0.42],\
        'chair':["flask/static/img/similarity/anchor/chair.jpg", "/static/img/similarity/anchor/chair.jpg", 0.32],\
            'stick':["flask/static/img/similarity/anchor/stick.jpg", "/static/img/similarity/anchor/stick.jpg", 0.4],\
                'fan':["flask/static/img/similarity/anchor/fan.png", "/static/img/similarity/anchor/fan.png", 0.33]}
quiz = ['candy', 'table', 'chair', 'stick', 'fan']

def random_sim():
    q = random.choice(quiz)
    p_path = anchor[q][0]
    h_path = anchor[q][1]
    sim = anchor[q][2]
    return q, p_path, h_path, sim