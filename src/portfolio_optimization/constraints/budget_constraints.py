def check_budget_constraints(weights):
    """
    Check if the given portfolio weights satisfy the budget constraints.

    :param weights: A list or array of portfolio weights for each asset.
    :return: True if the constraints are satisfied, False otherwise.
    """
    total_allocation = sum(weights)
    non_negative = all(weight >= 0 for weight in weights)

    # The total allocation should be approximately 1 (or 100%)
    # and all weights should be non-negative.
    return abs(total_allocation - 1) < 1e-6 and non_negative
