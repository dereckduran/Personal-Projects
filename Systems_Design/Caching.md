# Caching

Caching is the process of storing frequently accessed data in a temporary storage location, called a cache, in order to quickly retrieve it without the need to query the original data source. This can improve the performance of an application by reducing the number of times a data source must be accessed.

Caching is suitable for frequently accessed data without negatively affecting data integrity or application functionality. Common use cases include serving static assets like images, stylesheets, and scripts, caching database queries or API responses, and caching pages or content for dynamic web apps. However, consider the caching strategy for each app and regularly refresh or invalidate cached content to avoid serving stale content.



## Cache Types

### In-memory caching

In-memory caching is a type of caching that involves storing data in the computer’s RAM (Random Access Memory) instead of in a database or on disk. This type of caching is useful for applications that require high-speed access to data, such as web servers and databases. In-memory caching can significantly improve the performance of an application by reducing the number of database queries and disk reads required to retrieve data. However, it is important to note that in-memory caching is volatile and the data stored in the RAM may be lost if the system is shut down or restarted.

Example: Imagine you have a web application that frequently needs to retrieve a list of products from a database. You could use in-memory caching to store the list of products in memory after the first retrieval, so that subsequent requests for the same data can be served directly from memory instead of hitting the database each time.


### Distributed caching

Distributed caching is a type of caching that involves storing data across multiple servers or nodes in a network. This type of caching is useful for applications that require high availability and scalability. Distributed caching allows multiple servers to share the workload of storing and retrieving data, which can improve the performance of the application and reduce the risk of data loss. However, managing a distributed caching system can be complex, and ensuring consistency across multiple nodes can be challenging.

Example: Let’s say you have a large-scale e-commerce website that serves customers all over the world. To ensure that product information is readily available to customers no matter where they are located, you could use a distributed caching solution such as Redis or Memcached to store product data in memory across multiple servers in different regions. This would help reduce latency and improve overall site performance.

### Client-side caching

Client-side caching is a type of caching that involves storing data on the client’s device, such as a web browser. This type of caching is useful for web applications that require frequent access to static resources, such as images and JavaScript files. Client-side caching can significantly improve the performance of a web application by reducing the number of requests made to the server. However, it is important to note that client-side caching can lead to issues with stale data, as the cached data may not always be up-to-date. Therefore, careful consideration should be given to the caching policies and expiration times used in client-side caching.

Example: Imagine you have a web application that frequently displays images or other static content that doesn’t change very often. You could use client-side caching to store the images in the user’s browser cache after the first retrieval, so that subsequent requests for the same content can be served directly from the cache instead of having to download the content again from the server. This can help improve page load times and reduce network traffic.

### Web Server Caching

Reverse proxies and caches such as Varnish can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.

### Application Caching

In-memory caches such as Memcached and Redis are key-value stores between your application and your data storage. Since the data is held in RAM, it is much faster than typical databases where data is stored on disk. RAM is more limited than disk, so cache invalidation algorithms such as least recently used (LRU) can help invalidate 'cold' entries and keep 'hot' data in RAM.

Redis has the following additional features:

    Persistence option
    Built-in data structures such as sorted sets and lists

Generally, you should try to avoid file-based caching, as it makes cloning and auto-scaling more difficult.

## Caching strategies:

Refresh Ahead
You can configure the cache to automatically refresh any recently accessed cache entry prior to its expiration.

Refresh-ahead can result in reduced latency vs read-through if the cache can accurately predict which items are likely to be needed in the future.
Disadvantage of refresh-ahead:

    Not accurately predicting which items are likely to be needed in the future can result in reduced performance than without refresh-ahead.


Read Through
In this strategy, the cache is used as the primary data source. When data is requested, the cache is checked first. If the data is not in the cache, it is retrieved from the database and stored in the cache for future use. This strategy can be useful when the database is slow or when data is frequently read but rarely updated.

Write-Behind
In write-behind, the application does the following:

    Add/update entry in cache
    Asynchronously write entry to the data store, improving write performance

Disadvantages of write-behind:

    There could be data loss if the cache goes down prior to its contents hitting the data store.
    It is more complex to implement write-behind than it is to implement cache-aside or write-through.


Write-through
In this strategy, data is written to both the cache and the database at the same time. When data is updated, it is written to the cache and the database simultaneously. This ensures that the cache always contains up-to-date data, but it can slow down write operations.

Cache Aside
In this strategy, the application is responsible for managing the cache. When data is requested, the application checks the cache first. If the data is not in the cache, it is retrieved from the database and stored in the cache for future use. This strategy is simple and flexible, but it requires careful management of the cache to ensure that it remains up-to-date.
Disadvantages

    When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database. Cache-aside in conjunction with write through can mitigate this issue.
    Most data written might never be read, which can be minimized with a TTL.


Also, you can have the cache in several places, examples include:

    Client Caching
    CDN Caching
    Web Server Caching
    Database Caching
    Application Caching


#### References
https://medium.com/@mmoshikoo/cache-strategies-996e91c80303