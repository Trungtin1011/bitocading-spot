# References  
[Ansible overview](https://www.middlewareinventory.com/blog/ansible-playbook-example/#What_is_Ansible_Playbook)  
[Copy files and directories with Ansible](https://www.middlewareinventory.com/blog/ansible-copy-examples/)  
[Create EC2 instance with Ansible](https://www.middlewareinventory.com/blog/ansible-aws-ec2/)  
[Kafka-cluster on EC2](https://github.com/giladju/setup-kafka-cluster-ec2/tree/master/tasks)  
[Kafka without ZooKeeper](https://hevodata.com/learn/kafka-without-zookeeper)  
[KRaft 1](https://developer.confluent.io/learn/kraft/)  
[KRaft 2](https://www.masterspringboot.com/apache-kafka/how-to-run-kafka-without-zookeeper/)  

[Ansible with item in range](https://stackoverflow.com/questions/48653092/ansible-with-items-in-range)

# Terminologies

```
{
  ---
    - name: Playbook
      hosts: webservers
      become: yes
      become_user: root
      tasks:
        - name: ensure apache is at the latest version
          yum:
            name: httpd
            state: latest
        - name: ensure apache is running
          service:
            name: httpd
            state: started
}
```

**name**  
Name of the playbook

**hosts**  
A set of hosts usually grouped together as a host group and defined in inventory file

**become**  
To tell ansible this play has to be executed with elevated privileges

**become_user**  
The user name that we want to switch to like compare it with sudo su - user

**tasks**  
Set of tasks to execute, All tasks would be defined below this and we have two tasks with two modules, the first module is *yum* and the second module is *service*

**A play**  
An ordered set of tasks which should be run against hosts selected from your inventory.

**A playbook** 
- A text file that contains a list of one or more plays to run in order.
- Can consider a playbook as a shell script. 

**Sample command**  
`ansible-playbook playbook.yml -i ansible_hosts`

**Dry Run the playbook without making Actual Changes**  
`ansible-playbook -C playbook.yml -i ansible_hosts`

**Perform a Syntax Check on the Playbook**  
`ansible-playbook  "playbook.yaml" -i hosts.yaml --extra-vars "" --syntax-check`

**Use Variables in Ansible Playbook**  
*vars* to define inline variables within the playbook  
```
{
    ...
    become_user: root
    vars:
       key_file:  /etc/apache2/ssl/mywebsite.key
       cert_file: /etc/apache2/ssl/mywebsite.cert
       server_name: www.mywebsite.com
    tasks:
    ...
}
```

*vars_files* to import files with variables  
```
{
   ...
    become_user: root
    vars_files:
        - apacheconf.yml
    tasks:
    ... 
    "{{apacheconf_content}}"
}
```

**Install on CentOS**  
```
{
  sudo yum update -y
  sudo yum install -y epel-release
  sudo yum install -y ansible
}
```

**Check Ansible version** `ansible --version`

**Inventory file parameters**
```
{
  ansible_host: server.com
  ansible_connection=ssh / winrm / localhost
  ansible_port: 22 / 5986
  ansible_user: root / administrator
  ansible_ssh_pass / ansible_password: passwd
  ansible_ssh_private_key_file
}
```  
```
{
  server01 ansible_host=<ip> ansible_port=22 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/key.pem
  server02 ansible_host=<ip> ansible_port=22 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/key.pem
  server03 ansible_host=<ip> ansible_port=22 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/key.pem
}
```  

**Do something with java version condition**
```
{
  - name: Fetch Java version
    shell: java -version 2>&1 | grep version | awk '{print $3}' | sed 's/"//g'
    register: java_version

  - name:
      <do something> 
    when: java_version.stdout | version_compare('11.0', '>=')
}
```  

**Pass Variables on CLI**  

`ansible-playbook release.yml --extra-vars "hosts=vipers user=starbuck"`  
  
`--extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'`  
  
`--extra-vars "@some_file.json"`  
  
```
{
  # file: user.yml  (playbook)
  ---
  - hosts: '{{ target }}'
    user: ...

  #Running the playbook
  ansible-playbook user.yml --extra-vars "target=imac-2.local"
}
```
