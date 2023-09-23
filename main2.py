# all the safe sequence code 

class Banker:
   

    def safe_state(self):
        work = self.available.copy()
        finish = [False] * self.num_processes
        sequences = []  # Collect all safe sequences
        while False in finish:
            found = False
            for i in range(self.num_processes):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.num_resources)):
                    work = [work[j] + self.allocation[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    found = True
            if not found:
                break
            if all(finish):
                sequence = [f"p{i + 1}" for i, f in enumerate(finish) if f]
                sequences.append(sequence)
        return sequences

    # ...

   
        
    def display_safe_sequences(self):
     sequences = self.safe_state()
     if not sequences:
        print("No safe sequences found.")
     else:
        print("Safe Sequences:")
        for sequence in sequences:
            print(" -> ".join(sequence))
    
    if __name__ == "__main__":
     num_processes = int(input("Enter the number of processes: "))
     num_resources = int(input("Enter the number of resources: "))

     banker = Banker(num_processes, num_resources)
     banker.get_input()
     banker.calculate_need()

     banker.table()
     banker.display_safe_sequences()  # Modified method name

