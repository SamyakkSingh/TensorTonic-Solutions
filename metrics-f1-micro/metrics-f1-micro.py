def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
    fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt != yp)
    fn = fp  # In single-label multiclass, total FP always equals total FN
    
    denominator = (2 * tp) + fp + fn
    if denominator == 0:
        return 0.0
        
    f1 = (2 * tp) / denominator
    return round(float(f1), 4)