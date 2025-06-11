import psutil

def cpu_precent():
    cpu_statistics = psutil.cpu_percent(interval=1)
    return cpu_statistics

def main():
    cpu_statistics = cpu_precent()
    print(f"CPU USAGE:  {cpu_statistics}%")

if __name__ == "__main__":
    main()

