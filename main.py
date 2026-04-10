import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

# TRUE VALUES
true_mu = 150.0
true_sigma = 10.0
n_obs = 50

np.random.seed(42)
data = true_mu + true_sigma * np.random.randn(n_obs)

# FUNCTIONS
def log_likelihood(theta, data):
    mu, sigma = theta
    if sigma <= 0:
        return -np.inf
    return -0.5 * np.sum(((data - mu) / sigma)**2 + np.log(2 * np.pi * sigma**2))

def log_prior(theta):
    mu, sigma = theta
    if 0 < mu < 300 and 0 < sigma < 50:
        return 0.0
    return -np.inf

def log_probability(theta, data):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data)

# MCMC
initial = [140, 5]
n_walkers = 32
pos = initial + 1e-4 * np.random.randn(n_walkers, 2)

sampler = emcee.EnsembleSampler(n_walkers, 2, log_probability, args=(data,))
sampler.run_mcmc(pos, 2000, progress=True)

flat_samples = sampler.get_chain(discard=500, thin=15, flat=True)

# CALCULATE RESULTS
mu_median = np.percentile(flat_samples[:, 0], 50)
mu_low = np.percentile(flat_samples[:, 0], 16)
mu_high = np.percentile(flat_samples[:, 0], 84)

sigma_median = np.percentile(flat_samples[:, 1], 50)
sigma_low = np.percentile(flat_samples[:, 1], 16)
sigma_high = np.percentile(flat_samples[:, 1], 84)

print("MU:", mu_median, mu_low, mu_high)
print("SIGMA:", sigma_median, sigma_low, sigma_high)

# SAVE PLOT
fig = corner.corner(flat_samples, labels=["mu", "sigma"], truths=[true_mu, true_sigma])
plt.savefig("results.png")
plt.show()
