<a name="readme-top"></a>

# Yet-Another-Kafka--YAK-2.0
```YAK-2.0``` can also be termed as ```Yet Another Kafka 2.0```. 

This project aims to create ```Kafka like software or platform```, for producers and consumers.


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
- We have successfully implemented producers, consumers, 3 brokers, topic log, etc... 
- This project can also handle multiple or any random number of producers and consumers.
 
  <p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>

## Prerequisites and Techstack
- Python
- RabbitMQ
- Kafka concept

  <p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>

## Steps for execution
1. Clone the ```Yet-Another-Kafka--YAK-2.0``` repository
   ```sh
    git clone https://github.com/ankitacoder3/Yet-Another-Kafka--YAK-2.0.git
3. Start RabbitMQ in terminal/command prompt. By typing
    ```sh
   rabbitmq-server.bat 
5. Open a new terminal and start consumer. By typing
   ```sh
   python consumer.py test n
   ```
    Or
   ```sh
   python consumer.py test --from-beginning
   ```
7. Open another new terminal and start producer. By typing
   ```sh
   python producer1.py test 101
   ```
9. Check the terminal where consumer is running, to check for messages received. 
10. Now, open the 'broker' folder, which is under 'YAK' folder. 
11. In that folder you can check the 'topic-log' file for the log activity. 
12. In the same folder, check the '101' folder (where 101 is the key of leader broker).
13. Open the 'test-lead' file (where test is the topic). You can see that the message has been appended in file.
14. Hence, the messages have been successfully sent, received and stored. A file also maintains all the activities done as log. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>

## Usage
- To run multiple producers and consumers, open a new terminal for each new consumer and producer. 
- To run a consumer type the following:
  -  To view the recent message sent
  ```sh
  python consumer.py <topic_name> n
  ```
  - To view all messages sent from beginning or starting of topic
  ```sh
  python consumer.py <topic_name> --from-beginning
  ```

- To run a producer type the following
  ```sh
  python producers1.py <topic_name> <key_of_leader_broker>
  ```
    where, key_of_leader_broker = 101 or 102 or 103

  <p align="right">(<a href="#readme-top">back to top</a>)</p>
  </br>


Thank You.
 
   
