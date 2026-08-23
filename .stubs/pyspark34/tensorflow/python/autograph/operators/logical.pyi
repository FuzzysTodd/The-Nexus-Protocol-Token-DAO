from tensorflow.python.framework import tensor_util as tensor_util
from tensorflow.python.ops import control_flow_ops as control_flow_ops, gen_math_ops as gen_math_ops

def not_(a):
    '''Functional form of "not".'''
def and_(a, b):
    '''Functional form of "and". Uses lazy evaluation semantics.'''
def or_(a, b):
    '''Functional form of "or". Uses lazy evaluation semantics.'''
def eq(a, b):
    '''Functional form of "equal".'''
def not_eq(a, b):
    '''Functional form of "not-equal".'''
