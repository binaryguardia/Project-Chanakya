const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadFile(path.join(__dirname, 'index.html'));
}

function createResultWindow(title, content) {
  let resultWindow = new BrowserWindow({
    width: 800,
    height: 600,
    parent: mainWindow,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  resultWindow.loadFile(path.join(__dirname, 'result.html'));

  resultWindow.webContents.on('did-finish-load', () => {
    resultWindow.webContents.send('update-content', { title, content });
  });
}

// Check if we're running in Electron
if (process.versions.electron) {
  app.whenReady().then(createWindow);

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
      app.quit();
    }
  });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });

  ipcMain.on('open-result-window', (event, { title, content }) => {
    createResultWindow(title, content);
  });
} else {
  console.log('This script is meant to be run with Electron. Please use the appropriate Electron command to start the app.');
}

// For testing purposes when running with Node.js
if (!process.versions.electron) {
  console.log('Running in Node.js environment. Electron features will not be available.');
  // You can add any Node.js specific code or tests here
}
