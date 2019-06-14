import pytest

from sklearn.utils.estimator_checks import check_estimator

from skljobs import TemplateEstimator
from skljobs import TemplateClassifier
from skljobs import TemplateTransformer


@pytest.mark.parametrize(
    "Estimator", [TemplateEstimator, TemplateTransformer, TemplateClassifier]
)
def test_all_estimators(Estimator):
    return check_estimator(Estimator)
