# Communication

Network protocols are a key part of systems today, as no system can exist in isolation - they all need to communicate with each other. You should learn about the networking protocols such as HTTP, TCP, UDP. Also, learn about the architectural styles such as RPC, REST, GraphQL and gRPC.


## HTTP
HTTP is a TCP/IP-based application layer communication protocol for encoding and transporting data between a client and a server. It is a request/response protocol: clients issue requests and servers issue responses with relevant content and completion status info about the request. HTTP is self-contained, allowing requests and responses to flow through many intermediate routers and servers that perform load balancing, caching, encryption, and compression.
By default, TCP port 80 is used, but other ports can also be used. HTTPS, however, uses port 443.

A basic HTTP request consists of a verb (method) and a resource (endpoint).


## TCP/IP
TCP

TCP is a connection-oriented protocol over an IP network. Connection is established and terminated using a handshake. All packets sent are guaranteed to reach the destination in the original order and without corruption through:

    Sequence numbers and checksum fields for each packet
    @article@Acknowledgement packets and automatic retransmission

If the sender does not receive a correct response, it will resend the packets. If there are multiple timeouts, the connection is dropped. TCP also implements flow control and congestion control. These guarantees cause delays and generally result in less efficient transmission than UDP.

To ensure high throughput, web servers can keep a large number of TCP connections open, resulting in high memory usage. It can be expensive to have a large number of open connections between web server threads and say, a memcached server. Connection pooling can help in addition to switching to UDP where applicable.

TCP is useful for applications that require high reliability but are less time critical. Some examples include web servers, database info, SMTP, FTP, and SSH.

Use TCP over UDP when:

    You need all of the data to arrive intact
    You want to automatically make a best estimate use of the network throughput

## UDP
UDP is connectionless. Datagrams (analogous to packets) are guaranteed only at the datagram level. Datagrams might reach their destination out of order or not at all. UDP does not support congestion control. Without the guarantees that TCP support, UDP is generally more efficient.

UDP can broadcast, sending datagrams to all devices on the subnet. This is useful with DHCP because the client has not yet received an IP address, thus preventing a way for TCP to stream without the IP address.

UDP is less reliable but works well in real time use cases such as VoIP, video chat, streaming, and realtime multiplayer games.

Use UDP over TCP when:

    You need the lowest latency
    Late data is worse than loss of data
    You want to implement your own error correction

## RPC

In an RPC, a client causes a procedure to execute on a different address space, usually a remote server. The procedure is coded as if it were a local procedure call, abstracting away the details of how to communicate with the server from the client program. Remote calls are usually slower and less reliable than local calls so it is helpful to distinguish RPC calls from local calls. Popular RPC frameworks include Protobuf, Thrift, and Avro.

RPC is a request-response protocol:

    Client program - Calls the client stub procedure. The parameters are pushed onto the stack like a local procedure call.
    Client stub procedure - Marshals (packs) procedure id and arguments into a request message.
    Client communication module - OS sends the message from the client to the server.
    Server communication module - OS passes the incoming packets to the server stub procedure.
    Server stub procedure - Unmarshalls the results, calls the server procedure matching the procedure id and passes the given arguments.
    The server response repeats the steps above in reverse order.


## gRPC

gRPC is a robust open-source RPC (Remote Procedure Call) framework used to build scalable and fast APIs. It allows the client and server applications to communicate transparently and develop connected systems. Many leading tech firms have adopted gRPC, such as Google, Netflix, Square, IBM, Cisco, & Dropbox. This framework relies on HTTP/2, protocol buffers, and other modern technology stacks to ensure maximum API security, performance, and scalability.

In the following gRPC architecture diagram, we have the gRPC client and server sides. In gRPC, every client service includes a stub (auto-generated files), similar to an interface containing the current remote procedures. The gRPC client makes the local procedure call to the stub with parameters to be sent to the server. The client stub then serializes the parameters with the marshaling process using Protobuf and forwards the request to the local client-time library in the local machine.

The OS makes a call to the remote server machine via HTTP/2 protocol. The server’s OS receives the packets and calls the server stub procedure, which decodes the received parameters and executes the respective procedure invocation using Protobuf. The server stub then sends back the encoded response to the client transport layer. The client stub gets back the result message and unpacks the returned parameters, and the execution returns to the caller.

### Advantages
1. Performance
2. Streaming
3. Code Generation
4. Interoperability
5. Security
6. Usability and Productivity
7. Built In Commodity Features

### Dsiadvantages
1. Limited Support
2. Non Human Readable Format
3. No Edge Caching
4. Steep Learning Curve



## REST

REST is an architectural style enforcing a client/server model where the client acts on a set of resources managed by the server. The server provides a representation of resources and actions that can either manipulate or get a new representation of resources. All communication must be stateless and cacheable.

There are four qualities of a RESTful interface:

    Identify resources (URI in HTTP) - use the same URI regardless of any operation.
    Change with representations (Verbs in HTTP) - use verbs, headers, and body.
    Self-descriptive error message (status response in HTTP) - Use status codes, don't reinvent the wheel.
    HATEOAS (HTML interface for HTTP) - your web service should be fully accessible in a browser.

REST is focused on exposing data. It minimizes the coupling between client/server and is often used for public HTTP APIs. REST uses a more generic and uniform method of exposing resources through URIs, representation through headers, and actions through verbs such as GET, POST, PUT, DELETE, and PATCH. Being stateless, REST is great for horizontal scaling and partitioning.

### Disadvantage(s): REST

    With REST being focused on exposing data, it might not be a good fit if resources are not naturally organized or accessed in a simple hierarchy. For example, returning all updated records from the past hour matching a particular set of events is not easily expressed as a path. With REST, it is likely to be implemented with a combination of URI path, query parameters, and possibly the request body.
    REST typically relies on a few verbs (GET, POST, PUT, DELETE, and PATCH) which sometimes doesn't fit your use case. For example, moving expired documents to the archive folder might not cleanly fit within these verbs.
    Fetching complicated resources with nested hierarchies requires multiple round trips between the client and server to render single views, e.g. fetching content of a blog entry and the comments on that entry. For mobile applications operating in variable network conditions, these multiple roundtrips are highly undesirable.
    Over time, more fields might be added to an API response and older clients will receive all new data fields, even those that they do not need, as a result, it bloats the payload size and leads to larger latencies.

## GraphQL 

Query language and runtime for building APIs. It allows clients to define the structure of the data they need and the server will return exactly that. This is in contrast to traditional REST APIs, where the server exposes a fixed set of endpoints and the client must work with the data as it is returned.

#### References
https://cs.fyi/guide/http-in-depth
https://www.howtographql.com/basics/3-big-picture/
https://www.redhat.com/en/topics/api/what-is-graphql
