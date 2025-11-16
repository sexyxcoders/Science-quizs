// database/init.js
// Run this script once to initialize MongoDB collections and insert sample data

const { MongoClient } = require("mongodb");
const fs = require("fs");
require("dotenv").config();

const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017";
const DB_NAME = process.env.DB_NAME || "science_quiz_bot";

async function init() {
    const client = new MongoClient(MONGO_URI);

    try {
        await client.connect();
        console.log("✅ Connected to MongoDB");

        const db = client.db(DB_NAME);

        // Create collections
        const usersCol = db.collection("users");
        const questionsCol = db.collection("questions");
        const attemptsCol = db.collection("attempts");

        console.log("✅ Collections created: users, questions, attempts");

        // Load sample questions from backup file
        const questionsData = JSON.parse(fs.readFileSync("./backup/questions.json", "utf8"));

        await questionsCol.insertMany(questionsData);
        console.log(`✅ Inserted ${questionsData.length} sample questions`);

        console.log("🎉 Database initialization complete!");
    } catch (err) {
        console.error("❌ Error initializing database:", err);
    } finally {
        await client.close();
        console.log("MongoDB connection closed");
    }
}

init();
