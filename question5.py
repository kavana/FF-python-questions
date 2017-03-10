def apply_operation(left_operand, right_operand, operator):
    result = 0
    exec('result = {0} {1} {2}'.format(str(left_operand), str(right_operand), operator))
    return result

if __name__ == "__main__":
    print apply_operation(2, '-', 3)