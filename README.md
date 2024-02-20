## Running the Application with bash script
### How script works
This Bash script sends a POST request to an AWS API endpoint with a provided URL as JSON data, then uses jq to format the response and save it to a file named "raport.json".
### Prerequisites
To run this app you need to install jq.
- Linux
  run this in terminal to install jq:
  ```
  sudo apt-get update
  sudo apt-get install jq
  ```
- MacOS
  run this in terminal to install jq
  ```
  brew install jq
  ```
  if you do not have brew firstly you should install it 

### Installation
This command will download script to run program:
```
curl -O https://raw.githubusercontent.com/PawelHarasiuk/YouTube-Comment-Analyzer/main/create_raport.sh
```
### Running script 
To run this scirpt you have to provide the correct youtube link to wideo as an argument
```
bash create_raport.sh https://www.youtube.com/watch?v=S33SNjGyVN0
```
