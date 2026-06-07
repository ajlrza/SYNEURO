import type {
    CommunicationObject, writeToSlot,
    readActiveSlot, clearSlot
} from './db_comm_interfaces.js';
import * as fs from 'node:fs';

console.log("👀 TypeScript is watching config.json for changes...");

fs.watchFile('bridge.json', (curr, prev) => {
    console.log("🔄 bridge.json has received data!");
    
    // Read the fresh data immediately
    const data = JSON.parse(fs.readFileSync('bridge.json', 'utf-8'));
    const dataObject = data
    if (dataObject.written == true) {
        
    }
});