import logging
import time
import psutil
import os

from colorama import init, Fore, Style
init(autoreset=True)

def cpu_percent():
    cpu_statistics = psutil.cpu_percent(interval=1)
    return cpu_statistics

def cpu_alerts(cpu_statistics):
    if cpu_statistics > 90:
        logging.error("CPU USAGE ALERT: RED")
    elif 60 <= cpu_statistics < 90:
        logging.warning("CPU USAGE ALERT: ORANGE")
    else:
        logging.info("CPU USAGE NORMAL")


def memory_usage():
    memory_statistic = psutil.virtual_memory()
    return memory_statistic

def memory_alerts(memory_statistic):
    if memory_statistic.percent >= 90:
        logging.error("Memory usage alert: Red")
    elif 60 <= memory_statistic.percent < 90:
        logging.warning("Memory usage alert: Orange")
    else:
        logging.info("Memory Usage Normal")

def disk_usage():
    disk_statistic = psutil.disk_usage('/')
    return disk_statistic

def disk_alerts(disk_statistic):
    if disk_statistic.percent >= 90:
        logging.error("Disk usage alert: Red")
        print(Fore.RED + "Disk usage alert: Red" + Style.RESET_ALL)
    elif 60 <= disk_statistic.percent < 90:
        logging.warning("Disk usage alert: Yellow")
        print(Fore.YELLOW + "Disk usage alert: Yellow" + Style.RESET_ALL)
    else:
        logging.info("Disk usage normal")
        print(Fore.WHITE + "Disk usage normal" + Style.RESET_ALL)



def network_usage():
    network_statistics = psutil.net_io_counters()
    return network_statistics

def network_alerts(network_statistics):
    if network_statistics.errin > 0 or network_statistics.errout > 0:
        logging.error("Network USAGE ALERT: PACKET ERRORS DETECTED")
        print(Fore.RED + "Network USAGE ALERT: PACKET ERRORS DETECTED" + Style.RESET_ALL)
    elif network_statistics.dropin > 0 or network_statistics.dropout > 0:
        logging.warning("Network USAGE ALERT: DROPPED PACKAGES DETECTED")
        print(Fore.YELLOW + "Network USAGE ALERT: DROPPED PACKAGES DETECTED" + Style.RESET_ALL)
    else:
        logging.info("Network USAGE NORMAL")
        print(Fore.WHITE + "Network USAGE NORMAL" + Style.RESET_ALL)

#def main():
#    cpu_statistics = cpu_percent()
#    print(f"CPU USAGE:  {cpu_statistics}%")
#    memory_statistics = memory_usage()
#    print(f"MEMORY USAGE:  {memory_statistics.percent}%")
#    disk_statistics = disk_usage()
#    print(f"DISK USAGE:  {disk_statistics.percent}%")
#    network_statistics = network_usage()
#    print(f"BYTES SENT FROM DEVICE:  {network_statistics.bytes_sent}")
#    print(f"BYTES RECEIVED ON DEVICE:  {network_statistics.bytes_recv}")
#    print(f"PACKETS SENT FROM DEVICE:  {network_statistics.packets_sent}")
#    print(f"PACKETS RECEIVED ON DEVICE:  {network_statistics.packets_recv}")
#    print(f"NUMBER OF INCOMING PACKETS WITH ERRORS:  {network_statistics.errin}")
#    print(f"NUMBER OF OUTGOING PACKETS WITH ERRORS:  {network_statistics.errout}")
#    print(f"INCOMING PACKAGES DROPPED:  {network_statistics.dropin}")
#    print(f"OUTGOING PACKAGES DROPPED:  {network_statistics.dropout}")

#def main():
#    try:
#       while True:
#            os.system("clear" if os.name == "nt" else "clear")

#            cpu_statistics = cpu_percent()
#            print(f"CPU USAGE:  {cpu_statistics}%")
#            cpu_alerts(cpu_statistics)

#            memory_statistics = memory_usage()
#            print(f"Memory USAGE:  {memory_statistics.percent}%")
#            memory_alerts(memory_statistics)

#            disk_statistic = disk_usage()
#            print(f"Disk USAGE:  {disk_statistic.percent}%")
#            disk_alerts(disk_statistic)

#            network_statistics = network_usage()
#            print(f"BYTES SENT FROM DEVICE:  {network_statistics.bytes_sent}")
#            print(f"BYTES RECEIVED ON DEVICE:  {network_statistics.bytes_recv}")
#            print(f"PACKETS SENT FROM DEVICE:  {network_statistics.packets_sent}")
#            print(f"PACKETS RECEIVED ON DEVICE:  {network_statistics.packets_recv}")
#            print(f"NUMBER OF INCOMING PACKETS WITH ERRORS:  {network_statistics.errin}")
#            print(f"NUMBER OF OUTGOING PACKETS WITH ERRORS:  {network_statistics.errout}")
#            print(f"INCOMING PACKAGES DROPPED:  {network_statistics.dropin}")
#            print(f"OUTGOING PACKAGES DROPPED:  {network_statistics.dropout}")
#            network_alerts(network_statistics)

#            time.sleep(1)


def main():
    print("================SECUROX MACOS MONITER/LOGGER================")
    while True:
        print("1. Monitor CPU Only")
        print("2. Monitor Memory Usage")
        print("3. Monitor Disk Usage")
        print("4. Monitor Network Usage")
        print("5. Monitor ALL Components")
        print("THANK YOU FOR USING SECUROX --> CTRL + C To Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("Thank you for using Securox! - refer to /logs in /Securox for system issues")
        else:
            print("Error - Please try again")

def cpu_data():
    try:
        while True:
            cpu_statistics = cpu_percent()
            print(f"CPU USAGE:  {cpu_statistics}%")
            cpu_alerts(cpu_statistics)
            time.sleep(1)
            print("Press Ctrl + C to exit to Main Menu")

    except KeyboardInterrupt:
        print("Saved Log Report --> Returning to main menu")

def memory_data():
    try:
        while True:
            memory_statistics = memory_usage()
            print(f"Memory Usage:  {memory_statistics.percent}%")
            memory_alerts(memory_statistics)
            time.sleep(1)
            print("Press Ctrl + C to exit to main menu")

    except KeyboardInterrupt:
        print("Saved Log Report --> Returning to main menu")

def disk_data():
    try:
        while True:
            disk_statistic = disk_usage()
            print(f"Disk Usage:  {disk_statistic.percent}%")
            disk_alerts(disk_statistic)
            time.sleep(1)
            print("Press Ctrl + C to exit to main menu")

    except KeyboardInterrupt:
        print("Saved Log Report --> Returning to main menu")

def network_data():
    try:
        while True:
            network_statistic = network_usage()
            print(f"BYTES SENT FROM DEVICE:  {network_statistic.bytes_sent}")
            print(f"BYTES RECEIVED ON DEVICE:  {network_statistic.bytes_recv}")
            print(f"PACKETS SENT FROM DEVICE:  {network_statistic.packets_sent}")
            print(f"PACKETS RECEIVED ON DEVICE:  {network_statistic.packets_recv}")
            print(f"NUMBER OF INCOMING PACKETS WITH ERRORS:  {network_statistic.errin}")
            print(f"NUMBER OF OUTGOING PACKETS WITH ERRORS:  {network_statistic.errout}")
            print(f"INCOMING PACKAGES DROPPED:  {network_statistic.dropin}")
            print(f"OUTGOING PACKAGES DROPPED:  {network_statistic.dropout}")
            network_alerts(network_statistic)
            time.sleep(1)
            print("Press Ctrl + C to exit to main menu")

    except KeyboardInterrupt:
        print("Saved Log Report --> Returning to main menu")

def all_data():
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
                print(f"NUMBER OF INCOMING PACKETS WITH ERRORS:  {network_statistics.errin}")
                print(f"NUMBER OF OUTGOING PACKETS WITH ERRORS:  {network_statistics.errout}")
                print(f"INCOMING PACKAGES DROPPED:  {network_statistics.dropin}")
                print(f"OUTGOING PACKAGES DROPPED:  {network_statistics.dropout}")
                network_alerts(network_statistics)
                time.sleep(1)


        except KeyboardInterrupt:
            print("Saved Log Report --> Returning to main menu")


if __name__ == "__main__":
    main()

