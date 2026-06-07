import { SyneuroInferencePayload } from '';

export interface ChatMessageEntity extends Omit<SyneuroInferencePayload, 'tokens'> {
  id: string;          // DB Primary Key
  userId: string;      // Foreign Key
  fullText: string;    // Compiled from tokens
  createdAt: Date;     // DB Timestamp
}

export interface dbConfig {
  dbKey: string,
  dbHost: string,
  dbName: string,
  dbCert: string,
  dbUsername: string,
  dbPW: string,
  dbPort: number
}

