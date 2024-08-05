import Product from "@/components/Product";
import { fetchSearch } from "@/lib/fetchSearch";
import React from "react";

type Props = {
  searchParams: {
    q: string;
  };
};

const SearchPage = async ({ searchParams: { q } }: Props) => {
  await delay(1000);
  const results = await fetchSearch(q);
  console.log(results);
  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-2">Result for {q}</h1>
      <h2 className="mb-5 text-gray-400">({results?.total}) results</h2>
      <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
        {results?.products.map((product) => (
          <li key={product.id} className="">
            <Product product={product} />
          </li>
        ))}
      </ul>
    </div>
  );
};
const delay = (ms: any) => new Promise((res) => setTimeout(res, ms));

export default SearchPage;
