def bayes(p_A, p_B_given_A, p_notB_given_notA):
    ## TODO: Calculate the posterior probability
    ## and change this value
    posterior = -1 / ((((1 - p_A) * p_notB_given_notA - 1 + p_A) / (p_B_given_A * p_A)) - 1)

    return posterior

print bayes(0.3, 0.7, 0.9)
