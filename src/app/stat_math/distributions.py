from typing import Callable

import numpy as np
import sympy as syp

from sympy.parsing.sympy_parser import parse_expr, \
    standard_transformations, implicit_multiplication_application, convert_xor

__all__ = ['parse_distribution', 'ParserError']

PARSE_TRANSFORMATIONS = (*standard_transformations,
                         # implicit_multiplication_application,
                         convert_xor)


class ParserError(Exception):
    ...


def parse_distribution(dist_str):
    dist_expr = parse_expr(dist_str, transformations=PARSE_TRANSFORMATIONS)
    x = syp.Symbol('x')
    mean = syp.Symbol('mean')
    std = syp.Symbol('std')
    if illegal_symbols := dist_expr.free_symbols - {x, mean, std}:
        raise ParserError(f"Illegal symbols: {illegal_symbols}, only {x, mean, std} allowed.")
    cdf_expr = syp.integrate(dist_expr, (x, -syp.oo, x))
    cdf_f = syp.lambdify([x, mean, std], cdf_expr, modules=['numpy', 'scipy'])
    return cdf_f


def cramervonmises(samples: np.ndarray, cdf: Callable[[np.ndarray], np.ndarray]):
    size = samples.shape[0]
    criterion = 1 / (12 * size) + np.square(
        (2 * np.arange(1, size + 1) - 1) / (2 * size) -
        cdf(samples)[samples.argsort()]
    ).sum()
    return criterion
