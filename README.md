# Securox

Securox is a terminal-based, lightweight system-monitering and logging tool for macOS and Linux. 
  1. Brings Real Time Data for CPU, Network, Memory, and Disk.
  2. catagorizes alerts by severity (Red (>90%), Orange (60%-90%), and Green (<60%)) for reference.
  3. Saves Detailed Monitering Alerts where users can see past Securox Runs.

Securox is built fully on Python refering to psutil for system data and provides a structured log 
for easy refrence. 

## Installation

```bash
pip install psutil
pip install colorama
```

```bash
git clone https://github.com/GitHubCoder144/Securox.git
cd Securox
```

## Usage

```python
# for macOS
python Securox_macOS.py
# or if on Python 3
python3 Securox_macOS.py
```

```python
# for linux
python Securox_Linux.py
# or if in python 3
python3 Securox.Linux.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)
