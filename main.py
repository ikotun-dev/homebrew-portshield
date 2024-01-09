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


# this function returns all processes
def return_all_processes():
    processes = []
    for proc in psutil.process_iter(["pid", "name"]):
        #  processes.append(proc)

        try:
            for conn in proc.connections():
                #   if conn.status == "LISTEN":
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


# function to find a proceess
def find_process():
    # print("copyright-ikotun-dev23. ")
    port = input("Enter the port number: ")
    # to break out of the app
    if port == "c":
        quit()
    try:
        port = int(port)
    except ValueError:
        print("Not a valid port number ")
        main()

    processes = get_processes_by_port(port)
    return processes, port


def main():
    choice = input("View all processes or Kill process (v/k) : ")
    if choice.lower() == "v":
        print("Displaying all processes.....")

        processes = return_all_processes()
        print(processes)

    elif choice.lower() == "k":
        processes, port = find_process()
        #  print(type(processes), type(port))

        if len(processes) > 0:
            print(f"Processes using port {port}:")
            for proc in processes:
                print(f"PID: {proc.pid}, Name: {proc.name()}")
        else:
            print(f"No processes found using port {port}")
            main()  # calling the function again if there is no ports found in the previous

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
