def calculate_salary(hours_worked, hourly_rate, deductions):
    """
    Calculates gross and net salary based on hours worked, hourly rate, and deductions.


    Args:
        hours_worked (int): Number of hours worked.
        hourly_rate (float): Rate per hour.
        deductions (float): Total deductions.

    Returns:
        tuple: Gross and net salary.
    """
    gross = hours_worked * hourly_rate
    net = gross - deductions if gross >= deductions else 0
    return gross, net
