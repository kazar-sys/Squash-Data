from scipy.interpolate import interp1d
from src.config import MAX_PROMOTIONS, RAW_DATA_CLASSEMENTS, LEVELS

def process_ranking(actions):
    valid_actions_count = len([a for a in actions if not a['Expired']])
    
    promotions = [a for a in actions if a['Type'] == 'Promotion']
    promotions_sorted = sorted(promotions, key=lambda x: x['Points'], reverse=True)
    excess = max(0, len(promotions) - MAX_PROMOTIONS)
    for i in range(excess):
        actions.remove(promotions_sorted[i])

    if valid_actions_count < 12: return None
    elif 12 <= valid_actions_count <= 15: target = 12
    elif 16 <= valid_actions_count <= 19: target = 13
    elif 20 <= valid_actions_count <= 23: target = 14
    elif 24 <= valid_actions_count <= 27: target = 15
    elif 28 <= valid_actions_count <= 31: target = 16
    elif 32 <= valid_actions_count <= 35: target = 17
    else: target = 18

    pool = [dict(a) for a in actions] 
    best_actions = []
    
    while len(best_actions) < target:
        current_min = None
        min_idx = -1
        for i in range(len(pool)):
            if not pool[i]['Expired']:
                if current_min is None or pool[i]['Points'] < current_min:
                    current_min = pool[i]['Points']
                    min_idx = i
        if min_idx != -1:
            best_actions.append(pool.pop(min_idx))
        else:
            break

    moyenne = round(sum(a['Points'] for a in best_actions) / target, 2)
    
    unique_points = {}
    for r in RAW_DATA_CLASSEMENTS: unique_points[r[1]] = r[0]
    tab_x = sorted(unique_points.keys())
    tab_y = [unique_points[x] for x in tab_x]
    
    f_interp = interp1d(tab_x, tab_y, fill_value='extrapolate')
    rank = int(f_interp(moyenne).item())

    level_player, index_lvl = "N/A", 0
    for i, (low, high, lvl) in enumerate(LEVELS):
        if low <= rank <= high:
            level_player, index_lvl = lvl, i
            break
    
    percent = int(round(100 * (rank - LEVELS[index_lvl][0]) / (LEVELS[index_lvl][1] - LEVELS[index_lvl][0]), 0))

    return {
        "avg": moyenne, "rank": rank, "level": level_player, 
        "percent": percent, "index_level": index_lvl, 
        "best": best_actions, "count": valid_actions_count,
        "f_interp": f_interp, "tab_x": tab_x, "tab_y": tab_y
    }