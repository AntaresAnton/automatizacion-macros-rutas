// Función para alternar la visibilidad del contenido de una tarjeta
function toggleCard(header) {
  const content = header.nextElementSibling;
  content.style.display = content.style.display === "none" ? "block" : "none";
}

function updateProgress(btn) {
  const card = btn.closest(".card-body");
  const progressBar = card.querySelector(".progress-bar");
  const buttons = card.querySelectorAll(".btn-process");
  const completedButtons = Array.from(buttons).filter(button => button.classList.contains("btn-success"));

  const totalSteps = buttons.length;
  const completedSteps = completedButtons.length;
  const progress = (completedSteps / totalSteps) * 100;
  const roundedProgress = Math.round(progress);

  progressBar.style.width = `${roundedProgress}%`;
  progressBar.setAttribute("aria-valuenow", roundedProgress);
  progressBar.textContent = `${roundedProgress}%`;

  updateOverallProgress();
}



// Función para actualizar la barra de progreso general de todas las tareas
function updateOverallProgress() {
  const cards = document.querySelectorAll(".card");
  let totalProgress = 0;

  cards.forEach((card) => {
    const progressBar = card.querySelector(".progress-bar");
    totalProgress += parseInt(progressBar.getAttribute("aria-valuenow"));
  });

  const overallProgress = totalProgress / cards.length;
  const overallProgressBar = document.getElementById("overall-progress");
  overallProgressBar.style.width = `${overallProgress}%`;
  overallProgressBar.setAttribute("aria-valuenow", overallProgress);
  overallProgressBar.textContent = `${Math.round(overallProgress)}%`;
}

// Función para confirmar la realización de un proceso y actualizar su estado
function confirmProcess(btn, workflow) {
  if (confirm(`¿Confirma que se realizó la operación: ${workflow}?`)) {
    updateButtonState(btn, "Confirmado", "btn-primary", "btn-success");
    updateProgress(btn);
    showToast();
  }
}

// Función para ejecutar una macro y actualizar su estado
function executeMacro(btn, macroPath) {
  if (confirm(`¿Desea ejecutar la macro: ${macroPath || "Macro"}?`)) {
    updateButtonState(btn, "Macro Ejecutada", "btn-secondary", "btn-success");
    updateProgress(btn);
    showToast();
  }
}

// Función para publicar un informe y actualizar su estado
function publishReport(btn) {
  if (confirm("¿Desea publicar el informe?")) {
    updateButtonState(btn, "Informe Publicado", "btn-secondary", "btn-success");
    updateProgress(btn);
    showToast();
  }
}


// función para activar el botón de envío de correos
function sendEmail(btn) {
  if (confirm("¿Desea enviar el correo con el informe?")) {
    btn.textContent = "Enviando correo...";
    btn.disabled = true;

    setTimeout(() => {
      btn.classList.remove("btn-info");
      btn.classList.add("btn-success");
      btn.textContent = "Correo Enviado";
      updateProgress(btn);
      showToast("Correo enviado exitosamente");
    }, 3000);
  }
}


// Función auxiliar para actualizar el estado de los botones
function updateButtonState(btn, text, oldClass, newClass) {
  btn.classList.remove(oldClass);
  btn.classList.add(newClass);
  btn.textContent = text;
  btn.disabled = true;
  if (btn.nextElementSibling) {
    btn.nextElementSibling.disabled = false;
  }
}

// Función para mostrar una notificación toast
function showToast() {
  var toast = new bootstrap.Toast(document.getElementById("taskToast"));
  toast.show();
}

// Objeto que contiene las tareas para cada proceso
const processTasks = {
  "07": [
    {
      title: "Cierre CPCH - Generación Informes Venta Diaria CPCH",
      workflow: "WORKFLOW_02_RES_VENTA_DIARIA_MESCERRADO_PIS",
    },
    {
      title: "Cierre CPCH - Generación Informes Venta Diaria PR",
      workflow: "WORKFLOW_02_RES_VENTA_DIARIA_MESCERRADO_PIS",
    },
    // Add more tasks for process 07
  ],
  // Add more processes and their tasks
};

// Función para actualizar las tareas mostradas en la interfaz según el proceso seleccionado
function updateTasks(processId) {
  const tasks = processTasks[processId];
  const mainContent = document.querySelector("main");
  let tasksHtml = "";

  tasks.forEach((task, index) => {
    tasksHtml += `
      <div class="col-md-6 mb-4">
          <div class="card task-card">
              <div class="card-body">
                  <h5 class="card-title">${index + 1}. ${task.title}</h5>
                  <button class="btn btn-primary btn-sm btn-process custom-width" onclick="confirmProcess(this, '${task.workflow}')">Confirmar WORKFLOW</button>
                  <button class="btn btn-secondary btn-sm btn-process custom-width" onclick="executeMacro(this)" disabled>Ejecutar Macro</button>
                  <button class="btn btn-secondary btn-sm btn-process custom-width" onclick="publishReport(this)" disabled>Publicar Informe</button>
                  <div class="progress mt-3">
                      <div class="progress-bar" role="progressbar" style="width: 0%; background-color: #1a7e51" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%</div>
                  </div>
              </div>
          </div>
      </div>
    `;
  });

  mainContent.innerHTML = `
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Proceso ${processId}</h1>
    </div>
    <div class="row">
        ${tasksHtml}
    </div>
  `;
}

// Evento para manejar la selección de un proceso en la barra lateral
document.querySelectorAll(".sidebar .nav-link[data-process]").forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    const processId = e.target.getAttribute("data-process");
    updateTasks(processId);
  });
});

// Función para confirmar la eliminación de un proceso
function confirmDelete(processId) {
  if (confirm("¿Está seguro de que desea eliminar este proceso?")) {
    deleteProcess(processId);
  }
}


// contenido para el area de logs
document.getElementById('filterDate').addEventListener('click', function() {
  // Implement date filtering logic here
});

document.getElementById('downloadLogs').addEventListener('click', function() {
  // Implement log download logic here
});

document.querySelectorAll('.copy-log').forEach(button => {
  button.addEventListener('click', function() {
      const logText = this.closest('.log-entry').textContent;
      navigator.clipboard.writeText(logText);
      // Optionally, show a tooltip or alert to confirm the copy action
  });
});


