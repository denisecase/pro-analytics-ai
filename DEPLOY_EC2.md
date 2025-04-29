## DEPLOY - EC2 (Easy, Expensive)

Not recommended for large use due to expense — but works well to deploy the custom assistant.

## All Commands assume Linux OS

If Windows, use **WSL**. 

On all machines, use VS Code Terminal (bash or zsh) in the `pro-analytics-ai` root project folder.



## 1. Create .ssh Directory for SSH Key

```shell
mkdir -p ~/.ssh
```

### 2. Create EC2 Instance

- Go to <https://console.aws.amazon.com/ec2/>
- Click **Launch Instance**
- Name: `pro-analytics-ai`
- Amazon Machine Image (AMI): Ubuntu 24.04 LTS
- Instance Type: **t2.small or larger**
- Create a key pair (.pem file), named `pro-analytics-ai-key`
- Under **Security → Security Groups**, click **Edit Inbound Rules**
  - Add rule: **SSH** TCP 22 `0.0.0.0/0` (temporary for setup)
  - Add rule: **Custom TCP** 8000 `0.0.0.0/0` (for API access)
- Click **Launch Instance**

## 3. Move Key to `.ssh` and Set Permissions

```shell
mv ~/Downloads/pro-analytics-ai-key.pem ~/.ssh/
chmod 400 ~/.ssh/pro-analytics-ai-key.pem
```

### 4. Connect to EC2

Replace with your EC2 Public IP:

```shell
ssh -i ~/.ssh/pro-analytics-ai-key.pem ubuntu@34.222.116.69
```

### 5. Install System Dependencies

```shell
sudo apt update && sudo apt upgrade -y 
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.12-venv -y
```

### 6. Clone and Set Up Project

```shell
git clone https://github.com/denisecase/pro-analytics-ai.git  

cd pro-analytics-ai

rm -rf .venv
python3 -m venv .venv  

source .venv/bin/activate 

python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt --timeout 100

rm -rf ~/.cache/pip
sudo apt clean
```

## 7. Add `.env` File

Create a `.env` file in the project root. 
Replace `sk-or-xxxxxxxxxxxxxxxx` with your real OpenRouter API key.

```shell
cat <<EOF > .env
ENV=prod
QUANT_MODE=none
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx
OPENAI_MODEL=gpt-3.5-turbo
EMBEDDING_MODEL=all-MiniLM-L6-v2
VECTOR_DB=chroma
EOF
```


### 8. Update Files During Debugging (As Needed)

Example if you update `query_api.py` or `requirements.txt` - NOTE these must be run in a new terminal open to your local Linux/WSL project NOT the server terminal. 

```shell
scp -i ~/.ssh/pro-analytics-ai-key.pem backend/A_api_interface/query_api.py ubuntu@34.222.116.69:~/pro-analytics-ai/backend/A_api_interface/query_api.py

scp -i ~/.ssh/pro-analytics-ai-key.pem requirements.txt ubuntu@34.222.116.69:~/pro-analytics-ai/requirements.txt

scp -i ~/.ssh/pro-analytics-ai-key.pem -r docs ubuntu@34.222.116.69:~/pro-analytics-ai/

scp -i ~/.ssh/pro-analytics-ai-key.pem backend/utils/config.py ubuntu@34.222.116.69:~/pro-analytics-ai/backend/utils/config.py


```

## 9. Run the API for Debugging (Optional)


```shell
uvicorn backend.A_api_interface.query_api:app --host 0.0.0.0 --port 8000
```

### 10. Run the API For Deployment

From your VS Code terminal (in Linux or WSL):

```shell
ssh -i ~/.ssh/pro-analytics-ai-key.pem ubuntu@34.222.116.69
cd ~/pro-analytics-ai
source .venv/bin/activate
nohup uvicorn backend.A_api_interface.query_api:app --host 0.0.0.0 --port 8000 &
```

### 11. While Server is Running (as needed)

See logs: 

```shell
ssh -i ~/.ssh/pro-analytics-ai-key.pem ubuntu@34.222.116.69
cd ~/pro-analytics-ai
tail -f nohup.out
```

Kill the process (get the PID number from the first command and use it in the second):

```shell
ssh -i ~/.ssh/pro-analytics-ai-key.pem ubuntu@34.222.116.69
ps aux | grep uvicorn
kill <pid>
```


## 12. Lock Down SSH Access Until Needed Again

- Go to <https://console.aws.amazon.com/ec2/>
- Under **Security / Security Groups**, click **Edit Inbound Rules**
- Edit the SSH rule (TCP 22):
  - Change Source from `0.0.0.0/0` (open to all)  
  - To `1.1.1.1/32` (fake IP — nobody can reach it)

This effectively disables SSH access until you change it back to your real IP later.

--- 

### Test the API

- Visit in browser: http://34.222.116.69:8000
- Or test with curl (do this from your WSL or Linux terminal):

```shell
curl -X POST http://34.222.116.69:8000/query -H "Content-Type: application/json" -d '{"question": "What is git?"}'
```

# Important Reminders

- EC2 Server will **keep running** (and incurring costs) until you `kill` or `stop` it manually.
- Keep your `.env` and secrets private — do NOT publish your OpenRouter API key.
