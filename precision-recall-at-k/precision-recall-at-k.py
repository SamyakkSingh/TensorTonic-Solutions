def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    top_k = set(recommended[:k])
    relevant_set = set(relevant)
    
    intersection_size = len(top_k.intersection(relevant_set))
    
    precision = intersection_size / k if k > 0 else 0.0
    recall = intersection_size / len(relevant_set) if len(relevant_set) > 0 else 0.0
    
    return [float(precision), float(recall)]