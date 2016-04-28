Given a simple sentence in the travel context such as: _i want to fly from boston at 8:38am and arrive in denver at 11:10 in the morning_, this projects aim at matching each word in the sentence to the concept, such as _airport_, _cityname_.

[Finite State Tranducer](https://en.wikipedia.org/wiki/Finite_state_transducer) is defined with the training data set.

Then [OpenFST](http://www.openfst.org/twiki/bin/view/GRM/NGramQuickTour) use the pre-built tranducer to decide on the most probable transition for the sentence. And then it output corresponding _concept_ for each term.
