# Bayesian statistics

[toc]

## Definition

The Statistics that analyze data by applying Bayes'  theorem.

## Orientation

In Inferential statistics, we believe that even though the population is unknown, there is the only mean or variance there. In other words, the population is the only one and sees it as stable, a stable whole, and Normal distribution is assumed. Moreover, 5% or 1% percent of the rejection region is deemed as not "accidental," but "significant," and we have used it as the basis for testing in Inferential statistics.

But Today, with so much diversified data, traditional statistical approaches have become less useful.

Bayesian statistics is different approach from Inferential statistics. Bayes statistics view the population as an unstable whole and treat it as a random variable. "updating" your data from the vast amount of data and constantly reviewing the conditions and try to get closer to the truth by repeating it. This flexible thinking is Bayes Statistics.

## Flow of Bayesian statistics

(1) The extracted sample data is treated as the only data,

(2) Set the prior probability as the subject with a little information.

(3) Establish the likelihood of the accuracy of the hypothesis based on sample data.

(4) Update the new probability i.e. posterior probability,

(5) Estimate the population,

## Bayes Theorem

\[AAAAAAAA\] and $$B$$ are events and $$P(B) \neq $



\[P(A|B)=P(A)P(B|A)P(B)P(A|B) = \frac{P(A)P(B|A)}{P(B)}\]





And Let event $$A$$ be precondition, and event $$B$$ be $$D (Data)$$ . Then
$$
P(H|D) = \frac{P(H)P(D|H)}{P(D)}
$$
This($$P(H|D)$$) means "Look for the condition under which something happened when a result was produce"

## Likelihood, Pre-test probability and Post-test probability

$$
P(H|D) = \frac{P(H)P(D|H)}{P(D)}
$$

| Name                  | Symbol   | Concept                                                 |
| --------------------- | -------- | ------------------------------------------------------- |
| Pre-test probability  | $$P(H    | D)$$                                                    |
| Post-test probability | $$P(H)$$ | Probability of precondition H before data D is obtained |
| Likelihood            | $$P(D    | H)$$                                                    |

e.g. 

The Pre-test probability( $$P(H|D)$$) is "0.05% of people suffer from a certain disease."

The post-probability is "the probability of being really affected from a certain disease when people tested positive."

The likelihood ( $$P(D|H)$$)is, "How likely are certain conditions from observations?"

## Bayes' theorem with multiple condition

$$
P(H_i|D) = \frac{P(H_i)P(D|H_i)}{P(H_1)P(D|H_1)+P(H_2)P(D|H_2)+\dotsb+P(H_n)P(D|H_n)}
$$

Regard to Independent cause $$H_1, H_2, H_3$$, We can write

$$P(D) = P(D\cap H_1)+P(D\cap H_2)+P(D\cap H_3) $$

So, From Multiplication Rule of Probability

$$P(D) = P(H_1)P(D|H_1)+P(H_2)P(D|H_2)+P(H_3)P(D|H_3)$$

Then, We substitute the above expression for the following expression,

$$P(H_1|D) = \frac{P(H_1)P(D|H_1)}{P(D)}$$

$$\rArr P(H_i|D) = \frac{P(H_i)P(D|H_i)}{P(H_1)P(D|H_1 +P(H_2)P(D|H_2)+\dotsb+P(H_n)P(D|H_n)}$$

e.g.

In one city's weather statistics, 1st day, the probability of being 'clear' per day is 20%; the probability of being 'cloudy' is 60%; and the probability of being 'rainy' is 20%. 2nd day, the probability of being 'rainy' is, The probability of 'rainy' on the 2nd is 20% when the 1st was 'clear', 50% when the 1st was 'cloudy' and 30% when the 1st was 'rain'. Find the probability that the previous day is '<u>cloudy</u>' when the 2nd is '<u>rainy</u>' in this city.

> Set $H_1$: 1st day 'clear', $H_2$: 1st day 'cloudy', $H_3$: 1st day 'rainy', $D$: 2nd day 'rainy'
>
> And we need to figure out: $P(H_2|D)$
>
> Then, $P(H_1) = 0.2, P(H_2) = 0.5, P(H_3) = 0.2, P(D|H_1) =0.2, P(D|H_2) = 0.5, P(D|H_3) = 0.3$
>
> $$\begin{equation} \begin{aligned} P(H_2|D) & = \frac{P(H_2)P(D|H_2)}{P(H_1)P(D|H_1) +P(H_2)P(D|H_2)+P(H_3)P(D|H_3)} \\ & =  \frac{0.6\times0.5}{0.2\times0.2+0.6\times0.5+0.2\times0.3} \\ & =\frac{3}{4}\end{aligned} \end{equation}$$
>
> * $P(H_1), P(H_2), P(H_3)$ are Post-test probability
> * $P(H_2|D)$ is Pre-test probability
> * $P(D|H_1) ,P(D|H_2) , P(D|H_3)$ are likelihood

## Application of Bayesian statistics

1. Spam mail Filtering (Naive Bayes filter)

First of all, Naive Bayes filter requires materials. Spam-mail filtering uses a mechanism called morpheme analysis to break mail sentences into words. And then we find the words that characterize them.

2. Noise Canceling (Kalman filter)

Apply Bayes' theorem and Bayes' updates to eliminate fluctuations in the observed data itself.

e.g. Development of in-vehicle court cameras, car navigation systems, and financial products.

3. Association Analysis

The probability that a customer who purchased a product A will purchase a product 𝐵 is calculated by calculating $𝑃 (𝐵|𝐴)$ and Draw a conclusion, "The person who bought the product 𝐴 also buys the product 𝐵."

4. Text Mining

Separate sentence data with words or clauses and retrieve analytical information such as frequency of appearance, correlation, time series, etc.

