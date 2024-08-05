import { cn } from "@/lib/utils";
import Image from "next/image";
import Link from "next/link";
import React from "react";
type Props = {
  title: string;
  query: string;
  className?: string;
  image?: string;
};

const GridOption = ({ title, query, className, image }: Props) => {
  return (
    <Link
      href={{
        pathname: "/search",
        query: { q: query },
      }}
      className={cn("grid-option relative", className)}
    >
      <h2 className="text-xl font-bold">{title}</h2>
      {image && (
        <Image
          src={image}
          alt={title}
          layout="fill"
          className="object-cover opacity-40 hover:opacity-100 transition-all rounded-md"
        />
      )}
    </Link>
  );
};

export default GridOption;
