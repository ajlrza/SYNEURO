import { db } from './config/db'

export async function query(query: String | undefined, object: Object | undefined) {
    const Query = db.Query;
    const Drizzle = db.Drizzle;
    const hashMap = new Map()

    if (query == undefined || object == undefined) {
        console.log("Error, could not process request. The query or data object may have been undefined.");
        // Return this for the frontend to send a request / try again, 
        // If front-end receives this error, it'll request again.
        return {"Data Error": true, "Cause": "Undefined input"};
    }

    const userID: number  = object.userID;
    const userMessage: String  = object.userMessage;
    const messageDate: Date  = object.messageDate;

    hashMap.set("sprite", Query.load_sprite(userID, Drizzle));
    hashMap.set("load_messages", Query.load_message(userMessage, Drizzle));
    hashMap.set("save_message", Query.save_message(userMessage, Drizzle));
    hashMap.set("save_conversation", Query.save_conversation(object, Drizzle));
    hashMap.set("display_conversation", Query.display_conversation(userID, Drizzle));
    hashMap.set("load_conversation_history", Query.load_conversation_history(userID, Drizzle));

    const result = await hashMap.get(query);
    return result;

} 