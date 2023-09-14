import os
import pika 
import sys
import logging
import random



logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='topic.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


brok_list=["101","102","103"]
rep_fac=3
def replicate(top,key,msg):
    for i in range(len(brok_list)):
        if(brok_list[i]!=key):
            rp = "C:/Users/Admin/Desktop/OSR_KAFKA/BROKER"
            rt=brok_list[i]+"/"+top
            rpath=os.path.join(rp,rt)
            rfn=top+"-isr"+".txt"
            if(os.path.exists(rpath)):
                with open(os.path.join(rpath, rfn), 'a') as fp:
                    fp.write(msg)
                    fp.write("\n")
                    fp.close()
            else:
                os.makedirs(rpath)
                with open(os.path.join(rpath, rfn), 'w') as fp:
                    fp.write(msg)
                    fp.write("\n")
    data = 'Topic {} created successfully , message  replicated successfully to all the partitions\n'.format(top)
    logger.info(data)
              
                    

    
#def logs():
def check(top,msg,key):
    data = 'Producer produced a message on the topic {} \n'.format(top)
    logger.info(data)
    brok_list=["101","102","103"]
    if(key in brok_list):
        p = "C:/Users/Admin/Desktop/OSR_KAFKA/BROKER"
        t=key+"/"+top
        path=os.path.join(p,t)
        fn=top+"-leader"+".txt"
        
        if(os.path.exists(path)):
            with open(os.path.join(path, fn), 'a') as fp:
                fp.write(msg)
                fp.write("\n")
                fp.close()
                data = 'Record successfully written to the topic {} message inserted  to the leader partition  \n'.format(top)
                logger.info(data)
                replicate(top,key,msg)
                
 


        else:
            os.makedirs(path)
            with open(os.path.join(path, fn), 'w') as fp:
                fp.write(msg)
                fp.write("\n")
                fp.close()
                data = 'Topic {} created successfully , leader is elected and mesaage is inserted\n'.format(top)
                logger.info(data)
                  
                replicate(top,key,msg)
                
        
    else:
        print("key not found")             
            

def read_brok(top):
    p = "C:/Users/Admin/Desktop/OSR_KAFKA/BROKER"
    for i in range(len(brok_list)):
        p = "C:/Users/Admin/Desktop/OSR_KAFKA/BROKER"
        p=p+"/"+brok_list[i]
        path=os.path.join(p,top)
        fn=top+"-leader.txt"
        pt=os.path.join(path, fn)
        if(os.path.exists(pt)):
            file1 = open(pt, "r+")
            print(file1.read())
            data = 'Consumer consumes from topic{}\n'.format(top)
            logger.info(data)
            break
        else:
            p = "C:/Users/Admin/Desktop/OSR_KAFKA/BROKER"
            p=p+"/"+brok_list[i]
            path=os.path.join(p,top)
            fn=top+"-isr.txt"
            pt=os.path.join(path, fn)
            if(os.path.exists(pt)):
                file1 = open(pt, "r+")
                print(file1.read())
                data = 'ERROR:Leader node failed,Consumer consumes from topic{} from the replicas\n'.format(top)
                logger.info(data)
                break



        


    
#read_brok(top)
#read_brok(top)

