#!/usr/bin/env python3

import numpy as np
import scipy.stats as stats


def read_floats_from_file(filename):
    """Reads float values from a text file, discarding negative values and values greater than 30."""
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file if 0 <= float(line.strip()) <= 31]
    return numbers, len(numbers)  # Return both the valid numbers and their count


def calculate_mean_and_ci(data):
    """Calculates the mean and 95% confidence interval for the given data."""
    mean = np.mean(data)
    n = len(data)
    if n < 2:
        return mean, (mean, mean), 0  # No confidence interval if not enough data

    # Standard error
    se = stats.sem(data)
    # Confidence interval
    ci = stats.t.interval(0.95, n - 1, loc=mean, scale=se)
    ci_width = ci[1] - ci[0]  # Calculate the width of the confidence interval

    return mean, ci, ci_width


def main():
    # Read data from files
    phase1_data, phase1_count = read_floats_from_file('phase1.txt')
    phase2_data, phase2_count = read_floats_from_file('phase2.txt')

    # Calculate mean and confidence intervals
    phase1_mean, phase1_ci, phase1_ci_width = calculate_mean_and_ci(phase1_data)
    phase2_mean, phase2_ci, phase2_ci_width = calculate_mean_and_ci(phase2_data)

    # Write results to results.txt
    with open('results.txt', 'w') as results_file:
        results_file.write(f"Phase 1:\n")
        results_file.write(f"Count: {phase1_count}\n")
        results_file.write(f"Mean: {phase1_mean:.2f}\n")
        results_file.write(f"95% Confidence Interval: ({phase1_ci[0]:.2f}, {phase1_ci[1]:.2f})\n")
        results_file.write(f"Width of Confidence Interval: {phase1_ci_width:.2f}\n\n")

        results_file.write(f"Phase 2:\n")
        results_file.write(f"Count: {phase2_count}\n")
        results_file.write(f"Mean: {phase2_mean:.2f}\n")
        results_file.write(f"95% Confidence Interval: ({phase2_ci[0]:.2f}, {phase2_ci[1]:.2f})\n")
        results_file.write(f"Width of Confidence Interval: {phase2_ci_width:.2f}\n")


if __name__ == '__main__':
    main()
