import { NextRequest, NextResponse } from 'next/server';
import client from '@/lib/mongodb';

interface Product {
  name: string;
  price: number;
  description?: string;
  category: string;
  ecotag?: number;  // Optional, will be added before saving
}

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    const data: Product = await request.json();

    // Call the predict API
    const predictResponse = await fetch('http://localhost:3000/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!predictResponse.ok) {
      throw new Error('Failed to get prediction');
    }

    const prediction = await predictResponse.json();
    const ecotag = prediction.ecotag;  // Assuming the predict API returns { ecotag: 0 or 1 }

    // Add ecotag to the product data
    data.ecotag = ecotag;

    // Save the modified data to MongoDB
    const db = client.db('your-database-name');
    const collection = db.collection('your-collection-name');
    const result = await collection.insertOne(data);

    return NextResponse.json({ success: true, id: result.insertedId }, { status: 200 });
  } catch (error) {
    console.error('Error saving product:', error);
    return NextResponse.json({ success: false, error: error.message }, { status: 500 });
  }
}
