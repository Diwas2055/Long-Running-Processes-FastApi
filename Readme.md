# Managing Long-Running Processes with FastAPI in Python


## Introduction

- Long-running processes refer to tasks that take a significant amount of time to complete. In a traditional synchronous setup, such processes can block the entire application, leading to slow response times and poor user experience. FastAPI, being asynchronous by nature, provides a solution to this problem by allowing you to execute time-consuming tasks without blocking the main event loop.


### Here’s are 3 options than can be used: 

1. Use the `BackgroundTasks` Class: FastAPI provides the `BackgroundTasks` class, which allows you to defer the execution of certain tasks to the background while still responding to the client. This is particularly useful for tasks that don’t require an immediate response.

2. While background process can solve most problems, it comes with its own disadvantages. ,Background task merely dispatches the task to the background, triggering its execution immediately. This means that if a subsequent request arrives, the background task kicks off without regard for the completion status of the first task. This problem can be solved with `asyncio queue` . Ensuring request run in the background in the order they come in.
3. Using Rabbit MQ `Propan` - a declarative Python Messaging Framework. It's inspired by `FastAPI` and `Kombu`, simplify Message Brokers around code writing and provides a helpful development toolkit, which existed only in HTTP-frameworks world until now.

- `RabbitMQ` stands as a prominent open-source message broker software, serving as a conduit for communication among distinct components within a distributed system. It relies on the `Advanced Message Queuing Protocol (AMQP)` to facilitate efficient and dependable message exchange. RabbitMQ’s versatility, scalability, and support for a multitude of programming languages render it an appealing choice for constructing responsive and resilient distributed applications.
```bash
    ## Propan

    - `Propan` is a powerful and easy-to-use Python framework for building event-driven applications that interact with any MQ Broker. 
    - Propan - just an another one HTTP a declarative Python Messaging Framework. It's inspired by `FastAPI` and `Kombu`, simplify Message Brokers around code writing and provides a helpful development toolkit, which existed only in HTTP-frameworks world until now.

    - It's designed to create reactive microservices around `Messaging Architecture`.

    - It is a modern, high-level framework on top of popular specific Python brokers libraries, based on `pydantic` and `FastAPI`, `pytest` concepts.

    - [Github Propan](https://github.com/Lancetnik/Propan)

```