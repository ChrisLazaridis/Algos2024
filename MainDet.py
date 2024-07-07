import numpy as np

# Δεδομένα
D_alpha_f_A = -2
D_beta_f_A = 1

# Gradient της συνάρτησης f στο σημείο A (θεωρητικά δεδομένα)
grad_f_A = np.array([0, 0])  # Προσαρμόστε ανάλογα το gradient της f στο σημείο Α

# Αποθηκεύουμε τις κατευθύνσεις α
alpha = np.array([0, -1])
beta = np.array([1, 1])

# Υπολογισμός των κατευθύνσεων
D_alpha = np.dot(grad_f_A, alpha)
D_beta = np.dot(grad_f_A, beta)

# Εύρεση της κατεύθυνσης του μέγιστου ρυθμού ελάττωσης
if abs(D_alpha) > abs(D_beta):
    u_max = alpha / np.linalg.norm(alpha)
else:
    u_max = beta / np.linalg.norm(beta)

print("Η κατεύθυνση του μέγιστου ρυθμού ελάττωσης είναι:", u_max)
