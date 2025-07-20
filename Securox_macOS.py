#!/usr/bin/env python3

# Securox - macOS monitoring tool

# -------------------------------

import logging  # for alerts functions
import os  # for directory handling and creation
import time  # for pauses between checks
from datetime import datetime  # to format timestamp with current time

import psutil  # system monitoring APIs - stats for CPU, memory, disk, network
from colorama import Fore, Style, init  # to color alerts for categorization

# -------------------------------

init(autoreset=True)
# Resets color after every print

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# defined Time with current date and in format of Year/Month/Day
print(timestamp)

# alerts dictionary for color catagorization for alert methods
# for - cpu_alerts , memory_alerts, disk_alerts, network_alerts
alerts = {"red": [], "yellow": [], "green": []}

# Prefered Structure for alerts methods:
# If usage is Above or > 90% --> Red Alert
# Else If usage is in between 60% to 90% --> Yellow Alert
# Else --> Green Alert


# cpu_precent - Function cpu_precent pulls CPU Stats every second
def cpu_percent():
    cpu_statistics = psutil.cpu_percent(interval=1)
    return cpu_statistics


# cpu_alerts - Function cpu_alerts takes cpu_statistics defined earlier
# and catagorizes the alerts by severity (the highest being red and lowest being green)
def cpu_alerts(cpu_statistics):

    # threshhold for severity level red
    if cpu_statistics > 90:
        # 2. Gather the current date with global date format
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 3. Apply Red From Alert Dictonary and attach Message with current time stamp
        alerts["red"].append(f"{now} - cpu usage exceeds 90%")
        # 4. Print the whole Message in Red and Reset For next Reading
        print(Fore.RED + "CPU usage alert: Red" + Style.RESET_ALL)
        # 5. Log the Error With the inputed message
        logging.error("CPU USAGE ALERT: RED")
    elif 60 <= cpu_statistics < 90:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["yellow"].append(f"{now} - CPU usage between 60% and 90%")
        logging.warning("CPU USAGE ALERT: YELLOW")
        print(Fore.YELLOW + "CPU usage alert: Yellow" + Style.RESET_ALL)
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["green"].append(f"{now} - CPU USAGE NORMAL")
        logging.info("CPU USAGE NORMAL")
        print(Fore.GREEN + "CPU USAGE NORMAL" + Style.RESET_ALL)


# memory_alert and memory_usage follows exact logic as cpu_precent and cpu_alerts
# just with different components


def memory_usage():
    memory_statistic = psutil.virtual_memory()
    return memory_statistic


def memory_alerts(memory_statistic):
    if memory_statistic.percent >= 90:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["red"].append(f"{now} - Memory usage alert: RED")
        logging.error("Memory usage alert: Red")
        print(Fore.RED + "Memory usage alert: Red" + Style.RESET_ALL)
    elif 60 <= memory_statistic.percent < 90:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["yellow"].append(f"{now} - Memory usage alert: YELLOW")
        logging.warning("Memory usage alert: Yellow")
        print(Fore.YELLOW + "Memory usage alert: Yellow" + Style.RESET_ALL)
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["green"].append(f"{now} - Memory USAGE NORMAL")
        logging.info("Memory Usage Normal")
        print(Fore.GREEN + "Memory usage normal" + Style.RESET_ALL)


# disk_usage and disk_alerts follows exact logic as cpu_precent and cpu_alerts
# just with different components


def disk_usage():
    disk_statistic = psutil.disk_usage("/")
    return disk_statistic


def disk_alerts(disk_statistic):
    if disk_statistic.percent >= 90:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["red"].append(f"{now} - Memory usage alert: RED")
        logging.error("Disk usage alert: Red")
        print(Fore.RED + "Disk usage alert: Red" + Style.RESET_ALL)
    elif 60 <= disk_statistic.percent < 90:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["yellow"].append(f"{now} - Memory usage alert: YELLOW")
        logging.warning("Disk usage alert: Yellow")
        print(Fore.YELLOW + "Disk usage alert: Yellow" + Style.RESET_ALL)
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["green"].append(f"{now} - DISK USAGE NORMAL")
        logging.info("Disk usage normal")
        print(Fore.GREEN + "Disk usage normal" + Style.RESET_ALL)


# network_alert and network_usage follows exact logic as cpu_precent and cpu_alerts
# just with different components


def network_usage():
    network_statistics = psutil.net_io_counters()
    return network_statistics


def network_alerts(network_statistics):
    if network_statistics.errin > 0 or network_statistics.errout > 0:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["red"].append(f"{now} - Network usage alert: RED")
        logging.error("NETWORK USAGE ALERT: PACKET ERRORS DETECTED")
        print(
            Fore.RED + "NETWORK USAGE ALERT: PACKET ERRORS DETECTED" + Style.RESET_ALL
        )

    elif network_statistics.dropin > 0 or network_statistics.dropout > 0:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["yellow"].append(f"{now} - Network usage alert: YELLOW")
        logging.warning("Network USAGE ALERT: DROPPED PACKAGES DETECTED")
        print(
            Fore.YELLOW
            + "Network USAGE ALERT: DROPPED PACKAGES DETECTED"
            + Style.RESET_ALL
        )
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alerts["green"].append(f"{now} - Network usage normal")
        logging.info("Network USAGE NORMAL")
        print(Fore.GREEN + "Network USAGE NORMAL" + Style.RESET_ALL)


# initilization- Function initilization is meant to run ONCE in the life of Securox primary
# to set up Securox file system with the proper file path for proper logging


def initialization():
    components = ["cpu", "memory", "disk", "network"]
    severities = ["red", "yellow", "green"]

    for component in components:
        for severity in severities:
            path = f"Securox/logs/{component}/{severity}"
            os.makedirs(path, exist_ok=True)


# filealerts- function filealerts provides a way for the program to store saved memory during
# a security monitering session into the appropriate file path based on component and severity


def filealerts(component_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    # Took Imported OS and Added the First Part of Path: Both /Users/(Username) and /Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    # Second Part Of the Path /Securox and /Securox/logs
    base_path = os.path.join(desktop, "Securox", "logs")
    for severity, messages in alerts.items():
        if messages:
            # Filename Standered for all Securox Messages
            filename = f"{component_name}_{severity}_{timestamp}.txt"
            # file path Standered for Where Securox files should end up
            file_path = os.path.join(base_path, component_name, severity, filename)
            # ensures path exists if function initilization didnt work
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # writes messages by opening a file, writing alerts to that file, then wiped from memory
            with open(file_path, "w") as file:
                for message in messages:
                    file.write(message)
                    alerts["red"].clear()
                    alerts["yellow"].clear()
                    alerts["green"].clear()


def main():
    initialization()
    # VERSION 3: main UI WITH LIVE UPDATE --> what the person interacts with
    print("================SECUROX MACOS MONITER/LOGGER================")
    while True:
        print("1. Monitor CPU Only")
        print("2. Monitor Memory Usage")
        print("3. Monitor Disk Usage")
        print("4. Monitor Network Usage")
        print("5. Monitor ALL Components")
        print("6. Exit")
        print("THANK YOU FOR USING SECUROX")

        choice = input("Enter your choice (1-6): ")
        # Options and their outputs based on what number the person chooses

        if choice == "1":
            cpu_data()
        elif choice == "2":
            memory_data()
        elif choice == "3":
            disk_data()
        elif choice == "4":
            network_data()
        elif choice == "5":
            all_data()
        elif choice == "6":
            print(
                "Thank you for using Securox! - refer to /logs in /Securox for system issues"
            )
            break
        else:
            print("Error - Please try again")


def cpu_data():
    # cpu_data -- This function displays the cpu precent every one second
    # until ctrl + c is pressed
    try:
        while True:
            cpu_statistics = cpu_percent()
            print(f"CPU USAGE:  {cpu_statistics}%")
            cpu_alerts(cpu_statistics)
            time.sleep(1)
            print("Press Ctrl + C to exit to Main Menu", flush=True)

    except KeyboardInterrupt:
        filealerts("cpu")
        print("Saved Log Report --> Returning to main menu")


def memory_data():
    # memory_data -- This function displays the memory precent every one second
    # until ctrl + c is pressed
    try:
        while True:
            memory_statistics = memory_usage()
            print(f"Memory Usage:  {memory_statistics.percent}%")
            memory_alerts(memory_statistics)
            time.sleep(1)
            print("Press Ctrl + C to exit to main menu", flush=True)

    except KeyboardInterrupt:
        filealerts("memory")
        print("Saved Log Report --> Returning to main menu")


def disk_data():
    # disk_data -- This function displays the precent of disk used every one second
    # until ctrl + c is pressed
    try:
        while True:
            disk_statistic = disk_usage()
            print(f"Disk Usage:  {disk_statistic.percent}%")
            disk_alerts(disk_statistic)
            time.sleep(1)
            print("Press Ctrl + C to exit to main menu", flush=True)

    except KeyboardInterrupt:
        filealerts("disk")
        print("Saved Log Report --> Returning to main menu")


def network_data():
    # network_data -- This function unlike the other shows details on bytes and packets of a system
    # until ctrl + c is pressed
    try:
        while True:
            network_statistic = network_usage()
            print(f"BYTES SENT FROM DEVICE:  {network_statistic.bytes_sent}")
            print(f"BYTES RECEIVED ON DEVICE:  {network_statistic.bytes_recv}")
            print(f"PACKETS SENT FROM DEVICE:  {network_statistic.packets_sent}")
            print(f"PACKETS RECEIVED ON DEVICE:  {network_statistic.packets_recv}")
            print(f"NUMBER OF INCOMING PACKETS WITH ERRORS:  {network_statistic.errin}")
            print(
                f"NUMBER OF OUTGOING PACKETS WITH ERRORS:  {network_statistic.errout}"
            )
            print(f"INCOMING PACKAGES DROPPED:  {network_statistic.dropin}")
            print(f"OUTGOING PACKAGES DROPPED:  {network_statistic.dropout}")
            network_alerts(network_statistic)
            time.sleep(1)
            print("Press Ctrl + C to exit to main menu", flush=True)

    except KeyboardInterrupt:
        filealerts("network")
        print("Saved Log Report --> Returning to main menu")


def all_data():
    # all_data -- This function displays everything (cpu,memory,disk, network) every one second
    # until ctrl + c is pressed
    try:
        while True:
            cpu_statistics = cpu_percent()
            print(f"CPU USAGE:  {cpu_statistics}%")
            cpu_alerts(cpu_statistics)

            memory_statistics = memory_usage()
            print(f"Memory USAGE:  {memory_statistics.percent}%")
            memory_alerts(memory_statistics)

            disk_statistic = disk_usage()
            print(f"Disk USAGE:  {disk_statistic.percent}%")
            disk_alerts(disk_statistic)

            network_statistics = network_usage()
            print(f"BYTES SENT FROM DEVICE:  {network_statistics.bytes_sent}")
            print(f"BYTES RECEIVED ON DEVICE:  {network_statistics.bytes_recv}")
            print(f"PACKETS SENT FROM DEVICE:  {network_statistics.packets_sent}")
            print(f"PACKETS RECEIVED ON DEVICE:  {network_statistics.packets_recv}")
            print(
                f"NUMBER OF INCOMING PACKETS WITH ERRORS:  {network_statistics.errin}"
            )
            print(
                f"NUMBER OF OUTGOING PACKETS WITH ERRORS:  {network_statistics.errout}"
            )
            print(f"INCOMING PACKAGES DROPPED:  {network_statistics.dropin}")
            print(f"OUTGOING PACKAGES DROPPED:  {network_statistics.dropout}")
            network_alerts(network_statistics)
            time.sleep(1)
            print("Press Ctrl + C to exit to main menu", flush=True)

    except KeyboardInterrupt:
        filealerts("cpu")
        filealerts("memory")
        filealerts("disk")
        filealerts("network")
        print("Saved Log Report --> Returning to main menu")


# ONLY run the main function if Securox.py is being directly run on
if __name__ == "__main__":
    main()
