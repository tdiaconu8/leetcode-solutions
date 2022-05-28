L = [[['cheese', 'peppers'],[]],[['basil'],['pineapple']],[['mushrooms', 'tomatoes'],['basil']]]

def graph(L):
    g = {}
    for i, c_cur in enumerate(L):
        g[i] = []
        print(i)
        print(g)
        # clients précédents (déjà créés)
        for j, c_prev in enumerate(L[:i]):
            print(i,j)
            # cur client dislikes in prev client likes ?
            #ennemy = False # if cannot be client at the same time

            if list(set(c_cur[0]) & set(c_prev[1])) or list(set(c_cur[1]) & set(c_prev[0])):
                g[i].append(j)
                g[j].append(i)

    return g

print(graph(L))
print(len(L))