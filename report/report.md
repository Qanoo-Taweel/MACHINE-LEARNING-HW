# HMM Speech Recognition Report

## Introduction

Speech recognition systems attempt to determine spoken words from audio signals. In this homework, we implement a simple speech recognition model using a Hidden Markov Model (HMM).

## Model Description

The hidden states represent phonemes of the word:

e , v

The observation sequence represents frequency levels detected by a microphone:

High, Low

The model uses:

* Initial probabilities
* Transition probabilities
* Emission probabilities

## Viterbi Algorithm

The Viterbi algorithm is used to compute the most likely sequence of hidden states that generated the observations.

Observation sequence:

High → Low

Possible sequences:

e → e

e → v

Probability calculations:

P(e→e) = 0.7 × 0.6 × 0.3 = 0.126

P(e→v) = 0.7 × 0.4 × 0.9 = 0.252

Since 0.252 is larger, the most likely phoneme sequence is:

e → v

## Conclusion

Using the Viterbi algorithm, we determined that the most probable phoneme sequence for the observation High → Low is:

e → v

This demonstrates how Hidden Markov Models can be used for simple speech recognition tasks.



Discussion Questions

1. Effect of Noise on Emission Probabilities

Noise in speech signals can distort the acoustic features detected by the system. In a Hidden Markov Model, emission probabilities represent the likelihood of observing a certain sound given a phoneme state. When noise is present, the observed signal may not accurately represent the true phoneme. This can reduce the reliability of emission probabilities and lead to incorrect phoneme predictions.

2. Why Deep Learning is Preferred in Large Systems

The Viterbi algorithm works well for small HMM models with limited vocabulary. However, real speech recognition systems must handle thousands of words, different accents, speaking speeds, and background noise. Deep learning models can learn complex patterns from large datasets and generalize better to real-world speech. For this reason, modern speech recognition systems often use deep neural networks instead of simple HMM-based approaches.
