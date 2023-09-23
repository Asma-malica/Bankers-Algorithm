
document.getElementById("run-btn").addEventListener("click", function() {
  // Get user input values
  const availableInput = document.getElementById("available-input").value;
  const maxInput = document.getElementById("max-input").value;
  const allocatedInput = document.getElementById("allocated-input").value;

  // Parse input values
  const available = availableInput.split(" ").map(Number);
  const max = maxInput.split("\n").map(row => row.split(" ").map(Number));
  const allocated = allocatedInput.split("\n").map(row => row.split(" ").map(Number));

  // Call Banker's algorithm function
  const { result, safeSequence, need } = bankersAlgorithm(available, max, allocated);

  // Update result text
  const resultText = document.getElementById("result");
  if (result) {
    resultText.textContent = "Safe state - All processes can be completed.";
    displayNeedMatrix(need);
    displaySafeSequence(safeSequence);
  } else {
    resultText.textContent = "Unsafe state - Deadlock may occur.";
    clearOutput();
  }
});

function displayNeedMatrix(need) {
  const needMatrixContainer = document.getElementById("need-matrix-container");
  needMatrixContainer.innerHTML = "";

  const needMatrixTitle = document.createElement("h3");
  needMatrixTitle.textContent = "Need Matrix:";
  needMatrixContainer.appendChild(needMatrixTitle);

  const needMatrixTable = document.createElement("table");
  need.forEach(row => {
    const tableRow = document.createElement("tr");
    row.forEach(val => {
      const tableData = document.createElement("td");
      tableData.textContent = val;
      tableRow.appendChild(tableData);
    });
    needMatrixTable.appendChild(tableRow);
  });
  needMatrixContainer.appendChild(needMatrixTable);
}

function displaySafeSequence(safeSequence) {
  const safeSequenceContainer = document.getElementById("safe-sequence-container");
  safeSequenceContainer.innerHTML = "";

  const safeSequenceTitle = document.createElement("h3");
  safeSequenceTitle.textContent = "Safe Sequence:";
  safeSequenceContainer.appendChild(safeSequenceTitle);

  const safeSequenceText = document.createElement("p");
  safeSequenceText.textContent = safeSequence.join(" -> ");
  safeSequenceContainer.appendChild(safeSequenceText);
}

function clearOutput() {
  const needMatrixContainer = document.getElementById("need-matrix-container");
  needMatrixContainer.innerHTML = "";

  const safeSequenceContainer = document.getElementById("safe-sequence-container");
  safeSequenceContainer.innerHTML = "";
}

function bankersAlgorithm(available, max, allocated) {
  const numProcesses = max.length;
  const numResources = available.length;

  // Initialize data structures
  const work = available.slice();
  const finish = Array(numProcesses).fill(false);
  const need = max.map((row, i) => row.map((val, j) => val - allocated[i][j]));

  // Store the safe sequence
  const safeSequence = [];

  // Check if all processes can be completed
  while (true) {
    let found = false;

    for (let i = 0; i < numProcesses; i++) {
      if (!finish[i] && need[i].every((val, j) => val <= work[j])) {
        // Allocate resources to process i
        for (let j = 0; j < numResources; j++) {
          work[j] += allocated[i][j];
        }

        finish[i] = true;
        found = true;

        // Add the process to the safe sequence
        safeSequence.push(i);
      }
    }

    if (!found) {
      break;
    }
  }

  const result = finish.every(Boolean);

  return { result, safeSequence, need };
}
