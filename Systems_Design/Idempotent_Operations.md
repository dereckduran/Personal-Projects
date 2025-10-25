# Idempotent Operations

Idempotent operations are operations that can be applied multiple times without changing the result beyond the initial application. In other words, if an operation is idempotent, it will have the same effect whether it is executed once or multiple times.

Idempotent operations are often used in the design of network protocols, where a request to perform an operation is guaranteed to happen at least once, but might also happen more than once. If the operation is idempotent, then there is no harm in performing the operation two or more times.

It is also important to understand the benefits of idempotent operations, especially when using message or task queues that do not guarantee exactly once processing. Many queueing systems guarantee at least once message delivery or processing. These systems are not completely synchronized, for instance, across geographic regions, which simplifies some aspects of their implementation or design. Designing the operations that a task queue executes to be idempotent allows one to use a queueing system that has accepted this design trade-off.

For example, consider the Python set and its discard method. The discard method removes an element from a set, and does nothing if the element does not exist. So:

my_set.discard(x)

has exactly the same effect as doing the same operation twice:

my_set.discard(x)
my_set.discard(x)

Payments are a good example to illustrate why idempotence is useful. In the previous example, we’ve seen that the payment to R is executed multiple times because S retires without knowing that the transfer already had been successful.

If the operation was idempotent, this wouldn’t have been the case. But how does PS know that S just has retried the same payment and doesn’t want to send a second payment of $10 to S?

To achieve this, S includes an idempotence key in his request to PS. This key can be, for example, is a UUID. If PS receives a request with the same idempotence key, it knows that it’s a retry. If it hasn’t seen the key before, it knows that it’s a new request.

#### Reference
https://www.baeldung.com/cs/idempotent-operations
