<a name="readme-top"></a>

# YAK-2.0
YAK 2.0 can also be termed as Yet another Kafka 2.0

<details>
  <summary color= blue >Table of Contents</summary>
<li>Introduction</li>
<li> Prerequisites and Techstack</li>
<li> Steps for execution</li>
<li> Usage</li>
</details>
</br>


## Introduction
- In this project we have used Python and RabbitMQ to mimic the functionalities of Kafka. 
- We have successfully implemented producers, consumers, 3brokers, topic log, etc... 
- This project can also handle multiple or any random number of producers and consumers.
 
  <p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>

## Prerequisites and Techstack

- Python
- RabbitMQ
- Prerequisites: Kafka concept

  <p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>

## Steps for execution
1. Download all files from this github repository and put them under a new folder (say, YAK2) . 
2. Start RabbitMQ in terminal/command prompt. (By typing 'rabbitmq-server.bat'). 
3. Open a new terminal and start consumer. (By typing 'python consumer.py test n' Or 'python consumer.py test --from-beginning'.) 
4. Open another new terminal and start producer. (By typing 'python producer1.py test 101’) 
5. Check the terminal where consumer is running, to check for messages received. 
6. Now, open the 'broker' folder, which is under 'YAK' folder. 
7. In that folder you can check the 'topic-log' file for the log activity. 
8. In the same folder, check the '101' folder (where 101 is the key of leader broker). Open the 'test-lead' file (where test is the topic). You can see that the message has been appended in file.
9. Hence, the messages have been successfully sent, received and stored. A file also maintains all the activities done as log. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>

## Usage
- To run multiple producers and consumers, open a new terminal for each new consumer and producer. 
- To run a consumer type the following, { "python consumer.py <topic_name> n", to view the recent message sent } or { "python consumer.py <topic_name> --from-beginning", to view all messages sent from beginning or starting of topic }. 
- To run a producer type the following, { "python producers1.py <topic_name> <key_of_leader_broker>", where key_of_leader_broker can be 101 or 102 or 103}. 

  <p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>


Thank You.
 
   
