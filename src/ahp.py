import numpy as np
import pandas as pd

class AHP:
    def __init__(self, criteria, pairwise_matrix):
        self.criteria = criteria
        self.n = len(criteria)
        self.matrix = np.array(pairwise_matrix, dtype=float)

    def normalize_matrix(self):
        self.col_sum = self.matrix.sum(axis=0)
        self.normalized_matrix = self.matrix / self.col_sum
        return pd.DataFrame(self.normalized_matrix, columns=self.criteria, index=self.criteria)

    def calculate_priority_vector(self):
        self.priority_vector = self.normalized_matrix.mean(axis=1)
        return pd.Series(self.priority_vector, index=self.criteria, name="Priority")

    def consistency_ratio(self):
        weighted_sum = np.dot(self.matrix, self.priority_vector)
        lambda_max = np.mean(weighted_sum / self.priority_vector)
        ci = (lambda_max - self.n) / (self.n - 1)
        RI_dict = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
        ri = RI_dict.get(self.n, 1.49)
        cr = ci / ri if ri != 0 else 0
        return {
            "lambda_max": round(lambda_max, 4),
            "CI": round(ci, 4),
            "RI": ri,
            "CR": round(cr, 4),
            "consistency": "Acceptable" if cr < 0.10 else "NOT Acceptable"
        }
