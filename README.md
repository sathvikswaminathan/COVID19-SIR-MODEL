# COVID19-SIR-MODEL
SIR Model to predict the number of COVID-19 cases.

## Building an SIR Model based on some analysis done on data online related to the COVID-19 pandemic.

### Here I try to explain how I went about building this Model

Mathematical Models can be used to represent how variables in the real world behave.

During a pandemic like the one that we are enduring right now, it becomes important to model the spread 
of the virus as it can help extrpolate the current data we have about the outbreak to predict the future.
We are interested in various variables such as the number of infected cases per day. We shall come up with a model that can acheive this.

Let's try to come up with a simple model that can represent the number of infected individuals per day.
Let's make the assumption that on Day 0, only 1 person has been infected. Now, let us assume that this person affects 2 more susceptible people per day (A reasonable assumption since the estimated **Reproductive Number** for COVID-19 is around 2).

So, the number of people infected on Day 1 would be 2 and the number of people infected on Day 2 would be 4 and so on.

1, 2, 4 -> Geometric progression.

If we had to represent the number of infected individuals on Day N, it'd be 2<sup>N</sup>.

Let's graph this!

![](/Images/desmos-graph.png)

Clearly this is wrong because the curve only increases exponentially and ends up leaving the entire population infected.

Epidemics have a characteristic "shape"

Let's have a look at a few graphs related to different epidemics in the past:

Spanish Flu:

![](/Images/image.png)

(Source: Google Images)

Ebola:

![](/Images/ebola.png)

(Source: Google Images)

All the epidemic curves represent a bell curve. This is true for almost all the epidemics that we have encountered in the past.

Therefore we need to refine our model to make it more realistic.
There are a variety of predefined models out there that are used to model epidmeics.
We shall look at the simple **SIR** model.

## SIR MODEL

In this model people are divided into three categories or compartments:

* **Susceptible (S)**

Those who are not immune to the infection and are susceptible to getting infected

* **Infected (I)**

Those who have been infected

* **Recovered/Removed (R)**

Those who can no longer spread the disease. These are people who have either recovered from the disease and gained immunity or those who have died.

These three quantities are goverend by the below given set of differential equations: 

![](/Images/sir_differential.jpg)

(Source: Google Images)

Let's understand them!

In any chosen province, people belong to one of the 3 categories.
Initially everyone belongs to the Susceptible category because generally no one is immune to the virus.

* Now, a susceptible person getting infected depends on how much interaction there is between the two categories.
Hence it makes sense to say that rate of change of people in **S** is directly proportional to -(**S** **I**) because more the people in both categories, more the interactions. This proportionality can be removed by introducing a constant **β** which is also known as the transmission rate. This what the first equation says!

* Since a portion of the **S** category get infected, they move to the **I** category. This is what the first part of the 2nd equation says. Now, some of the infected people recover or die and move to the **R** category. Let's say the recovery period of COVID-19 is roughly 30 days. This means roughly everyday 1/30 of a person recovers. And **I** people can get recovered. So, number of people recovering per day is (1/30)**I**. This is what the second part of the second equation says. **γ** can be considered the reciprocal of the infectious period.

* Since a portion of the **I** category recover, they move to the **R** category. This is what the third equation says!

How can we implement this in code?

We want to graph the number of infected cases against time.

### Algorithm
Let us look at the algorithm for the SIR model:

Number of Infected people on Day 0 can be assumed to be 1. (depends on what time you choose)

**I0** = 1

Let **N** denote the total population

* **S0** = **N** - **I0**

* **R0** = 0

* **LOOP**
   
   This can be done using the **scipy.integrate.odeint** module


   
   **Compute dS**
   
   **Compute dI**
   
   **Compute dR**

   **S(t+1)** = **S(t)** + **dS**
   
   **I(t+1)** = **I(t)** + **dI**
   
   **R(t+1)** = **R(t)** + **dR**

* Plot(**I(t)**, t)

Hmm, but what about the constants **β** and **γ**?

We need to look at how to estimate these parameters.

## SIR Model Parameter Estimation

Our main focus here is the number of infected cases. So, we must be able to predict it accurately.

We can initialise our parameters **β** and **γ** to some random values and our algorithm will spit out the vector **I** containing the predicted number of cases per day. But obviously this is going to be wrong since our parameters were randomly initialized.

Now, we can compute the Mean Squared Error or the **MSE** of **I** using the actual number of infected cases as training data.

Now, our aim is to minimize the **MSE** because we want the number of infected cases to fit well with the real world data.

Changing the **MSE** would require a change in the parameters **β** and **γ** as all the other variables are either constants or computed in the algorithm.

We can use the **scipy.optimize.minimize** module to minimize the **MSE** and it'll return the minimized value of the **MSE** and also the the values of **β** and **γ** at which this is acheived. 

That's it! We have estimated the values of **β** and **γ**.

Now, we can plug in these values into the algorithm and voila! We get an epidemic curve predicitng the future.

## Let's test our algorithm now!

You must have realised by now that availability of data is a necessity for this algoritm to work as it is used to estimate the model parameters. Even a small change in these parameters can sometimes lead to a big difference.

Unfortunately India hasn't been doing a lot of testing and we have very little / inaccurate data at hand. Using the data that I have access to, I went ahead and ran the algortihm.

This is the graph I obtained using India's data:

![](/Images/IndiaCOVID.png)

For the reasons mentioned above, this graph is not reliable.

Iceland on the other hand is one of the few countries which has been actively testing its population. Around 10% of it's population has already been tested.

This is the graph I obtained using Iceland's data:

![](/Images/IcelandCOVID.png)

You can see that it has done a fairly good job on predicting the number of cases on untrained data.

This graph gives us information about how long it'll take it to hit the peak number of cases. This can help hospitals and medical facillities prepare themselves accordingly. 

Once the peak has been hit, the graph goes down and the epidemic ends! :)

What happens when we wash hands, practise social distancing and all that good stuff? It brings down the value of **β**, the transmission rate. 

What happens when proper medicine becomes available and everyone has access to it? It increases the value of **γ**.

The reproductive number, **R0** is defined as **β** / **γ** .

Hence, by following the **WHO** Guidleines, we are essentially bringing down the value of **R0** and flattening the curve.

For reference, this is how the value of **R0** effects the shape of the curve

![](/Images/effectofR0.png)

(Source: Google Images)

It is evident that as **R0** decreases, the curve flattens. 

Why is that a good thing? As the curve flattens, the infection is spread over a longer period of time and the number of infections per day decrease and hence can enable the hospitals and medical facillities to approach this situation in a more efficient manner.

**END**
