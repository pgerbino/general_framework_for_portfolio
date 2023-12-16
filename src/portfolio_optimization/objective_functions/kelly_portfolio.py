def kelly_criterion(win_prob, win_return, loss_return):
    """
    Calculate the optimal portfolio percentage to allocate to an asset based on the Kelly criterion.

    :param win_prob: The probability of a positive return (a number between 0 and 1).
    :param win_return: The return if the investment is successful (as a decimal, e.g., 0.05 for 5%).
    :param loss_return: The return if the investment is unsuccessful (as a decimal, e.g., -0.05 for -5%).
    :return: The fraction of the portfolio to allocate to the asset.
    """
    return (win_prob * win_return - (1 - win_prob) * abs(loss_return)) / win_return

