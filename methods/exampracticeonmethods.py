"""
This is the Exercise from the instructor:
Tax in US based on state:
    Create a method, which takes the state and gross income as the argument
    and returns the net income after deduction tax based on the state.

    Assume Federal Tax = 10%
    Assume State Tax on your wish

    You don't have to do for all the states, just do 3 - 4 to solve the
    purpose of the exercise
"""

def calculateNetIncome(gross, state):
    """
    Calculate the net income after the federal and state tax
    :param gross: Gross Income
    :param state: State Name
    :return: Net Income
    """
    state_tax = {'CA': 10, 'NC': 9, 'NY': 5, 'MO': 6}

    # Calculate net income after federal tax
    net = gross - (gross * .10)

    # Calculate the income after the state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after all the heavy taxes is: " + str(net))
        return net
    else:
        print("State not in the list")
        return None

calculateNetIncome(10000, 'NC')