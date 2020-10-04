name: glados-checkin

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
  schedule:
    - cron:  0 16 * * * 

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Install Python
      run: |
        sudo apt update && \
        sudo apt install python3
      
    - name: requirements
      run: |
        pip3 install -r requirements.txt
        
    - name: Checkin
      run: |
        python3 checkin.py 
      env: 
        SERVE: ${{ secrets.SERVE }}
        SCKEY: ${{ secrets.SCKEY }}
        COOKIE: ${{ secrets.COOKIE }}
