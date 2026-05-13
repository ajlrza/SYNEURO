import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';
import * as Query from './queries';

const host = process.env.host
const db_name = process.env.db_name
const cert = process.env.cert
const username = process.env.username
const pw = process.env.pw
const port = process.env.port

const queryClient = postgres(host);
export const db =  {
    "Drizzle": drizzle({ client: queryClient }),
    "Query": Query,
};