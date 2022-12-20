import sympy as syp

from sympy.parsing.sympy_parser import parse_expr, \
    standard_transformations, implicit_multiplication_application, convert_xor

__all__ = ['parse_distribution', 'ParserError']

PARSE_TRANSFORMATIONS = (*standard_transformations, implicit_multiplication_application, convert_xor)


class ParserError(Exception):
    ...


def parse_distribution(dist_str):
    dist_expr = parse_expr(dist_str, transformations=PARSE_TRANSFORMATIONS)
    x = syp.Symbol('x')
    if illegal_symbols := dist_expr.free_symbols - {x}:
        raise ParserError(f"Illegal symbols: {illegal_symbols}, only {x} allowed.")
    dist_f = syp.lambdify([x], dist_expr, modules=['numpy'])
    return dist_f
