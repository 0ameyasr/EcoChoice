import { Skeleton } from "@/components/ui/skeleton";
import React from "react";

const Loading = () => {
  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-2">Searching...</h1>
      <h2 className="mb-5 text-gray-400">We wont be long...</h2>
      <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full " />
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full " />
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full " />
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full " />
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full " />
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full] " />
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full " />
        <Skeleton className="shadow-md p-5 rounded-lg h-[300px] w-full " />
      </ul>
    </div>
  );
};

export default Loading;
