def arithmetic_arranger(problems, solve=False):

    # Number of problems is limited to 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # Split problems into individual problems
    line1 = line2 = line3 = line4 = ""
    for problem in problems:
        try:
            [operand1, operator, operand2] = problem.split()
        except ValueError:
            return "Error: Malformed problem"

        # Check operators
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

        # Check that input is comprised of digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check that numbers are 4 digits or less
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the answer
        if operator in "+":
            answer = str(int(operand1) + int(operand2))
        elif operator in "-":
            answer = str(int(operand1) - int(operand2))
        else:
            return "Error: unknown operator (this is a bug)"

        # Create the lines for the formatting
        width = max(len(operand1), len(operand2))
        line1 += "  " + " " * (width - len(operand1)) + operand1 + "    "
        line2 += operator + " " + " " * (width - len(operand2)) + operand2 + "    "
        line3 += "-" * (width + 2) + "    "
        line4 += " " * ((width + 2) - len(answer)) + answer + "    "

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    if solve:
        arranged_problems += '\n' + line4.rstrip()

    return arranged_problems
