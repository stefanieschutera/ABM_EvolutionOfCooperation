# ABM_EvolutionOfCooperation

## WHAT IS IT?
This model demonstrates how a population can evolve high levels of altruism in a structured population with or without the presence of social parasites. In this model, population is structured as a ring and agents may interact with others along the ring determined by the global variable neighborhood_radius. 


## HOW IT WORKS
The world is populated with [population_size] agents arrayed along a ring, each of which has three attributes: a [tag], a [tolerance], and a [cheater_flag]. [tag] and [tolerance] values are initially randomly drawn, with uniform distribution, from [0,1]. [cheater_flag] is initially FALSE for all agents (meaning that they are not cheaters).

During each generation, every agent of the population randomly selects [pairings] partners, with replacement, from its neighborhood with which to interact. During an interaction, the selecting agent assess how similar it is to its partner. It does this by comparing the difference between their [tag] values and the selecting agent's threshold of allowable differnce, or [tolerance]. If they are sufficiently similar, the selecting agent pays [cost] and the partner receives [benefit]. If they are not sufficiently similar, nothing changes and the interaction ends.

Selection takes place via a tournament in which each agent randomly selects a partner from its neighborhood with which to compare [fitness], which is just the sum of [cost] and [benefit] accumulated during the generation. The agent with the higher fitness copies its [tag] and [tolerance] values to the child of the selecting agent.

Mutation is applied separately to each agent attribute (tag and tolerance) with a probability of [mutation_rate]. If [tag] is mutated, it is replaced with a new random value from the uniform distribution [0,1]. If the [tolerance] is mutated, Gaussian noise with mean 0 and standard deviation of 0.01 is added to the existing value. If this causes [tolerance] to drop below [minimum_tolerance], [tolerance] is set to equal [minimum_tolerance]. If [cheater_flag] is mutated, it simply flips its binary state. However, if [social_parasite_type] = "strong" then this mutation can only change [cheater_flag] from FALSE to TRUE.

Monitors track how frequently a donation - synonymous with an act of altruism - takes place within the population.


## HOW TO USE IT
Enter a desired population size. This will create a ring network. For this network select a neighborhood_size which determines how far along the ring that an agent may interact with other agents. 


## RELATION TO PUBLISHED WORK
This is the model used to present results in [1] and [2]. In those cases the [social_parasite_type] was not none, meaning that cheaters were present.

When [social_parasite_type] is set to none, all of the following apply:

If agents can interact along the entire ring and minimum_tolerance = 0, the model replicates that presented in [3] (with the  selection routine corrected as per [4]).

If instead, minimum_tolerance = 1x10E-6, the model replicates [5], which was a response to [4]. 

By reducing the neighborhood_radius such that agents can only interact with a subset of the entire population, the model replicates [6].


References:
[1] Shutters & Hales (2013). "Tag-Mediated Altruism is Contingent on How Cheaters Are Defined", J. Artif. Societ. Soc. Simul. 16:4, http://jasss.soc.surrey.ac.uk/16/1/4.html

[2] Shutters & Hales (2015). "Altruism displays a harmonic signature in structured societies", J. Artif. Societ. Soc. Simul. In Press.

[3] Riolo, Cohen & Axelrod (2001). "Evolution of cooperation without reciprocity", Nature 414:441-443

[4] Edmonds & Hales (2003). "Replication, Replication and Replication: Some Hard Lessons from Model Alignment", J. Artif. Societ. Soc. Simul. 6:11, http://jasss.soc.surrey.ac.uk/6/4/11.html

[5] Roberts & Sherratt (2002). "Does similarity breed cooperation?", Nature 418:499-500.

[6] Spector & Klein (2006). "Genetic stability and territorial structure facilitate the evolution of tag-mediated altruism", Artif. Life 12:553-560.
