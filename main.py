import psutil
import os

#function to get processes by port
def get_processes_by_port(port):
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try :
            for conn in proc.connections():
                            if conn.status == 'LISTEN' and conn.laddr.port == port:
                                processes.append(proc)
                                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
    return processes
#function to kill process by its PID
def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.kill()
        return True
    except psutil.NoSuchProcess:
        return False

def main():
    # Get the user input
    print("copyright-ikotun-dev23. ")

    port = int(input("Enter the port number: "))

    # Get the list of processes using the specified port
    processes = get_processes_by_port(port)

    # Display the processes
    if len(processes) > 0:
        print(f"Processes using port {port}:")
        for proc in processes:
            print(f"PID: {proc.pid}, Name: {proc.name()}")
    else:
        print(f"No processes found using port {port}")

    # Ask if the user wants to close the processes
    close_processes = input("Do you want to close the processes? (y/n): ")

    if close_processes.lower() == "y":
        # Kill the processes
        for proc in processes:
            killed = kill_process(proc.pid)
            if killed:
                print(f"Process with PID {proc.pid} has been killed.")
            else:
                print(f"Failed to kill process with PID {proc.pid}.")

if __name__ == "__main__":
    main()
