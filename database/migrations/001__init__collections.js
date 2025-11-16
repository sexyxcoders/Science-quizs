// database/migrations/001_init_collections.js
// MongoDB migration: initializes collections and indexes for Science Quiz Bot

const { MongoClient } = require("mongodb");
require("dotenv").config();

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017";
const DB_NAME = process.env.DB_NAME || "science_quiz_bot";

async function runMigration() {
    const client = new MongoClient(MONGO_URI);

    try {
        await client.connect();
        console.log("✅ Connected to MongoDB");

        const db = client.db(DB_NAME);

        // Create collections if they don't exist
        const collections = await db.listCollections().toArray();
        const collectionNames = collections.map(c => c.name);

        if (!collectionNames.includes("users")) {
            await db.createCollection("users");
            console.log("✅ Created collection: users");
            await db.collection("users").createIndex({ user_id: 1 }, { unique: true });
        }

        if (!collectionNames.includes("questions")) {
            await db.createCollection("questions");
            console.log("✅ Created collection: questions");
            await db.collection("questions").createIndex({ question: 1 }, { unique: true });
        }

        if (!collectionNames.includes("attempts")) {
            await db.createCollection("attempts");
            console.log("✅ Created collection: attempts");
            await db.collection("attempts").createIndex({ user_id: 1, question_id: 1 }, { unique: true });
        }

        console.log("🎉 Migration complete!");
    } catch (err) {
        console.error("❌ Error during migration:", err);
    } finally {
        await client.close();
        console.log("MongoDB connection closed");
    }
}

runMigration();
