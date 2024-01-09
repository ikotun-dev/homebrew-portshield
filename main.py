import psutil
import os
import types


# function to get processes by port
def get_processes_by_port(port):
    processes = []
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            for conn in proc.connections():
                if conn.status == "LISTEN" and conn.laddr.port == port:
                    processes.append(proc)
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes


# function to kill process by its PID
def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.kill()
        return True
    except psutil.NoSuchProcess:
        return False


def find_process():
    # print("copyright-ikotun-dev23. ")

    port = int(input("Enter the port number: "))
    processes = get_processes_by_port(port)
    return processes, port


def main():
    processes, port = find_process()
    print(type(processes), type(port))

    if isinstance(port, int):
        if len(processes) > 0:
            print(f"Processes using port {port}:")
            for proc in processes:
                print(f"PID: {proc.pid}, Name: {proc.name()}")
        else:
            print(f"No processes found using port {port}")
            main()  # calling the function again if there is no ports found in the previous
    else:
        print(type(port))
        main()

    # Ask if the user wants to close the processes
    close_processes = input("Do you want to close the processes? (y/n) c - close: ")

    if close_processes.lower() == "y":
        # Kill the processes
        for proc in processes:
            killed = kill_process(proc.pid)
            if killed:
                print(f"Process with PID {proc.pid} has been killed.")
            else:
                print(f"Failed to kill process with PID {proc.pid}.")
    elif close_processes.lower() == "c":
        quit()
    else:
        main()


if __name__ == "__main__":
    main()
