# Simple Viterbi Algorithm for HMM Speech Recognition

states = ['e', 'v']

observations = ['High', 'Low']

start_probability = {
    'e': 1.0,
    'v': 0.0
}

transition_probability = {
    'e': {'e': 0.6, 'v': 0.4},
    'v': {'e': 0.2, 'v': 0.8}
}

emission_probability = {
    'e': {'High': 0.7, 'Low': 0.3},
    'v': {'High': 0.1, 'Low': 0.9}
}


def viterbi(obs, states, start_p, trans_p, emit_p):

    V = [{}]
    path = {}

    # Initialize base cases
    for state in states:
        V[0][state] = start_p[state] * emit_p[state][obs[0]]
        path[state] = [state]

    # Run Viterbi algorithm
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for curr_state in states:

            (prob, state) = max(
                (V[t-1][prev_state] *
                 trans_p[prev_state][curr_state] *
                 emit_p[curr_state][obs[t]], prev_state)
                for prev_state in states
            )

            V[t][curr_state] = prob
            newpath[curr_state] = path[state] + [curr_state]

        path = newpath

    # Find the final most probable state
    n = len(obs) - 1
    (prob, state) = max((V[n][state], state) for state in states)

    return prob, path[state]


probability, sequence = viterbi(
    observations,
    states,
    start_probability,
    transition_probability,
    emission_probability
)

print("Most likely phoneme sequence:", sequence)
print("Probability:", probability)