// AI Gf Sprite Load

export async function load_sprite(userid: number, Drizzle: any) {
    const get_gf_id = await Drizzle.execute('select 1');
    
    const load = await sql`
    select gf from AI_girlfriends
    where gfID = ${gfid}
    `
}

// Load messages on user side if conversation is opened

export async function load_message(usermessage: object, Drizzle: any) {
    const message_object: object = usermessage;
    const message: string = message_object.message;
    const userid: number = message_object.userid;
    const messagedate: Date = message_object.date;

    if (message_object && Object.keys(message_object).length > 1) {
        const load = await sql`
        select message from messages
        where ${userid} == ${messages.userid}
        and where ${messagedate} == ${messages.messagedate}
        `;
    }
}

// Save messages each time a message is sent

export async function save_message(usermessage: object, Drizzle: any) {
    const message_object = usermessage;
    const message: string = message_object.message;
    const userid: number = message_object.userid;
    const messagedate: Date = message_object.date;

    if (message_object && Object.keys(message_object).length > 1) {
        const save = await sql`
        insert into messages (message)
        values (${message})
        where ${userid} == ${messages.userid}
        `;
    }
}

// Save conversations history for redundancy and data load

export async function save_conversation(messageschunk: object, Drizzle: any) {
    const messageschunk_object = messageschunk;
    const messages: string = messageschunk_object.messages;
    const userid: number = messageschunk_object.userid;
    const messagedate: Date = messageschunk_object.date;

    if (message_object && Object.keys(messageschunk_object).length > 1){
        const save = await sql`
        insert into messages (conversationhistory)
        values (${userid}, ${messages}, ${messagedate})
        where ${userid} == ${messages.userid}
        `
    }
}

// Load conversation in the conversation history section

export async function load_conversation_history(userid: number, Drizzle: any) {
    const userid_number = userid;
    if (userid_number) {
        const load_conversation: Object = await sql`
        select conversationhistory from messages
        where ${userid} == ${messages.userid}
        `
    }
}

// Display previous conversations in conversation history

export async function display_conversation(userid: number, Drizzle: any) {
    const userid_number = userid;
    if (userid_number) {
        const display_conversation: Object = await sql`
        select conversationname, date from messages
        where ${userid} == ${messages.userid}
        `
    }
}
