from abc import ABC, abstractmethod

class ForecastingMethod(ABC):
    """
    Abstract base class for forecasting methods.
    """

    @abstractmethod
    def fit(self, data):
        """
        Fit the forecasting model to the data.

        :param data: The historical data to fit the model.
        """
        pass

    @abstractmethod
    def predict(self, future_periods):
        """
        Predict future values using the fitted model.

        :param future_periods: Number of future periods to predict.
        :return: Predicted values for the future periods.
        """
        pass

    @abstractmethod
    def evaluate(self, actual, predicted):
        """
        Evaluate the accuracy of the predictions.

        :param actual: Actual observed values.
        :param predicted: Predicted values from the model.
        :return: A metric or set of metrics evaluating prediction accuracy.
        """
        pass
    