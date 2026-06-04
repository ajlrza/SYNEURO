import { db } from '../backend_config/db.js';
import type {
    CommunicationObject, writeToSlot,
    readActiveSlot, clearSlot
} from './db_comm_interfaces.js';
import * as fs from 'node:fs';

// what if since the frontend is in TSX too
// User messages, query, and loading stuff will be sent to TS and Python at the same time
// Since the frontend logic would dictate how the user is acting right?, so if it
// wants to load the message (automatically), it sends both to TS and Python, vice versa
// and through TS, the query stuff could be handed to TS as middleman, to JS, so no more python? nah stillthere is

console.log("👀 TypeScript is watching config.json for changes...");

fs.watchFile('bridge.json', (curr, prev) => {
    console.log("🔄 bridge.json has received data!");
    
    // Read the fresh data immediately
    const data = JSON.parse(fs.readFileSync('bridge.json', 'utf-8'));
    const dataObject = data
    if (dataObject.written == true) {
        query(dataObject.Communication.Object)
    }
});

export async function query(object: CommunicationObject | undefined) {
    const Query = db.Query;
    const Drizzle = db.Drizzle;
    const hashMap = new Map()

    if (object == undefined) {
        console.log("Error, could not process request. The query or data object may have been undefined.");
        // Return this for the frontend to send a request / try again, 
        // If front-end receives this error, it'll request again.
        return {"Data Error": true, "Cause": "Undefined input"};
    }
    const queryObject = object; // safe: object checked above

    const userID: number  = queryObject.userID;
    const userMessage: string  = queryObject.userMessage;
    const messageTimestamp: Date = new Date(`${queryObject.messageDate}T${queryObject.messageTime}Z`);
    
    hashMap.set("sprite", Query.load_sprite(userID, Drizzle));
    hashMap.set("load_messages", Query.load_message(userMessage, Drizzle));
    hashMap.set("save_message", Query.save_message(userMessage, Drizzle));
    hashMap.set("save_conversation", Query.save_conversation(object, Drizzle));
    hashMap.set("display_conversation", Query.display_conversation(userID, Drizzle));
    hashMap.set("load_conversation_history", Query.load_conversation_history(userID, Drizzle));

    const result = await hashMap.get(queryObject.dbQuery);
    return result;

} 