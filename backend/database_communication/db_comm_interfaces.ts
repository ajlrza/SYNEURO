export interface CommunicationObject {
    userID: number;
    userMessage: string;
    messageDate: Date; 
    messageTime: string
    dbQuery: string
}

export interface writeToSlot {
    (queryObject: CommunicationObject, slotNumber: number): string // "Success" output value with performance stats?
}


export interface readActiveSlot {
    (slotNumber: number): boolean // true || false -> active or not
}

export interface clearSlot {
    
}