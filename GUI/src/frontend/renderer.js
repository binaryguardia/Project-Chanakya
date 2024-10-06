const { ipcRenderer } = require('electron');
const { exec } = require('child_process');
const path = require('path');

function runCommand(command, title) {
    console.log(`Running command: ${command}`);
    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            showResult(title, `Error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            showResult(title, `Error: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        showResult(title, stdout);
    });
}

function showResult(title, content) {
    ipcRenderer.send('open-result-window', { title, content });
}

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.clickable');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const title = button.textContent.trim();
            switch (title) {
                case 'Check your Machine Health':
                    runCommand(`python3 "${path.join(__dirname, '..', 'backend', 'machine_health.py')}"`, title);
                    break;
                case 'Check for external Drives':
                    runCommand(`python3 "${path.join(__dirname, '..', 'backend', 'disk_analysis.py')}"`, title);
                    break;
                default:
                    showResult(title, 'Functionality not implemented yet.');
            }
        });
    });
});
