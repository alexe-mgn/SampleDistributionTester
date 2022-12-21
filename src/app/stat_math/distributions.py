from typing import Callable

import numpy as np
import sympy as syp

from sympy.parsing.sympy_parser import parse_expr, \
    standard_transformations, implicit_multiplication_application, convert_xor

__all__ = ['parse_distribution', 'ParserError']

PARSE_TRANSFORMATIONS = (*standard_transformations,
                         # implicit_multiplication_application,
                         convert_xor)
CRAMERVONMISES_TABLE = {0.1: 0.1035, 0.05: 0.1260, 0.01: 0.1788, 0.005: 0.2018, 0.001: 0.2559}


class ParserError(Exception):
    ...


def parse_distribution(cdf_str):
    cdf_expr = parse_expr(cdf_str, transformations=PARSE_TRANSFORMATIONS)
    x = syp.Symbol('x')
    mean = syp.Symbol('mean')
    std = syp.Symbol('std')
    if illegal_symbols := cdf_expr.free_symbols - {x, mean, std}:
        raise ParserError(f"Illegal symbols: {illegal_symbols}, only {x, mean, std} allowed.")
    cdf = np.vectorize(syp.lambdify([x, mean, std],
                                    cdf_expr,
                                    modules=['numpy', 'scipy']),
                       excluded={1, 2})

    def cdf(x: np.ndarray, mean=None, std=None, *, cdf=cdf):
        return cdf(x, mean if mean is not None else np.mean(x), std if std is not None else np.std(x))

    return cdf


def cramervonmises(samples: np.ndarray, cdf: Callable[[np.ndarray, float], np.ndarray], args=()):
    size = samples.shape[0]
    criterion = 1 / (12 * size) + np.square(
        (2 * np.arange(1, size + 1) - 1) / (2 * size) -
        cdf(samples, *args)[samples.argsort()]
    ).sum()
    return criterion
