# Quality Assuarance - Perfomance Testing

- [Install & Setup on Mac](#install--setup-on-mac)
    - [Install Java JDK](#install-java-jdk)
    - [Install Jmeter](#install-jmeter)
    
Includes testing for responsiveness, speed, stability, and scalability, focusing on:
- **Load testing** (simulating anticipated user/transaction traffic)
- **Stress testing** (identifying the system’s breaking point)
- **Scalability testing** (assessing performance under increasing load)

## Install & Setup on Mac 
### Install Java JDK:
Find an installer for your platform [here](https://www.oracle.com/java/technologies/downloads/#jdk25-mac).

1. **Check java-version**
```bash
java -version
```

2. **Get JDK path for setting the JAVA_HOME environment variable**
```bash
/usr/libexec/java_home
```
It will be something like
```zsh
/Library/Java/JavaVirtualMachines/jdk-25.jdk/Contents/Home
```

3. **Set the env variable**
```bash
vim ~/.bash_profile

##insert the env variable
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-25.jdk/Contents/Home
```

4. **Apply changes & check the path**
- expect the path added in step 3 above.
```zsh
source ~/.bash_profile

echo $JAVA_HOME
```

### Install Jmeter
```zsh
brew install jmeter
```

1. **Verify installation**
```zsh
jmeter --version
```
![alt text](jmeter_verify.png)

2. **launch jmeter**
```zsh
jmeter
```
![alt text](jmeter_launch.png)

# Load Testing
Load testing is a type of performance testing that measures how an application performs under heavy user activity and various conditions.

## Test run #1
**Scene**
- We will send 100 requests to STACAPI & record the response time. 
```zsh
Total requests = Num of Threads(users) x Loop Count
```
**Setting the test up**

Add a `Thread group` (Virtual users with ceryain behaviour)
- User/Thread count: `25`
- Ramp-up period : `100 secs` - Total time(in seconds) it takes to add all test users
    - each user will start 4 seconds after the previous user begins
- Loop Count - the number of times each user will make a request(Repeat)

For detailed setup steps, read more [here](https://medium.com/@simaalkan/jmeter-performance-testing-with-harry-potter-api-504365c5e60a)

**Run a Load test - CLI**

For heavy tests, it is recomended to use the non-GUI mode.
```zsh
jmeter -n -t test_plan.jmx -l results/results_$(date +%Y%m%d_%H%M%S).jtl -e -o results/dashboard_$(date +%Y%m%d_%H%M%S)
```
- `n` : non‑GUI mode
- `t` : path to your test plan
- `l` : path to save raw results (JTL format)
- `e` : generate HTML dashboard after test
- `o` : output directory for dashboard (must be empty or non‑existent)

### 



ref
- https://www.cobeisfresh.com/blog/how-to-perform-load-testing-using-jmeter
- https://medium.com/@simaalkan/jmeter-performance-testing-with-harry-potter-api-504365c5e60a