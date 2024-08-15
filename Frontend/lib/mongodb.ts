import { MongoClient } from "mongodb";

if (!process.env.MONGODB_URI) {
  throw new Error('Invalid/Missing environment variable: "MONGODB_URI"');
}

const uri = process.env.MONGODB_URI;
const options = { appName: "devrel.template.nextjs" };

let client: MongoClient;

if (process.env.NODE_ENV === "development") {
  // In development mode, use a global variable so that the value
  // is preserved across module reloads caused by HMR (Hot Module Replacement).
  let globalWithMongo = global as typeof globalThis & {
    _mongoClient?: MongoClient;
  };

  if (!globalWithMongo._mongoClient) {
    globalWithMongo._mongoClient = new MongoClient(uri, options);
  }
  client = globalWithMongo._mongoClient;
} else {
  // In production mode, it's best to not use a global variable.
  client = new MongoClient(uri, options);
}

async function checkConnection() {
    try {
      await client.connect();
      console.log("Successfully connected to MongoDB");
      // Optionally, you can close the connection after the check
      // await client.close();
    } catch (error) {
      console.error("Failed to connect to MongoDB", error);
      throw new Error("Failed to connect to MongoDB");
    }
  }
  
// Export a module-scoped MongoClient. By doing this in a
// separate module, the client can be shared across functions.
checkConnection();
export default client;