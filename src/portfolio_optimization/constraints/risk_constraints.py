import numpy as np

def portfolio_variance(weights, covariance_matrix):
    """
    Calculate the variance of the portfolio.

    :param weights: A list or array of portfolio weights for each asset.
    :param covariance_matrix: The covariance matrix of the asset returns.
    :return: The variance of the portfolio.
    """
    return np.dot(weights, np.dot(covariance_matrix, weights))

def check_risk_constraints(weights, covariance_matrix, max_variance):
    """
    Check if the given portfolio satisfies the risk constraints based on variance.

    :param weights: A list or array of portfolio weights for each asset.
    :param covariance_matrix: The covariance matrix of the asset returns.
    :param max_variance: The maximum allowable variance for the portfolio.
    :return: True if the risk constraints are satisfied, False otherwise.
    """
    return portfolio_variance(weights, covariance_matrix) <= max_variance
