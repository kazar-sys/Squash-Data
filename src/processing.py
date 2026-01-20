from datetime import datetime, timedelta
from scipy.interpolate import interp1d
from src.config import LEVEL_DATA, RAW_RANKING_DATA, MAX_PROMOTION_ACTIONS

def get_target_count(count):
    if count < 12: return 12
    mapping = { (12,15): 12, (16,19): 13, (20,23): 14, (24,27): 15, (28,31): 16, (32,35): 17 }
    for (low, high), target in mapping.items():
        if low <= count <= high: return target
    return 18

def calculate_player_rank(average_points):
    points = [row[1] for row in RAW_RANKING_DATA]
    ranks = [row[0] for row in RAW_RANKING_DATA]
    f = interp1d(points, ranks, fill_value='extrapolate')
    return int(f(average_points).item())

def get_level_info(rank):
    for low, high, lvl in LEVEL_DATA:
        if low <= rank <= high:
            percent = int(round(100 * (rank - low) / (high - low), 0))
            return lvl, percent
    return "N/A", 0