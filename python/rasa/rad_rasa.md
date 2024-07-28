# Reference

[RASA Docs](https://rasa.com/docs/rasa/action-server/)

# Overview


**Rasa Open Source**  
An open source conversational AI platform that allows you to understand and hold conversations, and connect to messaging channels and third party systems through a set of APIs.  
It supplies the building blocks for creating virtual (digital) assistants or chatbots.  

**Rasa Pro**  
The commercial, pro-code offering of Rasa that’s built to address enterprise needs around security, observability and scale  
Rasa Pro integrates seamlessly with enterprise technology stacks and is the recommended platform for all Rasa enterprise customers  

**Rasa CLI**  
*Reference* [Rasa CLI](https://rasa.com/docs/rasa/command-line-interface)  
| Command | Description |
| ----------- | ----------- |
| `rasa init` | Creates a new project with example training data, actions, and config files |
| `rasa train` | Trains a model using your NLU data and stories, saves trained model in `./models` |
| `rasa interactive` | Starts an interactive learning session to create new training data by chatting to your assistant |
| `rasa shell` | Loads your trained model and lets you talk to your assistant on the command line|
| `rasa run` | Starts a server with your trained model |
| `rasa run actions` | Starts an action server using the Rasa SDK |
| `rasa visualize` | Generates a visual representation of your stories |
| `rasa test` | Tests a trained Rasa model on any files starting with `test_` |
| `rasa export` | Exports conversations from a tracker store to an event broker |
| `rasa license` | Display licensing information |
| `rasa -h` | Shows all available commands|  

**Rasa Terminologies**  
*Reference* [Rasa Glossary](https://rasa.com/docs/rasa/glossary)  
| Terms | Description |
| ----------- | ----------- |
| Action | A single step that a bot takes in a conversation (e.g. calling an API or sending a response back to the user). |
| Custom Action | An action written by a bot developer that can run arbitrary code, mainly to interact with external systems and APIs |
| Default Action | A built-in action that comes with predefined functionality |
| Annotation | Adding labels to messages and conversations so that they can be used to train a model |
| Chitchat | A conversation pattern where the user says something that isn't directly related to their goal |
| Conversation-Driven Development (CDD) | The process of using user messages and conversation data to influence the design of an assistant and train the model, combined with engineering best practices. There are 6 steps that make up CDD: Share, Review, Annotate, Fix, Track, and Test. |
| Dual Intent and Entity Transformer (DIET) | The default NLU architecture used by Rasa, which performs both intent classification and entity extraction |
| Domain | Defines the inputs and outputs of an assistant. It includes a list of all the intents, entities, slots, actions, and forms that the assistant knows about |
| Entity | Keywords that can be extracted from a user message (a phone number, a person's name, a location, a product name, ...) |
| Event | Something that happens in a conversation.  Ex: `UserUttered` event represents a user entering a message |
| Form | A type of custom action that asks the user for multiple pieces of information |
| Intent | In a given user message, the thing that a user is trying to convey or accomplish (e,g., greeting, specifying a location) |
| Natural Language Generation (NLG) | The process of generating natural language messages to send to a user |
| Natural Language Understanding (NLU) | Parsing and understanding human language into a structured format |
| Pipeline | The list of NLU components that defines a Rasa assistant’s NLU system.  A user message is processed by each component one by one, before returning the final structured output |
| NLU Component | An element in the Rasa NLU pipeline that processes incoming messages.  Components perform tasks ranging from entity extraction to intent classification to pre-processing |
| REST Channel | A messaging channel used to build custom connectors. Includes an input channel, where user messages can be posted to Rasa, and the ability to specify a callback URL, where the bot’s response actions will be sent |
| Rules | Special training data to specify rule-like behavior, where a specific condition always predicts a specific next action |
| Slot | A key-value store that Rasa uses to track information over the course of a conversation |
| Story | Training data format for the dialogue model, consisting of a conversation between a user and a bot.  The user's messages are represented as annotated intents and entities.  The bot’s responses are represented as a sequence of actions |
| Tracker | Rasa component that maintains the state of the dialogue, which is represented as a JSON object listing the events from the current session |  

# Deploying a Rasa Assistant  

**When to deploy**  
The best time to deploy an assistant and make it available to test users is once it can handle Minimum Viable Assisstant.  
*Minimum Viable Assistant*: A basic assistant that can handle the most important happy path stories.  

**Recommended Deployment Method**  
[Rasa Helm Chart](https://github.com/RasaHQ/helm-charts/tree/main/charts/rasa) is the production-ready method to deploy your assistant on a Kubernetes or Openshift cluster.  

*Deployment Guide*: [Deploy Rasa](https://rasa.com/docs/rasa/deploy/deploy-rasa/)

To install the Rasa Helm Chart, you need an existing Kubernetes cluster or OpenShift cluster. 

Can get a managed cluster from a cloud provider like:
- Google Cloud
- DigitalOcean
- Microsoft Azure
- Amazon EKS

Deployment for development and testing:
- Running an assistant locally on the [command line](https://rasa.com/docs/rasa/command-line-interface#rasa-run)
- Developing an assistant in a [Docker container](https://rasa.com/docs/rasa/docker/building-in-docker)
- Deploying an assistant with [Docker Compose](https://rasa.com/docs/rasa/docker/deploying-in-docker-compose)  


# Rasa Architecture
![Architecture](rasa_arch.png)  

**Primary Components:** Natural Language Understanding (NLU) and Dialogue Management.  

**Natural Language Understanding (NLU)**  
Handle intent classification, entity extraction, and response retrieval.  
It's shown as the NLU Pipeline because it processes user utterances using an NLU model that is generated by the trained pipeline.  

**Dialogue Management**  
Decide the next action in a conversation based on the context.  
This is displayed as the Dialogue Policies in the diagram.  

## Tracker Store  

Assistant's conversations are stored within a tracker store.  
Rasa provides implementations for different store types and custom store
1. **InMemoryTrackerStore (default)**
    - `InMemoryTrackerStore`
    - Used if no other tracker store is configured. 
    - It stores the conversation history in memory.
    - The entire history is lost if Rasa server is restarted.
    - No configuration is needed to use the `InMemoryTrackerStore`

2. **SQLTrackerStore**
    - `SQLTrackerStore`
    - Used to store assistant's conversation history in an SQL database.
    - Compatible databases: `PostgreSQL` `Oracle > 11.0` `SQLite`

3. **RedisTrackerStore**
    - `RedisTrackerStore`
    - Store assistant's conversation history in Redis
    - Redis is a fast in-memory key-value store which can optionally also persist data.

4. **MongoTrackerStore**
    - `MongoTrackerStore`
    - Store assistant's conversation history in MongoDB
    - MongoDB is a free and open-source cross-platform document-oriented NoSQL database.

5. **DynamoTrackerStore**
    - `DynamoTrackerStore`
    - Store assistant's conversation history in DynamoDB
    - DynamoDB is a hosted NoSQL database offered by Amazon Web Services (AWS).

6. **Custom Tracker Store**  
    - To write a custom tracker store, extend the TrackerStore base class.

7. **Fallback Tracker Store**
    - When the primary tracker store configured in `endpoints.yml` becomes unavailable
    - The rasa agent will issue an error message and fall back on the `InMemoryTrackerStore` implementation. 
    - A new dialogue session will be started for each turn, which will be saved separately in the `InMemoryTrackerStore` fallback.

## Lock Store  

Rasa uses a ticket lock mechanism to ensure that incoming messages for a given conversation ID are processed in the right order, and locks conversations while messages are actively processed.  

This means multiple Rasa servers can be run in parallel as replicated services, and clients do not necessarily need to address the same node when sending messages for a given conversation ID.  
1. **InMemoryLockStore (default)**
    - `InMemoryLockStore`
    - The default lock store. It maintains conversation locks within a single process.
    - This lock store should not be used when multiple Rasa servers are run parallel.
    - To use the `InMemoryTrackerStore` no configuration is needed.

2. **ConcurrentRedisLockStore**
    - `ConcurrentRedisLockStore`
    - Rasa Pro Only
    - Use Redis as a persistence layer for instances of issued tickets and the last issued ticket number.

3. **RedisLockStore**
    - `RedisLockStore `
    - Maintain conversation locks using Redis as a persistence layer. 
    - This is the recommended lock store for running a replicated set of Rasa servers.

4. **Custom Lock Store**
    - Extend the base class `LockStore`  

## Event Broker  

An event broker allows you to connect your running assistant to other services that process the data coming in from conversations.  

The event broker publishes messages to a message streaming service, also known as a message broker, to forward Rasa Events from the Rasa server to other services.  

**Format**  
All events are streamed to the broker as serialized dictionaries every time the tracker updates its state.  
An example from `default` tracker  
```
{
    "sender_id": "default",
    "timestamp": 1528402837.617099,
    "event": "bot",
    "text": "what your bot said",
    "data": "some data about e.g. attachments"
    "metadata" {
          "a key": "a value",
     }
}
```  
1. **Pika Event Broker**
    - Use [Pika](https://pika.readthedocs.io/en/stable/), the Python client library for RabbitMQ.  
    - RabbitMQ is the default event broker

2. **Kafka Event Broker**
    - Use the [confluent-kafka](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#) library, a Kafka client written in Python
    - Need a running Kafka server.  

3. **SQL Event Broker**  
    - Use an SQL database as an event broker
    - Connections to databases are established using [SQLAlchemy](https://www.sqlalchemy.org/), a Python library which can interact with many different types of SQL databases
    - The default Rasa installation allows connections to SQLite and PostgreSQL databases.  

4. **FileEventBroker**
    - Use the `FileEventBroker` as an event broker. 
    - This implementation will log events to a file in json format. 
    - You can provide a path key in the `endpoints.yml` file if you wish to override the default file name: `rasa_event.log`  

5. **Custom Event Broker**  
    Done by extending the base class EventBroker.  

## Model Storage  

Trained models can be stored in different places.  
Rasa can be configured to load models in 3 different ways.  

1. **Load Model from local disk**
    - By default models will be loaded from local disk
    - Specify the path to model with the `--model` parameter
    - Ex: `rasa run --model models/20190506-100418.tar.gz`
    - Specify a directory instead of a file to load the latest model in that directory: `rasa run --model models/`
    - If `--model` argument is not specified, Rasa will look for models in the `models/` directory.  

2. **Load Model from HTTP server**
    - Configure the HTTP server to fetch models from another URL by adding it to `endpoints.yml` file
    ```
    {
        models:
          url: http://my-server.com/models/default
          wait_time_between_pulls: null  # fetch model only once
    }
    ```  

3. **Fetch from cloud storage**
    - Configure Rasa server to fetch model from a remote storage
    - Ex: rasa run --model 20190506-100418.tar.gz --remote-storage aws
    - Supported remote storage: 
        - `Amazon S3` using `boto3`
        - `Google Cloud Storage` using `google-cloud-storage`
        - `Azure Storage` using `azure-storage-blob`
        - `Other Remote Storage` using ` rasa.nlu.persistor.Persistor` class  

**Secret Manager**  
    Rasa Pro Only  
    Use HashiCorp Vault Secrets Manager  

## Use Rasa only as an NLU component  

1. **Train NLU-only models**  
    Run `rasa train nlu`  
    This will look for NLU training data files in the `data/` directory and saves a trained model in the `models/` directory.  
    The name of the model will start with `nlu-`  

2. **Test NLU model on the command line**  
    Run `rasa shell nlu`  
    The Rase shell will start and can type message to test  
    Can also pass in a NLU-only model directly with command `rasa shell -m models/nlu-20190515-144445.tar.gz`  

3. **Run NLU Server**
    Run command `rasa run --enable-api -m models/nlu-20190515-144445.tar.gz`  
    Can then request predictions from the model using `/model/parse endpoint` with command `curl localhost:5005/model/parse -d '{"text":"hello"}'`  


# Rasa Use Cases  

[Customer Experience Solution](https://rasa.com/solutions/customer-service-automation/)

[Community Showcase](https://rasa.com/showcase/)

[Rasa Chatbot](https://viblo.asia/p/tong-quan-ve-rasa-chatbot-E1XVOxrp4Mz)