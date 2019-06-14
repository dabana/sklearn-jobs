.. -*- mode: rst -*-

|Travis|_ |AppVeyor|_ |Codecov|_ |CircleCI|_ |ReadTheDocs|_

.. |Travis| image:: https://travis-ci.org/scikit-learn-contrib/project-template.svg?branch=master
.. _Travis: https://travis-ci.org/scikit-learn-contrib/project-template

.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/coy2qqaqr1rnnt5y/branch/master?svg=true
.. _AppVeyor: https://ci.appveyor.com/project/glemaitre/project-template

.. |Codecov| image:: https://codecov.io/gh/scikit-learn-contrib/project-template/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/scikit-learn-contrib/project-template

.. |CircleCI| image:: https://circleci.com/gh/scikit-learn-contrib/project-template.svg?style=shield&circle-token=:circle-token
.. _CircleCI: https://circleci.com/gh/scikit-learn-contrib/project-template/tree/master

.. |ReadTheDocs| image:: https://readthedocs.org/projects/skljobs/badge/?version=latest
.. _ReadTheDocs: https://skljobs.readthedocs.io/en/latest/?badge=latest

sklearn-jobs - A flexible custom framework for automating hyper-parameter optimization with Scikit-Learn Pipelines
============================================================

.. _scikit-learn: https://scikit-learn.org

**sklearn-jobs** is flexible custom framework for automating hyper-parameter optimization with Scikit-Learn Pipelines

It builds on the sklearn Pipelines tooling by providing additionnal tools for performing 
hyper-parameter tuning on (custom) estimators not compatible with the sklearn v0 Pipelines.
These estimators are mainly transformers that modify the number of samples. This [core API issue is well
well known by the sklearn community](https://github.com/scikit-learn/scikit-learn/issues/3855)
and is planned to be solved for the release of sklearn V1. Meanwhile sklearn-jobs was created to 
circumvent this issue and overcome some of the limitations it implies.
