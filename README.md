# Hand-Written Digit Recognition System

## [LIVE link](https://codepen.io/dhruv-dogra/full/wXNEXg)

## Abstract
This is a neural network which is trained to recognize hand written digits. MNIST dataset was used to train the network. Using Python we obtained our training parameters. JS, HTML and CSS were used to create user interface. Accuracy obtained was close to 93%.

## Flow Diagram

<img width="204" alt="flowdiagram" src="https://user-images.githubusercontent.com/13077629/42184586-0d119106-7e14-11e8-9345-917c9a166445.png">

## Description

### Block 1: Get an input image and process it
MNIST datapoints is made of 2 parts: image and corresponding label. Image in the dataset is present as a 2D array of size 28 * 28. The numbers in the array define pixel intensity at
that point. These arrays are flattened into a 784-
dimensional vector. The label associated with each
image is also processed and converted into a vector
of desired form. The labels store the integer which
describe the corresponding image. We shall store the
vector as ”one-hot” vector, which means that it’s
value is 1 in one dimension and is 0 in every other
dimension. For example, 2 would be represented as
[0,0,1,0,0,0,0,0,0,0].

### Block 2: Calculate evidence
This step involves creating ”evidence”, which is used
to decide to which group our image belongs. To
calculate evidence we perform weighted sum of the
pixel intensities. To this a ”bias” is added as well.
What bias does is that some output are more likely
than others. Mathematically we can express evidence
as follows: 

> Evidence[i] = Summation(Weights * Input + Biases)

### Block 3: Get probabilities
We convert the previously calculated evidence is
used to get probabilities. The evidence is fed to
”activation” function which generates a probability
distribution over 10 digits. The softmax function is
defined as follows:

<img width="201" alt="softmax exp" src="https://user-images.githubusercontent.com/13077629/42184801-bb005f2c-7e14-11e8-9d95-bb298c0a7436.png">

### Block 4: Training 
In this step our motive is minimize
our cost function. First, we cost function as a ”cross
entropy”, which is defined as follows:

<img width="192" alt="screen shot 2018-07-02 at 4 27 44 pm" src="https://user-images.githubusercontent.com/13077629/42184850-e944fef6-7e14-11e8-9a9e-35b740ac3bc2.png">

Here y is our predicted probability distribution, and
y’ is the true distribution. Backpropagation and
gradient descent algorithm is applied in order to
minimize the cost.

### Block 5: Evaluate our Model 
In this step we compare our group with highest predicted probability against
the label.

## Results

The neural network processes the image entered by the
user and assigns percentage against ten numbers ranging
from 0-9. The percentage indicates which number is most
likely drawn by the user. We output the number with the
highest percentage among all the 10 numbers.

The accuracy obtained after training and testing neural
network is as follows:

| Digit        | (Correctly Deduced Samples)/(Total Samples)           | Accuracy|
| ------------- |:-------------:| -----:|
| 0      | 954/980 | 0.973469387755 |
| 1      | 1114/1135      |   0.981497797357 |
| 2 | 936/1032      |    0.906976744186 |
| 3      | 913/1010 | 0.90396039604 |
| 4      | 936/982      |   0.953156822811 |
| 5 | 816/892      |    0.914798206278 |
| 6      | 895/958 | 0.934237995825 |
| 7      | 962/1028      |   0.93579766537 |
| 8 | 877/974      |    0.900410677618 |
| 9 | 917/1009      |    0.90882061447 |

The average accuracy comes out to be 0.931312 or 93%.
