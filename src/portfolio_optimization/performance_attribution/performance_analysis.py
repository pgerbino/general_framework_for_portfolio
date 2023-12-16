from abc import ABC, abstractmethod

class PerformanceAttribution(ABC):
    """
    Abstract base class for performance attribution methods.
    """

    @abstractmethod
    def calculate_attribution(self, portfolio_performance, benchmark_performance):
        """
        Calculate the attribution of the portfolio's performance.

        :param portfolio_performance: Performance data of the portfolio.
        :param benchmark_performance: Performance data of the benchmark.
        :return: Attribution analysis results.
        """
        pass

    @abstractmethod
    def analyze_contributors(self, attribution_results):
        """
        Analyze the main contributors to the portfolio's performance.

        :param attribution_results: Results from the attribution analysis.
        :return: Analysis of the main contributors.
        """
        pass

    @abstractmethod
    def analyze_detriments(self, attribution_results):
        """
        Analyze the main detriments to the portfolio's performance.

        :param attribution_results: Results from the attribution analysis.
        :return: Analysis of the main detriments.
        """
        pass
