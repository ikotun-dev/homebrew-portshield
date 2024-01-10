#!/usr/bin/env python3
import psutil
from rich import print
from tabulate import tabulate


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
                processes.append(
                    {
                        "pid": proc.info["pid"],
                        "name": proc.info["name"],
                        "port": conn.laddr.port,
                    }
                )
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
    try:
        port = input("Enter the port number: ")
    except KeyboardInterrupt:
        print("Exiting...")
        exit()

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
    print("[bold green]View all processes or Kill process (v/k)  ")
    try:
        choice = input(">>> ")
    except KeyboardInterrupt:
        print("Exiting....")
        quit()

    if choice.lower() == "v":
        print("Displaying all processes.....")

        processes = return_all_processes()
        table_data = [[proc["pid"], proc["name"], proc["port"]] for proc in processes]
        # table_data.append([pid, name, port])

        headers = ["PID", "Name", "Port"]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        quit()

    elif choice.lower() == "k":
        processes, port = find_process()
        #  print(type(processes), type(port))

        if len(processes) > 0:
            print(f"[bold green]Process using port {port} :")
            for proc in processes:
                print(f"PID: {proc.pid}, Name: {proc.name()}")
        else:
            print(f"[bold red]No processes found using port {port}")
            main()  # calling the function again if there is no ports found in the previous

        # Ask if the user wants to close the processes
        print("[italic red]use e to exit ")
        try:
            close_processes = input("Do you want to close the processes? (y/n) : ")
        except KeyboardInterrupt:
            print("Exiting....")
            quit()
        if close_processes.lower() == "y":
            # Kill the processes
            for proc in processes:
                killed = kill_process(proc.pid)
                if killed:
                    print(f"[bold green]Process with PID {proc.pid} has been killed.")
                else:
                    print(f"[bold red]Failed to kill process with PID {proc.pid}.")
        elif close_processes.lower() == "e":
            print("Bye..")
            quit()
        else:
            main()
    else:
        print("[bold red]Not a valid command")
        main()


if __name__ == "__main__":
    main()
