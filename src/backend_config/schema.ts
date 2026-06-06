import { pgTable, integer, date, varchar } from "drizzle-orm/pg-core";

// dgs_main SCHEMA

export const usersTB = pgTable("users", {
    userID: integer().primaryKey().generatedAlwaysAsIdentity(),
    username: varchar().notNull(),
    joinDate: date().notNull(),
    userStatus: varchar().notNull()
})

export const gfTB = pgTable("ai_girlfriends", {
    gfID: integer().primaryKey().generatedAlwaysAsIdentity(),
    gfKey: integer().notNull(),
    gfName: varchar().notNull(),
    gfAPi: varchar().notNull(),
    gfStatus: varchar().notNull(),
    gfUserCount: integer()
})

export const pTB = pgTable("pw", {
    userID: integer().primaryKey().generatedAlwaysAsIdentity(),
    // I need a custom data type??!
    userPW: varchar().notNull()
})

// dgs_messages SCHEMA

export const userMessagesTB_A = pgTable("user_messages_a", {
    userID: integer().primaryKey().generatedAlwaysAsIdentity(),
    userMessage: varchar().notNull(),
    messageDate: date().notNull()
})

export const userMessagesTB_B = pgTable("user_messages_b", {
    userID: integer().primaryKey().generatedAlwaysAsIdentity(),
    userMessage: varchar().notNull(),
    messageDate: date().notNull()
})