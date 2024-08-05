import { Skeleton } from "@/components/ui/skeleton";
import React from "react";

const Loading = () => {
  return (
    <div>
      <div className="fp-4 pt-10 lg:p-10 flex flex-col lg:flex-row w-full">
        <div className="hidden lg:inline space-y-4 mx-2">
          <Skeleton className="w-[50px] h-[50px] border rounded-lg" />
          <Skeleton className="w-[50px] h-[50px] border rounded-lg" />
          <Skeleton className="w-[50px] h-[50px] border rounded-lg" />
          <Skeleton className="w-[50px] h-[50px] border rounded-lg" />
        </div>
        <Skeleton className="w-4/5 m-auto md:w-3/5 h-[400px]  border rounded-lg" />
        <div className="flex flex-col space-y-4 p-4 w-full">
          <Skeleton className="w-2/4 h-7 border rounded-lg" />
          <div className="flex gap-3">
            <Skeleton className="w-20 h-4 border rounded-lg" />
            <Skeleton className="w-20 h-4 border rounded-lg" />
            <Skeleton className="w-20 h-4 border rounded-lg" />
          </div>
          <Skeleton className="w-full h-5 border rounded-lg" />
          <Skeleton className="w-3/4 h-7 border rounded-lg" />
          <Skeleton className="w-full h-6 border rounded-lg" />
          <Skeleton className="w-3/5 h-5 border rounded-lg" />
        </div>
      </div>
    </div>
  );
};

export default Loading;
