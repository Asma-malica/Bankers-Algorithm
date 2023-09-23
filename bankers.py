class Banker:
    def __init__(self, num_processes, num_resources):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self._max = [[0] * num_resources for _ in range(num_processes)]
        self.allocation = [[0] * num_resources for _ in range(num_processes)]
        self.available = [0] * num_resources
        self.need = [[0] * num_resources for _ in range(num_processes)]

    def get_input(self):
        print("Enter the maximum resource allocation:")
        for i in range(self.num_processes):
            self._max[i] = list(map(int, input(f"Process {i+1}: ").split()))

        print("Enter the current resource allocation:")
        for i in range(self.num_processes):
            self.allocation[i] = list(map(int, input(f"Process {i+1}: ").split()))

        self.available = list(map(int, input("Enter the available resources: ").split()))

    def calculate_need(self):
        for i in range(self.num_processes):
            for j in range(self.num_resources):
                self.need[i][j] = self._max[i][j] - self.allocation[i][j]

    def safe_state(self):
        work = self.available.copy()
        finish = [False] * self.num_processes
        sequence = []
        while False in finish:
            found = False
            for i in range(self.num_processes):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.num_resources)):
                    work = [work[j] + self.allocation[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    sequence.append(f"p{i + 1}")
                    found = True
            if not found:
                break
        if all(finish):
            return sequence
        else:
            return None

    def request_resources(self, process, request):
        if any(request[i] > self.need[process][i] for i in range(self.num_resources)):
            print("Error: Request exceeds need")
            return False
        elif any(request[i] > self.available[i] for i in range(self.num_resources)):
            print("Error: Request exceeds available")
            return False
        else:
            for i in range(self.num_resources):
                self.available[i] -= request[i]
                self.allocation[process][i] += request[i]
                self.need[process][i] -= request[i]
            safe_sequence = self.safe_state()
            if safe_sequence is None:
                for i in range(self.num_resources):
                    self.available[i] += request[i]
                    self.allocation[process][i] -= request[i]
                    self.need[process][i] += request[i]
                print("Error: Request results in an unsafe state")
                return False
            else:
                print("Request granted")
                return True

    def table(self):
        print("Process\t\tMax\t\tAllocation\tNeed\t\tAvailable")
        for i in range(self.num_processes):
            print(
                f"P{i + 1}\t\t{self._max[i]}\t{self.allocation[i]}\t{self.need[i]}\t{self.available}"
            )

    def display_safe_sequence(self):
        sequence = self.safe_state()
        if sequence is None:
            print("No safe sequence found.")
        else:
            print("Safe Sequence:", " -> ".join(sequence))


if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resources: "))

    banker = Banker(num_processes, num_resources)
    banker.get_input()
    banker.calculate_need()

    banker.table()
    banker.display_safe_sequence()

