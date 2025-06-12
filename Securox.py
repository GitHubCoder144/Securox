import psutil

def cpu_percent():
    cpu_statistics = psutil.cpu_percent(interval=1)
    return cpu_statistics

def Network_usage():
    network_statistics = psutil.net_io_counters()
    return network_statistics


def main():
    cpu_statistics = cpu_precent()
    print(f"CPU USAGE:  {cpu_statistics}%")
    network_statistics = Network_usage()
    print(f"BYTES SENT FROM DEVICE:  {network_statistics.bytes_sent}")
    print(f"BYTES RECIVED ON DEVICE:  {network_statistics.bytes_recv}")
    print(f"PACKETS SENT FROM DEVICE:  {network_statistics.packets_sent}")
    print(f"PACKETS RECIVED ON DEVICE:  {network_statistics.packets_recv}")
    print(f"NUMBER OF INCOMING PACKETS WITH ERRORS:  {network_statistics.errin}")
    print(f"NUMBER OF OUTGOING PACKETS WITH ERRORS:  {network_statistics.errout}")
    print(f"INCOMING PACKAGES DROPPED:  {network_statistics.dropin}")
    print(f"OUTGOING PACKAGES DROPPED:  {network_statistics.dropout}")


if __name__ == "__main__":
    main()

